import pandas as pd
import numpy as np

def compare_gene_profiles(upload_df, reference_df):
    merged = pd.merge(upload_df, reference_df, on="Gene", suffixes=("_upload", "_ref"))
    merged["Difference"] = (merged["Expression_upload"] - merged["Expression_ref"]).abs()
    return merged.pivot(index="Gene", columns=None, values="Difference")
