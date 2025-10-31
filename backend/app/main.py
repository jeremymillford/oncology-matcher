from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
import os
from app.file_processing import compare_files
from app.db import get_comparison_data
from fastapi.staticfiles import StaticFiles

UPLOAD_FOLDER = "uploaded_files"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = FastAPI()

# Mount static files directory to serve the plot
app.mount("/static", StaticFiles(directory="/usr/src/app", html=True), name="static")

@app.get("/")
async def root():
    return {"message": "Backend is running successfully!"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Save the uploaded file locally
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(file_path, "wb") as f:
            f.write(await file.read())
        
        # Attempt to load the file as a CSV
        try:
            uploaded_df = pd.read_csv(file_path)
        except Exception as e:
            raise HTTPException(status_code=422, detail=f"Invalid file format: {str(e)}")
        
        # Check required columns in the CSV file
        required_columns = {"gene", "type", "alteration", "alt_type"}
        if not set(required_columns).issubset(uploaded_df.columns):
            raise HTTPException(
                status_code=422,
                detail=f"CSV file does not contain required columns: {required_columns}"
            )
        
        # Fetch data from the database to compare with
        db_data = get_comparison_data()
        if db_data is None:
            raise HTTPException(status_code=500, detail="Failed to fetch data from the database.")

        # Compare uploaded file with database and generate plot
        comparison_result = compare_files(uploaded_df, db_data)
        if "error" in comparison_result:
            raise HTTPException(status_code=400, detail="Comparison failed: " + comparison_result["error"])
        
        # Return the path to the generated plot file and the matched count
        return {"plot_path": comparison_result["plot_path"], "matched_count": comparison_result["matched_count"]}
    
    except Exception as e:
        print(f"Error uploading file: {e}")
        raise HTTPException(status_code=500, detail="An error occurred during file upload.")