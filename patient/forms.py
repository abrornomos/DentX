from django import forms
from django.forms import ModelForm
from .models import *
from django.utils.translation import ugettext_lazy as _


class UserForm(ModelForm):
    class Meta:
        model=patsent
        fields='__all__'

class patentForm(forms.Form):
    first_name = forms.CharField(
        label=_("Ismi"),
        widget=forms.TextInput(
            attrs={'class': 'form-control',
            "placeholder:_('Ismingiz')"}
        ),
        max_length=150,
        localize=True
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            label=_('Familiya'),
            attrs={'class': 'form-control',
             "placeholder:_('Familiyangiz')"}
        ),
        max_length=150,
        localize=True
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            label=_("Telefon nomer"),
            attrs={'class': 'form-control',
            "placeholder:_('Telefon nomeringiz')"}
        ),
        max_length=30,
        localize=True
    )
    birthay = forms.TimeField()
    adress = forms.CharField(
        widget=forms.TextInput(
            label=_('Manzil')
            attrs={'class': 'form-control',
            "placeholder:_('Manzilingiz')"}
        ),
        max_length=150,
        localize=True
    )
    image = forms.ImageField()
    language = forms.CharField(
        label=_('Til')
        widget=forms.TextInput(
            attrs={'class': 'form-control',
            "placeholder:_('Tilni tanlang')"}
        ),
        max_length=150,
        localize=True

    )


