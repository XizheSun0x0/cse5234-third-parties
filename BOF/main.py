from bofpay import PaymentInfo,PaymentConfirmation
from fastapi import FastAPI, HTTPException, status
import uvicorn

import uuid

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "BOF Users"}

@app.get("/didi")
async def test():
    return {"message":"Call Success!"}

@app.post("/payment-processing/credit-card-processing/payment", response_model=PaymentConfirmation)
async def process_cc_transaction(payment_info: PaymentInfo):
    confirmation_number = f"BOF-{uuid.uuid4()}"
    return PaymentConfirmation(confirmation_number=confirmation_number)

if __name__ == "__main__":
    uvicorn.run(app,port=5001)