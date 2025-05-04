import joblib
import os
import pytest

def test_model_load_and_predict():
    model_path = os.path.join("app", "model.pkl")
    model = joblib.load(model_path)

    # Sample encoded features based on training pipeline
    sample_input = [[5, 2, 2, 160, 3, 2, 1, 44, 1233]]  # Assume label-encoded values

    prediction = model.predict(sample_input)
    assert prediction in [[0], [1], [0.0], [1.0]], "Prediction should be 0 or 1"
