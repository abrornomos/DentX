from django import forms
from django.utils.translation import ugettext_lazy as _
from .var import CHOICES


class AppointmentForm(forms.Form):
    name = forms.CharField(
        label=_("Bemor"),
        widget=forms.TextInput(
            attrs={
                'class': "w-100 mb-3",
                'placeholder': _("Bemor FIOsi"),
            }
        ),
        localize=True
    )
    phone_number = forms.CharField(
        label=_("Telefon raqami"),
        widget=forms.TextInput(
            attrs={
                'class': "wid",
                'placeholder': _("+9989XXXXXXXX"),
            }
        ),
        localize=True
    )
    birthday = forms.DateField(
        label=_("Tugilgan sana"),
        widget=forms.DateInput(
            attrs={
                'class': "wid",
                'type': "date",
            }
        ),
        localize=True
    )
    gender = forms.CharField(
        label=_("Jins"),
        widget=forms.RadioSelect(
            attrs={
                'class': "m-1",
            },
            choices=CHOICES['gender']
        )
    )
    address = forms.CharField(
        label=_("Manzil"),
        widget=forms.TextInput(
            attrs={
                'class': "wid",
                'placeholder': _("Manzilni kiriting"),
            }
        ),
        localize=True
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

