from pydantic import BaseModel


class PaymentInfo(BaseModel):
    business_entity_name: str
    business_entity_account: str
    amount:str
    customer_name: str
    credit_card_number: str
    expiration_date: str
    cvv_code: str

class PaymentConfirmation(BaseModel):
    confirmation_number: str
