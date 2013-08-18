from django.contrib import admin
from zapisnici.models import Zapisnik

from django.db import models
from tinymce.widgets import TinyMCE

from django.core.mail import send_mail
from django.conf import settings

class ZapisnikAdmin(admin.ModelAdmin):
    fields = ['zap_date', 'zap_sadrzaj', 'prisutni', 'mail_notifikacija']
    list_display = ('zap_date', 'zap_sadrzaj', 'mail_notifikacija')

    def save_model(self, request, obj, form, change):
        if obj.mail_notifikacija == True:
            send_mail('Zapisnik sa sastanka', obj.zap_sadrzaj, settings.EMAIL_HOST_USER, ['sendto@mail.com'])
       
        super(ZapisnikAdmin, self).save_model(request, obj, form, change)


    formfield_overrides = {
            models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }

admin.site.register(Zapisnik, ZapisnikAdmin)

