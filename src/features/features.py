import pandas as pd

def housing_stock(df: pd.DataFrame):
    df['New housing stock'] = df['YearBuilt']
    df['New housing stock'] = df['YearBuilt'].apply(lambda x: 1 if (x >= 1990) else 0)
    return df