# =========================================================
# FILE: risk_model.py
# =========================================================

import pandas as pd
import numpy as np

df = pd.read_csv("featured_data.csv")

# weights
w1 = 0.5
w2 = 0.3
w3 = 0.2

df["utp_risk_score"] = (
    w1 * (1 - df["activity_score"]) +
    w2 * df["volatility"] +
    w3 * df["leverage_ratio"]
)

def classify_risk(score):
    if score < 0.4:
        return "LOW"
    elif score < 0.7:
        return "MEDIUM"
    else:
        return "HIGH"

df["risk_level"] = df["utp_risk_score"].apply(classify_risk)

print(df[[
    "date",
    "activity_score",
    "volatility",
    "leverage_ratio",
    "utp_risk_score",
    "risk_level"
]])

df.to_csv("utp_risk_output.csv", index=False)
