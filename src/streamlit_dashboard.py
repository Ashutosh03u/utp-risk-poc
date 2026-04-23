# =========================================================
# FILE: streamlit_dashboard.py
# =========================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Satellite-Based UTP Risk Monitoring")

df = pd.read_csv("utp_risk_output.csv")

st.dataframe(df)

fig, ax = plt.subplots(figsize=(10,5))

ax.plot(df["date"], df["activity_score"], label="Activity Score")
ax.plot(df["date"], df["utp_risk_score"], label="UTP Risk Score")

ax.set_xlabel("Date")
ax.set_ylabel("Score")

ax.legend()

plt.xticks(rotation=45)

st.pyplot(fig)

high_risk = df[df["risk_level"] == "HIGH"]

st.subheader("High Risk Periods")

st.dataframe(high_risk)
