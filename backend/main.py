from fastapi import FastAPI, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from io import StringIO
import pandas as pd
from app.models import GeneProfile
from app.schemas import GeneCreate, GeneResponse
from app.crud import create_gene, get_all_gene_profiles, get_gene_comparison
from app.database import get_db , engine

app = FastAPI()
@app.get("/")
async def startup_event():
    try:
        with engine.connect() as connection:
            connection.execute("SELECT 1")  # Test connection to the database
        print("Database connection successful!")
    except Exception as e:
        print(f"Database connection failed: {str(e)}")

@app.post("/upload/")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        # Read the uploaded file
        contents = await file.read()
        df = pd.read_csv(StringIO(contents.decode("utf-8")))

        # Validate columns
        required_columns = {"gene", "type", "alteration", "alt_type"}
        if not required_columns.issubset(df.columns):
            missing = required_columns - set(df.columns)
            raise HTTPException(status_code=400, detail=f"Missing columns: {missing}")

        # Insert data into database
        for _, row in df.iterrows():
            gene_data = GeneCreate(
                gene=row["gene"],
                type=row["type"],
                alteration=row["alteration"],
                alt_type=row["alt_type"]
            )
            create_gene(db, gene_data)

        return {"message": "CSV uploaded and data inserted successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")


@app.post("/compare/")
async def compare_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        # Read the uploaded file
        contents = await file.read()
        upload_df = pd.read_csv(StringIO(contents.decode("utf-8")))

        # Validate columns
        required_columns = {"gene", "type", "alteration", "alt_type"}
        if not required_columns.issubset(upload_df.columns):
            missing = required_columns - set(upload_df.columns)
            raise HTTPException(status_code=400, detail=f"Missing columns: {missing}")

        # Get all reference profiles from the database
        reference_profiles = get_all_gene_profiles(db)

        # Convert reference profiles to a DataFrame
        reference_df = pd.DataFrame([{
            "gene": row.gene,
            "type": row.type,
            "alteration": row.alteration,
            "alt_type": row.alt_type
        } for row in reference_profiles])

        # Compare uploaded data with reference data
        comparison = pd.merge(upload_df, reference_df, on="gene", how="inner", suffixes=("_uploaded", "_reference"))

        return {
            "message": "Comparison complete",
            "results": comparison.to_dict(orient="records")
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error comparing gene profiles: {str(e)}")