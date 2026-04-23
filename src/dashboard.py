# =========================================================
# FILE: visualization.py
# =========================================================

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("utp_risk_output.csv")

plt.figure(figsize=(10,5))

plt.plot(df["date"], df["activity_score"], label="Activity Score")
plt.plot(df["date"], df["utp_risk_score"], label="UTP Risk Score")

plt.xticks(rotation=45)

plt.xlabel("Date")
plt.ylabel("Score")

plt.title("Industrial Activity vs UTP Risk")

plt.legend()

plt.tight_layout()

plt.show()
