import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime
import joblib

class SalaryEstimator:
    
    def __init__(self, base_data_path, trend_data_path):
        self.base_salaries = self._load_base_data(base_data_path)
        self.trend_data = self._load_trend_data(trend_data_path)
        self.model = self._train_model()
        self.last_updated = datetime.now()
        
    def _load_base_data(self, path):
        """Load base salary data with career descriptions"""
        df = pd.read_csv(path)
        # Ensure required columns exist
        required_cols = ['role', 'base_salary', 'description', 'experience_multiplier']
        if not set(required_cols).issubset(df.columns):
            raise ValueError(f"Base data missing required columns: {required_cols}")
        return df.set_index('role')
    
    def _load_trend_data(self, path):
        """Load monthly trend adjustment data"""
        df = pd.read_csv(path, parse_dates=['month'])
        # Ensure required columns exist
        required_cols = ['role', 'month', 'trend_adjustment']
        if not set(required_cols).issubset(df.columns):
            raise ValueError(f"Trend data missing required columns: {required_cols}")
        return df
    
    def _train_model(self):
        """Train trend prediction model"""
        # Prepare data for modeling
        trend_pivot = self.trend_data.pivot_table(
            index='month', 
            columns='role', 
            values='trend_adjustment'
        ).fillna(0)
        
        # Create features (months as numeric values)
        X = np.array([(x - trend_pivot.index.min()).days for x in trend_pivot.index]).reshape(-1, 1)
        
        # Train separate model for each role
        models = {}
        for role in trend_pivot.columns:
            y = trend_pivot[role].values
            model = LinearRegression()
            model.fit(X, y)
            models[role] = model
            
        return models
    
    def _get_trend_adjustment(self, role, current_date=None):
        """
        Calculate current trend adjustment for a role
        Uses linear regression to project current month's adjustment
        """
        current_date = current_date or datetime.now()
        last_data_point = self.trend_data['month'].max()
        
        # Calculate days since first trend data point
        days_since_start = (current_date - self.trend_data['month'].min()).days
        
        # Get prediction from model
        adjustment = self.model[role].predict([[days_since_start]])[0]
        
        # Cap adjustments to reasonable ranges
        return max(-0.3, min(0.5, adjustment))
    
    def estimate_salary(self, role, experience_years=5, location="India", current_date=None):
        """
        Estimate salary with auto-adjusted trends
        Returns tuple: (adjusted_salary, explanation)
        """
        # Get base salary data
        if role not in self.base_salaries.index:
            raise ValueError(f"Role '{role}' not in database")
        
        base_data = self.base_salaries.loc[role]
        base_salary = base_data['base_salary']
        
        # Apply experience multiplier
        experience_multiplier = base_data['experience_multiplier']
        experienced_salary = base_salary * (1 + experience_multiplier * min(experience_years/10, 1))
        
        # Apply trend adjustment
        trend_adj = self._get_trend_adjustment(role, current_date)
        adjusted_salary = experienced_salary * (1 + trend_adj)
        
        # Generate explanation
        explanation = (
            f"Base salary: ${base_salary:,.0f}\n"
            f"+ Experience ({experience_years} yrs): ${experienced_salary - base_salary:,.0f}\n"
            f"+ Current trend ({trend_adj*100:.1f}%): ${adjusted_salary - experienced_salary:,.0f}\n\n"
            f"Why this career?\n{base_data['description']}"
        )
        
        return round(adjusted_salary), explanation
    
    def update_model(self, new_data_path):
        """Update model with new trend data"""
        new_data = pd.read_csv(new_data_path, parse_dates=['month'])
        self.trend_data = pd.concat([self.trend_data, new_data])
        self.model = self._train_model()
        self.last_updated = datetime.now()
        print(f"Model updated successfully at {self.last_updated}")
        
    def save_model(self, path):
        """Save current model state"""
        joblib.dump({
            'model': self.model,
            'trend_data': self.trend_data,
            'base_salaries': self.base_salaries,
            'last_updated': self.last_updated
        }, path)
        
    @classmethod
    def load_model(cls, path):
        """Load saved model state"""
        data = joblib.load(path)
        estimator = cls.__new__(cls)
        estimator.model = data['model']
        estimator.trend_data = data['trend_data']
        estimator.base_salaries = data['base_salaries']
        estimator.last_updated = data['last_updated']
        return estimator

# Sample Usage
if __name__ == "__main__":
    # Initialize with data files
    estimator = SalaryEstimator(
        base_data_path="data/base_salaries.csv",
        trend_data_path="data/trends.csv"
    )
    
    # Get salary estimate with explanation
    salary, explanation = estimator.estimate_salary(
        role="AI Engineer", 
        experience_years=4
    )
    
    print(f"Estimated Salary: ${salary:,}")
    print(f"\nExplanation:\n{explanation}")
    
    # Update model with new trend data
    estimator.update_model("/dataset/")
    
    # Save model state
    estimator.save_model("models/salary_estimator.pkl")