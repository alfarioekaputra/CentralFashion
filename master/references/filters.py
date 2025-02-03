from django_filters import FilterSet, ModelChoiceFilter, CharFilter

from master.references.models import Reference

class ReferenceFilter(FilterSet):
    name = CharFilter(label="NAMA MASTER", lookup_expr='icontains')
    description = CharFilter(label="KETERANGAN", lookup_expr='icontains')
    class Meta:
        model = Reference
        fields = ['name', 'description']