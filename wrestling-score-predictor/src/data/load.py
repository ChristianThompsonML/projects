import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
df = pd.read_csv(BASE_DIR / "data/raw/wrestler_tournament_data_2023-2025.csv")

print(df.shape)
print(df.columns)
print(df.head())