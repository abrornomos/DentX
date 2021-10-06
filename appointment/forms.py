from django import forms
from django.utils.translation import ugettext_lazy as _
from .var import CHOICES
from django.forms import DateTimeField



class AppointmentForm(forms.Form):
    name = forms.CharField(
        label=_("bemor"),
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
        label=_("number"),
        widget=forms.TextInput(
            attrs={
                'placeholder': _("Telefon nomer")


            }
        ),
        max_length=30,
        localize=True
    )
    birth_day = forms.CharField(
        label=_('date'),
        widget=forms.DateTimeField()
    )
    rod = forms.CharField(label=('Jins'),widget=forms.ChoiceField(widget=forms.RadioSelect(), choices=CHOICES))
    adress = forms.CharField(
        label=('Manzil'),
        widget = forms.TextInput(
            attrs={ 'class': "wid",
                'placeholder': _("Manzilni kiriting")

            }
        ),
        max_length = 150,
        localize = True
    )
    service=forms.CharField(
        widget=forms.TextInput(
             attrs={"id":'service'}
        ),
        max_length =100,
        localize=True
    )
    begin = forms.CharField(
        widget=forms.DateInput(attrs={
               " id": 'begin'

            })
    )
    end = forms.CharField(
        widget=forms.DateInput(attrs={
                'class': 'end'

            }

        )
    )
    message = forms.CharField(widget=forms.Textarea(attrs={
                'id': 'commit'

            }))

