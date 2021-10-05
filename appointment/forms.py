from django import forms
from django.utils.translation import ugettext_lazy as _
from .var import CHOICES


class AppointmentForm(forms.Form):
    name = forms.CharField(
        label=_("Bemor"),
        widget=forms.TextInput(
            attrs={
                'class': "w-100 mb-3",
                'placeholder': _("Bemor FIOsi")
            }
        ),
        max_length=200,
        localize=True
    )
    phone_number = forms.CharField(
        label=_("Telefon nomer"),
        widget=forms.TextInput(
            attrs={
                'class': "w-100 mb-3",
                'placeholder': _("Telefon nomer")

            }
        ),
        max_length=30,
        localize=True
    )
    birth_year = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': "year_holder",
                'value': datetime.today().year
            }
        ),
        localize=True
    )
    birth_month = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': "month_holder",
                'value': MONTHS[datetime.today().month - 1]
            }
        ),
        localize=True
    )
    birth_day = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': "day_holder",
                'value': datetime.today().day
            }
        ),
        localize=True
    )
    rod = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    adress = forms.CharField(
        widget = forms.TextInput(
            attrs={ 'class': "w-100 mb-3",
                'placeholder': _("Manzilni kiriting")

            }
        ),
        max_length = 150,
        localize = True
    )
    service=forms.CharField(
        widget=forms.TextInput(
             'class': "w-100 mb-3",
        ),
        max_length =100,
        localize=True
    )
    begin = forms.CharField(
        widget=forms.DateInput(attrs={
                'class': 'form-control'

            })
    )
    end = forms.CharField(
        widget=forms.DateInput(attrs={
                'class': 'form-control'

            }

        )
    )
    message = forms.CharField(widget=forms.Textarea(attrs={
                'class': 'form-control'

            }))

