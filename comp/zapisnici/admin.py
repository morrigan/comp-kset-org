from django.contrib import admin
from zapisnici.models import Zapisnik

from django.db import models
from tinymce.widgets import TinyMCE

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.conf import settings

class ZapisnikAdmin(admin.ModelAdmin):
    fields = ['zap_date', 'zap_sadrzaj', 'prisutni', 'mail_notifikacija']
    list_display = ('zap_date', 'zap_sadrzaj', 'mail_notifikacija')

    def save_model(self, request, obj, form, change):
        if obj.mail_notifikacija == True:

            plaintext = get_template('email.txt')
            htmltext = get_template('email.html')

            d = Context({ 'datum' : obj.zap_date,
                'prisutni' : obj.prisutni,
                'sadrzaj' : obj.zap_sadrzaj })

            subject, from_email, to = 'Zapisnik sa sastanka', settings.EMAIL_HOST_USER, 'sendto@mail.com'
            text_content = plaintext.render(d)
            html_content = htmltext.render(d)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

        super(ZapisnikAdmin, self).save_model(request, obj, form, change)


    formfield_overrides = {
            models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }

admin.site.register(Zapisnik, ZapisnikAdmin)

