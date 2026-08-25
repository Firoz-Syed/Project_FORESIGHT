from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

app = FastAPI(title="FORESIGHT API")

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "models",
    "final_random_forest.pkl"
)

model = joblib.load(MODEL_PATH)


class PredictionInput(BaseModel):
    unit_price: float
    promo_flag: int
    unit_cost: float
    list_price: float
    week: int
    month: int
    is_holiday: int
    day: int
    day_of_week: int
    quarter: int
    year: int
    on_hand_units: float
    on_order_units: float
    lead_time_days: float
    reorder_point: float


@app.get("/")
def home():
    return {"message": "FORESIGHT API is running"}


@app.post("/predict")
def predict(data: PredictionInput):
    features = [[
        data.unit_price,
        data.promo_flag,
        data.unit_cost,
        data.list_price,
        data.week,
        data.month,
        data.is_holiday,
        data.day,
        data.day_of_week,
        data.quarter,
        data.year,
        data.on_hand_units,
        data.on_order_units,
        data.lead_time_days,
        data.reorder_point
    ]]

    prediction = model.predict(features)

    return {
        "predicted_units_sold": float(prediction[0])
    }