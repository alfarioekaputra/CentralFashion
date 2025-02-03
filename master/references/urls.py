from django.urls import path

from .views import add_detail_form, index, create, detail, export_to_excel, load_filter_form, clear_filter, remove_detail_form

urlpatterns = [
  path("", index, name="reference_index"),
  path("create", create, name="reference_create"),
  path("export-excel/", export_to_excel, name="reference_export_excel"),
  path('load-filter-form/', load_filter_form, name='reference_load_filter_form'),
  path('clear-filter/', clear_filter, name='reference_clear_filter'),
  path('detail/<int:pk>/', detail, name='reference_detail'),
  path('add-detail-form/<int:reference_id>/', add_detail_form, name='reference_add_detail_form'),
  path('remove-detail-form/<input_id>/', remove_detail_form, name='reference_remove_detail_form'),
]