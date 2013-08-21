from django.contrib import admin
from minutes.models import Minutes 

from django.db import models
from tinymce.widgets import TinyMCE

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.conf import settings

class MinutesAdmin(admin.ModelAdmin):
    fields = ['date', 'content', 'members_present', 'mail_notification']
    list_display = ('date', 'members_present', 'content')

    def save_model(self, request, obj, form, change):
        if obj.mail_notification== True:
            plaintext = get_template('email.txt')
            htmltext = get_template('email.html')
            d = Context({ 'date' : obj.date,
                'present_members' : obj.members_present,
                'content' : obj.content})

            subject, from_email, to = 'Zapisnik sastanka {}'.format(obj.date), settings.EMAIL_HOST_USER, settings.EMAIL_TO_ADDRESS 
            text_content = plaintext.render(d)
            html_content = htmltext.render(d)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

        super(MinutesAdmin, self).save_model(request, obj, form, change)


    formfield_overrides = {
            models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }

admin.site.register(Minutes, MinutesAdmin)

