from ninja import NinjaAPI
from companies.models import Company
from machines.models import Machine
from companies.schemas import CompanySchema
from machines.schemas import MachineSchema
from typing import List
from django.db.models import Prefetch

api = NinjaAPI()

@api.get("/companies", response=List[CompanySchema])
def list_companies(request):
    return Company.objects.all()

@api.get("/companies/{company_id}", response=CompanySchema)
def company_detail(request, company_id: int):
    return (
        Company.objects
        .prefetch_related(
            Prefetch(
                "machines",
                queryset=Machine.objects.prefetch_related("sensors")
            )
        )
        .get(id=company_id)
    )

@api.get("/machines", response=List[MachineSchema])
def list_machines(request):
    return Machine.objects.all()