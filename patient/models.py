from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(models.Model):
    user = models.OneToOneField("auth.User", verbose_name=_("Bemor"), on_delete=models.CASCADE, related_name="patient_user")
    phone_number = models.CharField(_("Telefon raqami"), max_length=50)
    gender = models.ForeignKey("baseapp.Gender", verbose_name=_("Jins"), on_delete=models.CASCADE, related_name="patient_gender")
    address = models.CharField(_("Manzil"), max_length=255)
    birthday = models.DateField(_("Tug'ilgan sanasi"), auto_now=False, auto_now_add=False)
    image = models.ImageField(_("Rasmi"), upload_to="patients/photos/")
    language = models.ForeignKey("baseapp.Language", verbose_name=_("Tili"), on_delete=models.CASCADE, related_name="patient_language")

    class Meta:
        verbose_name = _("Bemor")
        verbose_name_plural = _("Bemorlar")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Tooth(models.Model):
    code = models.IntegerField(_("Tish raqami"))
    status = models.ForeignKey("patient.Tooth_status", verbose_name=_("Tish holati"), on_delete=models.CASCADE, related_name="patient_tooth_status")
    patient = models.ForeignKey("patient.User", verbose_name=_("Bemor"), on_delete=models.CASCADE, related_name="patient_tooth")

    class Meta:
        verbose_name = _("Tish")
        verbose_name_plural = _("Tishlar")

    def __str__(self):
        return f"{self.code}-{_('tish')} - {self.status} ({self.user.first_name} {self.user.last_name})"


class Tooth_status(models.Model):
    name = models.CharField(_("Holat nomi"), max_length=100)
    prefix = models.CharField(_("Holat qo'shimchasi"), max_length=50)

    class Meta:
        verbose_name = _("Tish holati")
        verbose_name_plural = _("Tish holatlari")

    def __str__(self):
        return self.name


class Plan(models.Model):
    name = models.CharField(_("Ish nomi"), max_length=100)
    is_done = models.BooleanField(_("Qilinganligi"))
    patient = models.ForeignKey("patient.User", verbose_name=_("Bemor"), on_delete=models.CASCADE, related_name="patient_plan")

    class Meta:
        verbose_name = _("Qilingan ish")
        verbose_name_plural = _("Qilingan ishlar")

    def __str__(self):
        return f"{self.name} - {self.patient.__str__()}"


class Process_photo(models.Model):
    image = models.ImageField(_("Ish jarayonidagi rasm"), upload_to="patients/process_photos/")
    patient = models.ForeignKey("patient.User", verbose_name=_("Bemor"), on_delete=models.CASCADE, related_name="patient_process_photo")

    class Meta:
        verbose_name = _("Tish holati")
        verbose_name_plural = _("Tish holatlari")

    def __str__(self):
        return f"{self.image.name} - {self.patient.__str__()}"
