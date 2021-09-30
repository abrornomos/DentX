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
        )
    )
    phone_number

