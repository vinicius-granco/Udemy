from ninja import Schema
from datetime import datetime
from sensors.schemas import SensorSchema
from typing import List

class MachineSchema(Schema):
    id: int
    name: str
    status: str
    created_at: datetime
    company_id: int
    sensors: List[SensorSchema]