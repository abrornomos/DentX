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
    birthday = forms.CharField(
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
                'class': "w-100",
                'placeholder': _("Manzilni kiriting"),
            }
        ),
        localize=True
    )
    service = forms.CharField(
        label=_("Xizmat"),
        widget=forms.Select(
            attrs={
                'class': "wid"
            }
        ),
        localize=True
    )
    begin_day = forms.CharField(
        widget=forms.HiddenInput()
    )
    begin_time = forms.CharField(
        label=_("Boshlanish vaqti"),
        widget=forms.Select(
            attrs={
                'class': "wid"
            }
        )
    )
    duration = forms.CharField(
        label=_("Davomiyligi"),
        widget=forms.Select(
            attrs={
                'class': "wid"
            },
            choices=CHOICES['duration']
        )
    )
    comment = forms.CharField(
        label=_("Eslatma"),
        widget=forms.Textarea(
            attrs={
                'class': 'w-100'
            }
        ),
        required=False
    )

