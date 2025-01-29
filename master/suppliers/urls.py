from django.urls import path

from .views import index, create, export_to_excel, load_filter_form, clear_filter

urlpatterns = [
  path("", index, name="supplier_index"),
  path("/create", create, name="supplier_create"),
  path("export-excel/", export_to_excel, name="supplier_export_excel"),
  path('supplier/load-filter-form/', load_filter_form, name='supplier_load_filter_form'),
  path('supplier/clear-filter/', clear_filter, name='supplier_clear_filter'),
]