from django_tables2 import tables, columns
from django_tables2.export.views import ExportMixin
from django_tables2.utils import A 

from master.references.models import Reference

class ReferenceTable(tables.Table):
  name = columns.LinkColumn("reference_detail", args=[A("pk")], verbose_name="NAMA MASTER")
  description = tables.Column(verbose_name="KETERANGAN")
  
  class Meta:
    model = Reference
    template_name = "django_tables2/bootstrap5-responsive.html"  # Gunakan template Bootstrap
    fields = ("name", "description")  # Tentukan kolom yang akan ditampilkan
    attrs = {"class": "table"}