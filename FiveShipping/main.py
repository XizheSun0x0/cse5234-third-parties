from fastapi import FastAPI, HTTPException
from models import ShipmentInfo, ShipmentMessage
from fastapi import FastAPI, HTTPException, status
from mangum import Mangum
import uuid

app = FastAPI()
handler = Mangum(app)

@app.get("/")
def read_root():
    return {"Hello": "5PS Users"}

@app.post("/shipment-processing/initiation")
async def initiate_shipping(shipment_message: ShipmentMessage):
    return{"message": "Please send with shipment details"}

@app.post("/shipment-processing/shipment")
async def create_shipping(shipment_info: ShipmentInfo):
    # Logic to process shipping
    label_number = f"5PS-{uuid.uuid4()}"
    return {"label_number": label_number}