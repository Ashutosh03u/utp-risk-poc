# =========================================================
# FILE: generate_data.py
# =========================================================

import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2024-01-01", periods=12, freq="M")

activity_score = np.clip(np.linspace(0.9, 0.3, 12) + np.random.normal(0, 0.05, 12), 0, 1)

volatility = np.clip(np.random.normal(0.25, 0.08, 12), 0, 1)

leverage_ratio = np.clip(np.linspace(0.4, 0.8, 12) + np.random.normal(0, 0.05, 12), 0, 1)

df = pd.DataFrame({
    "date": dates,
    "activity_score": activity_score,
    "volatility": volatility,
    "leverage_ratio": leverage_ratio
})

df.to_csv("activity_data.csv", index=False)

print("Sample dataset created.")
