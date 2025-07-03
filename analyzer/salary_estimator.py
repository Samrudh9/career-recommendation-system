import pandas as pd
import joblib
from datetime import datetime
from pathlib import Path
from typing import Tuple, Union

import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.pipeline import Pipeline


class SalaryEstimator:

    def __init__(self,
                 model_path: Union[str, Path] = "model/salary_model.pkl",
                 csv_path: Union[str, Path] = "dataset/career_data_with_qualifications.csv"):
        self.model_path = Path(model_path)
        if self.model_path.exists():
            self.pipeline = joblib.load(self.model_path)
            print(f"✅ Salary model loaded from: {self.model_path}")
        else:
            print("⚠️  Salary model not found — training a new one…")
            self._train_and_save(csv_path)

        self.last_updated = datetime.now()

    # ------------------------------------------------------------------
    def _train_and_save(self, csv_path: Union[str, Path]):
        csv_path = Path(csv_path)
        if not csv_path.exists():
            raise FileNotFoundError(f"CSV file not found for training: {csv_path}")

        df = pd.read_csv(csv_path)
        req = {"Skills", "Career", "Qualification_required", "Entry_level_salary"}
        missing = req - set(df.columns)
        if missing:
            raise ValueError(f"CSV missing required columns: {missing}")

        X = df[["Skills", "Career", "Qualification_required"]]
        y = df["Entry_level_salary"]

        pre = ColumnTransformer([
            ("skills_tf", TfidfVectorizer(token_pattern=r"[^,]+", lowercase=True), "Skills"),
            ("career_ohe", OneHotEncoder(sparse_output=False, handle_unknown="ignore"), ["Career"]),
            ("qual_ohe",  OneHotEncoder(sparse_output=False, handle_unknown="ignore"), ["Qualification_required"]),
        ])

        base_reg = Pipeline([
            ("pre", pre),
            ("rf", RandomForestRegressor(n_estimators=200, random_state=42))
        ])

        self.pipeline = TransformedTargetRegressor(
            regressor=base_reg,
            func=np.log1p,
            inverse_func=np.expm1,
        )

        self.pipeline.fit(X, y)
        self.model_path.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(self.pipeline, self.model_path)
        print(f"✅ New salary model trained and saved to {self.model_path}")

    # ------------------------------------------------------------------
    def estimate(self, *, skills: str, career: str, qualification: str) -> Tuple[int, None]:
        """Predict salary based on user‑provided features."""
        df_in = pd.DataFrame([{
            "Skills": skills,
            "Career": career,
            "Qualification_required": qualification
        }])
        salary = int(round(self.pipeline.predict(df_in)[0]))
        return salary, None  # second value reserved for future metrics


# Global singleton for easy Flask import
salary_est = SalaryEstimator()
