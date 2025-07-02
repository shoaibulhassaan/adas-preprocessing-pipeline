import pandas as pd

def load_csv(path):
    return pd.read_csv(path)

def save_csv(df, output_path="cleaned_data.csv"):
    df.to_csv(output_path, index=False)
