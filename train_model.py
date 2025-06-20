import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os



# ✅ Normalization helper
def normalize(text):
    return text.lower().replace('-', ' ').strip()

# ✅ Load and preprocess the dataset
def load_dataset():
    try:
        df = pd.read_csv('dataset/career_data.csv')

        # Normalize
        df['Skills'] = df['Skills'].str.split(', ').apply(lambda lst: [normalize(skill) for skill in lst])
        df['Interests'] = df['Interests'].str.split(', ').apply(lambda lst: [normalize(interest) for interest in lst])
        df['Career'] = df['Career'].str.strip()
        df['Description'] = df['Description'].str.strip()

        print(f"✅ Loaded {len(df)} entries")
        print("📊 Career distribution BEFORE balancing:\n", df['Career'].value_counts())
        return df
    except FileNotFoundError:
        print("❌ File 'career_data.csv' not found.")
        return None

# ✅ Balance dataset manually (oversampling)
def balance_dataset(df):
    max_count = df['Career'].value_counts().max()
    balanced_df = pd.DataFrame()

    for career, group in df.groupby('Career'):
        samples = group.sample(max_count, replace=True, random_state=42)
        balanced_df = pd.concat([balanced_df, samples], axis=0)

    print("📊 Career distribution AFTER balancing:\n", balanced_df['Career'].value_counts())
    return balanced_df.sample(frac=1, random_state=42).reset_index(drop=True)

# ✅ Main training function
def train_career_model():
    df = load_dataset()
    if df is None:
        return None

    # Combine features
    df['combined_features'] = df['Interests'] + df['Skills']

    # Encode features
    mlb = MultiLabelBinarizer()
    X_encoded = mlb.fit_transform(df['combined_features'])
    y = df['Career']

    print(f"✅ Feature matrix shape: {X_encoded.shape}")
    print(f"✅ Unique careers: {y.nunique()}")

    # Balance the dataset
    df_encoded = pd.DataFrame(X_encoded, columns=mlb.classes_)
    df_encoded['Career'] = y.values
    df_balanced = balance_dataset(df_encoded)

    X = df_balanced.drop(columns=['Career']).values
    y_balanced = df_balanced['Career']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y_balanced, test_size=0.2, random_state=42)

    # Train model
    print("\n🤖 Training RandomForestClassifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"✅ Accuracy: {accuracy:.2f}")
    print("\n📄 Classification Report:\n", classification_report(y_test, y_pred))

    # Map descriptions
    description_map = {normalize(career): desc for career, desc in zip(df['Career'], df['Description'])}


    # Save model package
    model_package = {
        'classifier': model,
        'feature_encoder': mlb,
        'feature_names': list(mlb.classes_),
        'careers': list(y.unique()),
        'descriptions': description_map
    }

    os.makedirs('model', exist_ok=True)
    with open('model/career_model.pkl', 'wb') as f:
        pickle.dump(model_package, f)

    print("✅ Model saved to model/career_model.pkl")
    return model_package

# ✅ Execute when run directly
if __name__ == "__main__":
    train_career_model()
    print("🚀 Training complete!")
    print("=",*60)