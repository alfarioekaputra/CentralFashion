from django_filters import FilterSet, ModelChoiceFilter, CharFilter

from master.suppliers.models import Supplier, Termin

class SupplierFilter(FilterSet):
    termin = ModelChoiceFilter(
        queryset=Termin.objects.all(),
        label="TERMIN PEMBAYARAN"
    )
    code = CharFilter(label="KODE SUPPLIER", lookup_expr='icontains')
    name = CharFilter(label="NAMA SUPPLIER", lookup_expr='icontains')
    class Meta:
        model = Supplier
        fields = ['code', 'name','termin']