from django_tables2 import tables
from django_tables2.export.views import ExportMixin

from master.suppliers.models import Supplier

class SupplierTable(tables.Table):
  code = tables.Column(verbose_name="KODE SUPPLIER")
  name = tables.Column(verbose_name="NAMA SUPPLIER")
  termin = tables.Column(verbose_name="TERMIN PEMBAYARAN")

  class Meta:
    model = Supplier
    template_name = "django_tables2/bootstrap5-responsive.html"  # Gunakan template Bootstrap
    fields = ("code", "name", "termin")  # Tentukan kolom yang akan ditampilkan
    attrs = {"class": "table"}