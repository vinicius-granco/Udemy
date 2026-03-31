from ninja import Schema
from datetime import datetime
from machines.schemas import MachineSchema
from typing import List

class CompanySchema(Schema):
    id: int
    name: str
    created_at: datetime
    machines: List[MachineSchema]