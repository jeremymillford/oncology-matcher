import pandas as pd
import matplotlib.pyplot as plt
import os

# Directory for saving generated plots
PLOT_DIR = "/usr/src/app"

def compare_files(uploaded_df, db_df):
    try:
        # Debugging: Inspect the incoming dataframes
        print("Uploaded DataFrame:")
        print(uploaded_df.head())
        print("Database DataFrame:")
        print(db_df.head())
        
        # Force columns to be consistent (string type for merging)
        uploaded_df['gene'] = uploaded_df['gene'].astype(str)
        db_df['gene'] = db_df['gene'].astype(str)
        
        # Merge on gene and alt_type columns
        comparison_result = pd.merge(uploaded_df, db_df, on=["gene", "alt_type"], how="inner")

        # Check if comparison_result has valid data to plot
        if comparison_result.empty:
            print("No matching data found for comparison!")
            return {"error": "No matching data found."}

        # Debugging: Inspect merged result
        print("Comparison Result DataFrame:")
        print(comparison_result)

        # Generate bar plot for gene frequency comparison
        plot_path = os.path.join(PLOT_DIR, "comparison_plot.png")  # Absolute path for saving the plot
        plt.figure(figsize=(10, 5))
        comparison_result["gene"].value_counts().plot(kind="bar", color='blue', alpha=0.7)
        plt.title("Gene Comparison - Frequency of Matches")
        plt.xlabel("Gene")
        plt.ylabel("Frequency")
        plt.tight_layout()

        # Save the plot to the specified path
        plt.savefig(plot_path)
        print(f"Plot generated and saved to: {plot_path}")

        return {"plot_path": "comparison_plot.png", "matched_count": len(comparison_result)}
    except Exception as e:
        print(f"Error comparing files: {e}")
        return {"error": str(e)}