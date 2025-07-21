from django.db import models
from django import forms

# Create your models here.
class Fornecedor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.name
    

class FornecedorForm(forms.ModelForm):
    class Meta:
        model=Fornecedor
        fields = ['name', 'email']

    name = forms.CharField(max_length=100)
    email = forms.EmailField()

def __init__(self, *args, **kwargs):
    super(FornecedorForm, self).__init__(*args, **kwargs)
    

