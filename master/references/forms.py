from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Row, Column
from django.forms import inlineformset_factory

from master.references.models import Reference, ReferenceDetail

class ReferenceForm(forms.ModelForm):
  class Meta:
    model = Reference
    
    fields = ['name','description']

    labels = {
      'name': 'NAMA MASTER',
      'description': 'KETERANGAN',
    }
    
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_method = 'post'
    self.helper.form_action = 'reference_create'
    
    self.helper.layout = Layout(
        Column('name'),
        Column('description'),
        Submit('submit', 'SIMPAN')
    )

class ReferenceDetailForm(forms.ModelForm):
  class Meta:
    model = ReferenceDetail
    fields = ['id', 'name', 'description', 'status']

    labels = {
      'name': 'NILAI',
      'description': 'KETERANGAN',
      'status': 'STATUS',
    }

    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'description': forms.TextInput(attrs={'class': 'form-control'}),
      'status': forms.CheckboxInput(attrs={'class': 'form-control'}),
    }

ReferenceDetailFormSet = inlineformset_factory(
  Reference, 
  ReferenceDetail, 
  form=ReferenceDetailForm, 
  extra=1, 
  can_delete=True
)