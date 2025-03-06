import os
import pandas as pd
import numpy as np

# Set paths relative to the project
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_excel_path = os.path.join(project_root, "Data", "Kleine_data.xlsx")

# Load the original Excel file
df = pd.read_excel(C:\Users\corne\Documents\thesis-question-classification\Data\Grote_data.xlsx

# Get the total number of rows
total_rows = len(df)
print(f"Total rows in original dataset: {total_rows}")

# Take 1000 random rows (or all if less than 1000)
sample_size = min(1000, total_rows)
random_sample = df.sample(n=sample_size, random_state=42)  # Set random_state for reproducibility
print(f"Sampled {sample_size} rows randomly")

# Save the random sample to a new Excel file
random_sample.to_excel(output_excel_path, index=False, engine="openpyxl")
print(f"Random sample saved to: {output_excel_path}")