from django.db import models

from core.models import TimeStampedModel, SoftDelete

# Create your models here.
class Reference(TimeStampedModel, SoftDelete):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)

    class Meta:
      db_table = "references"

    def __str__(self):
        return self.name

class ReferenceDetail(TimeStampedModel, SoftDelete):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    order = models.IntegerField(default=0)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    status = models.BooleanField(default=True)
    reference = models.ForeignKey(Reference, on_delete=models.CASCADE)

    class Meta:
      db_table = "reference_details"

    def __str__(self):
        return self.name