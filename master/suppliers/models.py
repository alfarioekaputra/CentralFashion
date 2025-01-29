
from django.db import models
from django.db.models import Max
from auditlog.registry import auditlog

from core.models import TimeStampedModel, SoftDelete

class Termin(TimeStampedModel, SoftDelete):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=100, null=True)
  time_period = models.IntegerField()

  def __str__(self):
    return self.name
class Supplier(TimeStampedModel, SoftDelete):
  code = models.CharField(max_length=10)
  name = models.CharField(max_length=100)
  address = models.TextField(null=True)
  phone = models.CharField(max_length=15, null=True)
  email = models.EmailField(null=True)
  termin = models.ForeignKey(Termin, on_delete=models.DO_NOTHING)

  class Meta:
    ordering = ['code']

  def __str__(self):
    return self.name

  @classmethod
  def generate_next_code(cls):
    # Get the maximum existing code
    last_code = cls.objects.aggregate(Max('code'))['code__max']
    
    if not last_code:
        # If no codes exist, start with S-00001
        return 'S-00001'
    
    # Extract the numeric part and increment
    prefix = 'S-'
    current_number = int(last_code.split('-')[1])
    next_number = current_number + 1
    
    # Format the new code with leading zeros
    return f'{prefix}{next_number:05d}'
  
auditlog.register(Supplier)