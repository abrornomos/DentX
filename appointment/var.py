from django.utils.translation import ugettext_lazy as _


CHOICES = {
    'gender': [
        ('1', _("Erkak")),
        ('2', _("Ayol"))
    ],
    'duration': [
        ("15", _("15 daqiqa")),
        ("30", _("30 daqiqa")),
        ("45", _("45 daqiqa")),
        ("60", _("1 soat")),
    ]
}

MONTHS = [
    _("Yanvar"),
    _("Fevral"),
    _("Mart"),
    _("Aprel"),
    _("May"),
    _("Iyun"),
    _("Iyul"),
    _("Avgust"),
    _("Sentyabr"),
    _("Oktyabr"),
    _("Noyabr"),
    _("Dekabr"),
]

DAYS = [
    _("Dushanba"),
    _("Seshanba"),
    _("Chorshanba"),
    _("Payshanba"),
    _("Juma"),
    _("Shanba"),
    _("Yakshanba"),
]
