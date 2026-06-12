import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("Crop_recommendation.csv")

X = df.drop("label", axis=1)
y = df["label"]

# Train model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X, y)
