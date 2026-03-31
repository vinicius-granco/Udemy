from django.db import models
from machines.models import Machine

# Create your models here.
class Sensor(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name="sensors")
    type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.type} sensor on {self.machine.name}"