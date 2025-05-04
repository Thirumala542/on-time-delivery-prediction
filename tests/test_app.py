from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)

def test_predict_endpoint():
    payload = {
        "Warehouse_block": "F",
        "Mode_of_Shipment": "Ship",
        "Customer_care_calls": 3,
        "Customer_rating": 4,
        "Cost_of_the_Product": 160,
        "Prior_purchases": 3,
        "Product_importance": "low",
        "Gender": "M",
        "Discount_offered": 44,
        "Weight_in_gms": 1233
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert response.json()["prediction"] in ["On-Time", "Delayed"]
