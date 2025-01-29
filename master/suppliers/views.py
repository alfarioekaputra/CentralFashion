from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.shortcuts import render
from django.urls import reverse
from django_tables2.config import RequestConfig
from django_tables2.export.export import TableExport

from master.suppliers.filters import SupplierFilter
from master.suppliers.forms import SuppliersForm
from master.suppliers.models import Supplier
from master.suppliers.tables import SupplierTable

# Create your views here.
def index(request):
    # Ambil semua data produk
    queryset = Supplier.objects.all()

    # Terapkan filter
    supplier_filter = SupplierFilter(request.GET, queryset=queryset)
    filtered_queryset = supplier_filter.qs

    table = SupplierTable(filtered_queryset)
    table.paginate(page=request.GET.get('page', 1), per_page=5)

    if request.headers.get('HX-Request') == 'true':
        # Jika request dari HTMX, kembalikan tabel dan form filter
        table_html = render_to_string('table.html', {'table': table}, request=request)
        filter_form_html = render_to_string('filter.html', {'filter': supplier_filter}, request=request)
        return HttpResponse(filter_form_html + table_html)
    else:
        # Jika request biasa, kembalikan seluruh halaman
        return render(request, 'index.html', {
            'table': table,
            'filter': supplier_filter,
        })

def export_to_excel(request):
    # Ambil queryset dan buat tabel
    queryset = Supplier.objects.all()
    table = SupplierTable(queryset)

    # Ekspor tabel ke format XLSX menggunakan Tablib
    export = TableExport("xlsx", table)
    
    # Generate response
    return export.response(f"data_export.xlsx")

def create(request):
    if request.method == 'POST':
        form = SuppliersForm(request.POST)

        if form.is_valid():
          supplier = form.save(commit=False) 
          supplier.code = Supplier.generate_next_code()
          supplier.save()
          return HttpResponseRedirect(reverse('supplier_index'))
    else:
        form = SuppliersForm()
    return render(request, 'create.html', {'form': form})

def load_filter_form(request):
    # Buat instance filter
    product_filter = SupplierFilter(request.GET)

    # Render form filter ke template
    filter_form_html = render_to_string('filter.html', {'filter': product_filter}, request=request)
    return HttpResponse(filter_form_html)

def clear_filter(request):
    # Buat instance filter tanpa parameter GET
    product_filter = SupplierFilter()

    # Render form filter kosong ke template
    filter_form_html = render_to_string('filter.html', {'filter': product_filter}, request=request)
    return HttpResponse(filter_form_html)

