from django.contrib import admin
from zapisnici.models import Zapisnik

from django.db import models
from tinymce.widgets import TinyMCE

class ZapisnikAdmin(admin.ModelAdmin):
    fields = ['zap_date', 'zap_sadrzaj', 'prisutni','mail_notifikacija']
    list_display = ('zap_date', 'zap_sadrzaj','mail_notifikacija')

    formfield_overrides = {
            models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }

admin.site.register(Zapisnik, ZapisnikAdmin)

