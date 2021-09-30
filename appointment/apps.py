from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AppointmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appointment'
    verbose_name = _("Qabullar ma'lumotlari")
