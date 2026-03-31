from django.db import models
from companies.models import Company

# Create your models here.
class Machine(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='machines')
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name