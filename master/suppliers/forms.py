from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Row, Column

from master.suppliers.models import Supplier

class SuppliersForm(forms.ModelForm):
  class Meta:
    model = Supplier
    
    fields = ['code','name', 'termin', 'address', 'phone', 'email']

    labels = {
      'code': 'KODE SUPPLIER',
      'name': 'NAMA SUPPLIER',
      'termin': 'TERMIN PEMBAYARAN',
      'address': 'ALAMAT',
      'phone': 'TELEPON',
      'email': 'EMAIL'
    }
    
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['code'].initial = Supplier.generate_next_code()
    self.helper = FormHelper()
    self.helper.form_method = 'post'
    self.helper.form_action = 'supplier_create'
    
    self.helper.layout = Layout(
        Row(
            Column(Field('code', css_class='bg-gray-700', readonly=True), css_class='form-group col-md-6 mb-0'),
            Column('name', css_class='form-group col-md-6 mb-0'),
            css_class='form-row'
        ),
        Row(
            Column('termin', css_class='form-group col-md-4 mb-0'),
            Column('phone', css_class='form-group col-md-4 mb-0'),
            Column('email', css_class='form-group col-md-4 mb-0'),
            css_class='form-row'
        ),
        Column('address'),
        Submit('submit', 'Simpan')
    )