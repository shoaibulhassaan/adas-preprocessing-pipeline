from .cleaner import clean_data
from .feature_engineer import extract_features
from .utils import load_csv, save_csv

def run_pipeline(csv_path, output_path="cleaned_data.csv"):
    df = load_csv(csv_path)
    df = clean_data(df)
    df = extract_features(df)
    save_csv(df, output_path)
    return df

