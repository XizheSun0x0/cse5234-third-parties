from typing import Optional
from pydantic import BaseModel, EmailStr


class ShipmentMessage(BaseModel):
    message: str

class ShipmentInfo(BaseModel):
    recipient_name: str
    postal_address: str
    email: Optional[str] = None
    number_of_items: Optional[int] = None
    total_weight: Optional[float] = None
    total_dimension: Optional[str] = None
    business_entity_name: str
    entity_account_number: str
