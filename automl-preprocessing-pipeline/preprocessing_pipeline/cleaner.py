import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

def clean_data(df):
    # Drop columns with more than 50% missing values
    df = df.loc[:, df.isnull().mean() < 0.5]

    # Fill numeric columns with median
    numeric_cols = df.select_dtypes(include=['number']).columns
    imputer = SimpleImputer(strategy='median')
    df[numeric_cols] = imputer.fit_transform(df[numeric_cols])

    return df
