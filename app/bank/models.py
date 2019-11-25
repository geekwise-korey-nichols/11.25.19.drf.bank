from django.db import models
import uuid
# Create your models here.

class Branch(models.Model):
    location_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    location_id = str(uuid.uuid4())

    def __str__(self):
        return f"{self.location_name} - {self.location}"

class Customer(models.Model):
    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE
    )
    customer_name = models.CharField(max_length=30)
    customer_email = models.EmailField(max_length=300)
    