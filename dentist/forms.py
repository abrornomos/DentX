from django import forms
from django.forms import ModelForm
from .models import *
from django.utils.translation import ugettext_lazy as _


class dentistForm(forms.Form):
    first_name = forms.CharField(
        label=_("Ismingiz")
        widget=forms.TextInput(
            attrs={'class': 'form-control',
            'placeholder:_("Ismingiz")'}
        ),
        max_length=150,
        localize=True
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            label=_("Familiya"),
            attrs={'class': 'form-control',
            "placeholder:_(""Familiyangiz)"}
        ),
        max_length=150,
        localize=True
    )
    number = forms.CharField(
        widget=forms.TextInput(
            label=_("Telefon nomer"),
            attrs={'class': 'form-control',
            "placeholder:_('Telefon nomeringiz')"}
        ),
        max_length=25,
        localize=True
    )
    adress = forms.CharField(
        widget=forms.TextInput(
            label=_('Manzil'),
            attrs={'class': 'form-control',
        "placeholder:_('Manzilingiz')"}
        ),
        max_length=150,
        localize=True
    )
    language = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
            "placeholder:_('Tilni Tanlang')"}
        ),
        max_length=50ы,
        localize=True

    )
    birthay = forms.DateTimeField()
    image = forms.ImageField()
    specialty = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
            "placeholder:_(Mutaxasisligi)"}
        ),
        max_length=150,
        localize=True

    )
    experience = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',}
        ),
        max_length=150,
        localize=True

    )
    work_begin = forms.DateTimeField()
    work_end = forms.DateTimeField()
    clinic = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        ),
        max_length=150,
        localize=True

    )



