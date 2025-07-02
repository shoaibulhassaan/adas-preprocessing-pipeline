from preprocessing_pipeline import run_pipeline

# Replace 'your_data.csv' with your input file
df = run_pipeline("your_data.csv")
print("Processed Data:\n", df.head())
