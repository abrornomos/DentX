from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Dentist2patient(models.Model):
    sender = models.ForeignKey("dentist.User", verbose_name=_("Tish shifokori"), on_delete=models.CASCADE, related_name="dentist_sender")
    recipient = models.ForeignKey("patient.User", verbose_name=_("Bemor"), on_delete=models.CASCADE, related_name="patient_recipient")
    message = models.TextField(_("Tish holatlari"))
    datetime = models.DateTimeField(_("Xabar jo'natilgan vaqt"), auto_now=False, auto_now_add=True)
    is_read = models.BooleanField(_("O'qilganmi?"))

    class Meta:
        verbose_name = _("D2P Xabar")
        verbose_name_plural = _("D2P Xabarlar")

    def __str__(self):
        return f"{self.sender.__str__()} - {self.datetime}"


class Patient2dentist(models.Model):
    sender = models.ForeignKey("patient.User", verbose_name=_("Bemor"), on_delete=models.CASCADE, related_name="patient_sender")
    recipient = models.ForeignKey("dentist.User", verbose_name=_("Tish shifokori"), on_delete=models.CASCADE, related_name="dentist_recipient")
    message = models.TextField(_("Tish holatlari"))
    datetime = models.DateTimeField(_("Xabar jo'natilgan vaqt"), auto_now=False, auto_now_add=True)
    is_read = models.BooleanField(_("O'qilganmi?"))

    class Meta:
        verbose_name = _("P2D Xabar")
        verbose_name_plural = _("P2D Xabarlar")

    def __str__(self):
        return f"{self.sender.__str__()} - {self.datetime}"
