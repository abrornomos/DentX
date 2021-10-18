from django.db import models
from django.utils.translation import ugettext_lazy as _


class Clinic(models.Model):
    name = models.CharField(_("Nomi"), max_length=100)
    region = models.ForeignKey("baseapp.Region", verbose_name=_("Hudud"), on_delete=models.CASCADE, related_name="clinic_region")
    address = models.CharField(_("Manzil"), max_length=255)
    orientir = models.CharField(_("Mo'ljal"), max_length=255, blank=True, null=True)
    latitude = models.FloatField(_("Kenglik"), blank=True, null=True)
    longitude = models.FloatField(_("Uzunlik"), blank=True, null=True)
    language = models.ForeignKey("baseapp.Language", verbose_name=_("Til"), on_delete=models.CASCADE, related_name="clinic_language")

    class Meta:
        verbose_name = _("Shifoxona")
        verbose_name_plural = _("Shifoxonalar")

    def __str__(self):
        return self.name


class User(models.Model):
    user = models.ForeignKey("auth.User", verbose_name=_("Tish shifokori"), on_delete=models.CASCADE, related_name="dentist_user")
    phone_number = models.CharField(_("Telefon raqami"), max_length=100)
    gender = models.ForeignKey("baseapp.Gender", verbose_name=_("Jins"), on_delete=models.CASCADE, related_name="dentist_gender")
    birthday = models.DateField(_("Tug'ilgan sanasi"), auto_now=False, auto_now_add=False)
    image = models.ImageField(_("Rasmi"), upload_to="dentists/photos/")
    language = models.ForeignKey("baseapp.Language", verbose_name=_("Tili"), on_delete=models.CASCADE, related_name="dentist_gender")
    speciality = models.CharField(_("Soha"), max_length=500)
    experience = models.IntegerField(_("Tajriba"))
    worktime_begin = models.TimeField(_("Ish vaqti boshlanishi"), auto_now=False, auto_now_add=False)
    worktime_end = models.TimeField(_("Ish vaqti tugashi"), auto_now=False, auto_now_add=False)
    is_fullday = models.BooleanField(_("24 soat rejimi"))
    slug = models.CharField(_("Slug"), max_length=255, default="1")
    clinic = models.ForeignKey("dentist.Clinic", verbose_name=_("Shifoxona"), on_delete=models.CASCADE, related_name="dentist_clinic")

    class Meta:
        verbose_name = _("Tish shifokori")
        verbose_name_plural = _("Tish shifokorlari")

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name}"


class Service(models.Model):

    name = models.CharField(_("FISh"), max_length=100)
    duration = models.TimeField(_("Xizmat davomiyligi"), auto_now=False, auto_now_add=False)
    price = models.IntegerField(_("Xizmat narxi"))
    dentist = models.ForeignKey("dentist.User", verbose_name=_("Tish shifokori"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Xizmat")
        verbose_name_plural = _("Xizmatlar")

    def __str__(self):
        return self.name


class Cabinet_Image(models.Model):

    image = models.ImageField(_("Rasm"), upload_to="dentists/cabinet_photos/")
    dentist = models.ForeignKey("dentist.User", verbose_name=_("Tish shifokori"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Kabinet rasmi")
        verbose_name_plural = _("Kabinet rasmlari")

    def __str__(self):
        return self.image


# class service(models.Model):
#     name = models.CharField(max_length=200, null=True)
#     price = models.FloatField(default=0)
#     duration = models.IntegerField()
#     dentist = models.ForeignKey(user, on_delete=models.CASCADE)


# class cabinet_photo(models.Model):
#     image = models.ImageField()
#     dentist = models.ForeignKey(user, on_delete=models.CASCADE)
