# =========================================================
# FILE: feature_engineering.py
# =========================================================

import pandas as pd

df = pd.read_csv("activity_data.csv")

df["activity_change"] = df["activity_score"].pct_change()

df["activity_change"] = df["activity_change"].fillna(0)

df.to_csv("featured_data.csv", index=False)

print(df.head())
