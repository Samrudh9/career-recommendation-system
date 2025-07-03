import os
import pandas as pd
import joblib
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# ─────────────────── Hard‑coded file paths ────────────────────
CSV_PATH = "dataset/career_data_with_qualifications.csv"
MODEL_OUT = "model/salary_model.pkl"

# ─────────────────── Load & validate data ────────────────────
if not os.path.exists(CSV_PATH):
    raise FileNotFoundError(f"CSV not found: {CSV_PATH}")

df = pd.read_csv(CSV_PATH)
REQ = {"Skills", "Career", "Qualification_required", "Entry_level_salary"}
missing = REQ - set(df.columns)
if missing:
    raise ValueError(f"CSV missing columns: {missing}")

X = df[["Skills", "Career", "Qualification_required"]]
y = df["Entry_level_salary"]

# ─────────────────── Preprocess text + categorical ────────────
pre = ColumnTransformer([
    ("skills_tf", TfidfVectorizer(token_pattern=r"[^,]+", lowercase=True), "Skills"),
    ("career_ohe", OneHotEncoder(sparse_output=False, handle_unknown="ignore"), ["Career"]),
    ("qual_ohe",  OneHotEncoder(sparse_output=False, handle_unknown="ignore"), ["Qualification_required"]),
], remainder="drop")

base_reg = Pipeline([
    ("pre", pre),
    ("rf", RandomForestRegressor(n_estimators=200, random_state=42))
])

# Wrap with target transformation: log1p ↔ expm1
model = TransformedTargetRegressor(
    regressor=base_reg,
    func=np.log1p,
    inverse_func=np.expm1,
)

# ───────────────────── Train / test split ─────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model.fit(X_train, y_train)

# Evaluate on original scale
preds = model.predict(X_test)
print(f"R² on test set: {r2_score(y_test, preds):.3f}")

# ───────────────────── Save model ─────────────────────────────
os.makedirs(os.path.dirname(MODEL_OUT), exist_ok=True)
joblib.dump(model, MODEL_OUT)
print(f"✅ Trained model saved to: {MODEL_OUT}")
# ───────────────────── End of script ─────────────────────────
# This script trains a salary estimation model using a dataset of career data with qualifications.
# It preprocesses the data, trains a RandomForestRegressor, and saves the model to disk.
# The model can then be loaded for salary estimation tasks in other scripts.            