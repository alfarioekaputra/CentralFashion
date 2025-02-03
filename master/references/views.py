from django.forms import formset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django_tables2.export.export import TableExport

from master.references.filters import ReferenceFilter
from master.references.forms import ReferenceForm, ReferenceDetailFormSet
from master.references.models import Reference, ReferenceDetail
from master.references.tables import ReferenceTable

# Create your views here.
def index(request):
    # Ambil semua data produk
    queryset = Reference.objects.all()

    # Terapkan filter
    reference_filter = ReferenceFilter(request.GET, queryset=queryset)
    filtered_queryset = reference_filter.qs

    table = ReferenceTable(filtered_queryset)
    table.paginate(page=request.GET.get('page', 1), per_page=5)

    if request.headers.get('HX-Request') == 'true':
        # Jika request dari HTMX, kembalikan tabel dan form filter
        table_html = render_to_string('table.html', {'table': table}, request=request)
        filter_form_html = render_to_string('reference/filter.html', {'filter': reference_filter}, request=request)
        return HttpResponse(filter_form_html + table_html)
    else:
        # Jika request biasa, kembalikan seluruh halaman
        return render(request, 'reference/index.html', {
            'table': table,
            'filter': reference_filter,
        })

def export_to_excel(request):
    # Ambil queryset dan buat tabel
    queryset = Reference.objects.all()
    table = ReferenceTable(queryset)

    # Ekspor tabel ke format XLSX menggunakan Tablib
    export = TableExport("xlsx", table)
    
    # Generate response
    return export.response(f"data_export.xlsx")

def create(request):
    if request.method == 'POST':
        form = ReferenceForm(request.POST)

        if form.is_valid():
          form.save()
          return HttpResponseRedirect(reverse('reference_index'))
    else:
        form = ReferenceForm()
    return render(request, 'reference/create.html', {'form': form})

def detail(request, pk):
    reference = get_object_or_404(Reference, pk=pk)
    
    if request.method == 'POST':
        formset = ReferenceDetailFormSet(request.POST, instance=reference)
        print(request.POST)
        if formset.is_valid():
            print(formset)
            formset.save()
            return HttpResponseRedirect(reverse('reference_detail', args=[pk]))
        else:
            print(formset.errors)
    else:
      formset = ReferenceDetailFormSet(instance=reference)

    return render(request, 'reference/detail.html', {'formset': formset, 'reference': reference})

def add_detail_form(request, reference_id):
    reference = Reference.objects.get(id=reference_id)
    formset = ReferenceDetailFormSet(instance=reference)
    form = formset.empty_form
    # form_html = render_to_string('detail_row.html', {'form': form})
    form_html = render_to_string('reference/detail_form.html', {'form': formset.empty_form})
    return HttpResponse(form_html)

def remove_detail_form(request, input_id):
  if request.method == 'GET':
        # Ambil id dari data POST
        form_id = input_id
        
        if form_id:
            # Hapus instance jika ada
            instance = ReferenceDetail.objects.get(id=form_id)
            instance.delete()
        return HttpResponse('')  # Kembalikan respons kosong
  return HttpResponse('')

def manage_reference_detail(request, reference_id):
    reference = get_object_or_404(Reference, pk=reference_id)

    if request.method == 'POST':
        formset = ReferenceDetailFormSet(request.POST, instance=reference)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse('reference_detail', args=[reference_id]))
    else:
      formset = ReferenceDetailFormSet(instance=reference)

    return render(request, 'reference/manage_reference_detail.html', {'formset': formset, 'reference': reference})

def load_filter_form(request):
    # Buat instance filter
    product_filter = ReferenceFilter(request.GET)

    # Render form filter ke template
    filter_form_html = render_to_string('reference/filter.html', {'filter': product_filter}, request=request)
    return HttpResponse(filter_form_html)

def clear_filter(request):
    # Buat instance filter tanpa parameter GET
    product_filter = ReferenceFilter()

    # Render form filter kosong ke template
    filter_form_html = render_to_string('reference/filter.html', {'filter': product_filter}, request=request)
    return HttpResponse(filter_form_html)

