import pandas as pd
import os

raw_path = 'data/raw/netflix_movies_detailed_up_to_2025.csv'
cleaned_path = 'data/processed/movies.csv' # using the processed one if it exists

print("=== RAW DATA ===")
if os.path.exists(raw_path):
    df_raw = pd.read_csv(raw_path)
    print(df_raw.shape)
    print(df_raw.columns)
    print(df_raw.isnull().sum())
    print("Unique shows:", df_raw['show_id'].nunique())
else:
    print("Raw file not found")

print("\n=== CLEANED DATA ===")
if os.path.exists(cleaned_path):
    df_clean = pd.read_csv(cleaned_path)
    print(f"Cleaned Shape: {df_clean.shape}")
    raw_rows = len(df_raw) if 'df_raw' in locals() else 0
    clean_rows = len(df_clean)
    diff = raw_rows - clean_rows
    if raw_rows > 0:
        pct = (diff / raw_rows) * 100
        print(f"Removed rows: {diff} ({pct:.2f}%)")
else:
    print("Cleaned file not found")

