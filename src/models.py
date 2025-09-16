from pydantic import BaseModel
from typing import List, Optional

class LoadSearchRequest(BaseModel):
    origin_city: str
    origin_state: str
    destination_city: Optional[str] = None
    destination_state: Optional[str] = None
    equipment_type: str
    pickup_datetime: Optional[str] = None

class LoadSearchResponse(BaseModel):
    loads: List[dict]
    load_count: int
    selected_load_id: str
    initial_rate: float
