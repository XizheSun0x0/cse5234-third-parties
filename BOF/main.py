from bofpay import PaymentInfo,PaymentConfirmation
from fastapi import FastAPI, HTTPException, status
from mangum import Mangum
import uuid

app = FastAPI()
handler = Mangum(app)
@app.get("/")
async def read_root():
    return {"Hello": "BOF Users"}

@app.get("/didi")
async def test():
    return {"message":"Call Success!"}

@app.post("/payment-processing/credit-card-processing/payment", response_model=PaymentConfirmation)
async def process_cc_transaction(payment_info: PaymentInfo):
    confirmation_number = f"BOF-{uuid.uuid4()}"
    return PaymentConfirmation(confirmation_number=confirmation_number)