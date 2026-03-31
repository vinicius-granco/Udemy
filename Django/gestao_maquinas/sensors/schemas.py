from ninja import Schema
from datetime import datetime

class SensorSchema(Schema):
    id: int
    type: str
    created_at: datetime
    machine_id: int