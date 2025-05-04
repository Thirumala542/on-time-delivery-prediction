# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv("Train.csv")
df.dropna(inplace=True)

# Encode categorical variables
label_cols = ['Warehouse_block', 'Mode_of_Shipment', 'Product_importance', 'Gender']
encoders = {}
for col in label_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# Save encoders for reuse
joblib.dump(encoders, "encoders.pkl")

# Features and target
X = df.drop(['ID', 'Reached.on.Time_Y.N'], axis=1)
y = df['Reached.on.Time_Y.N']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(random_state=50)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model.pkl")
print("Model and encoders saved.")
