from django.db import models
from tinymce.widgets import TinyMCE

from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

class Zapisnik(models.Model):
    zap_date = models.DateTimeField('datum zapisnika')
    zap_sadrzaj = models.TextField('sadrzaj zapisnika')
    prisutni = models.TextField('prisutni')
    mail_notifikacija = models.BooleanField(default=False)

    def __unicode__(self):
        return self.zap_sadrzaj

    class Meta:
        verbose_name_plural = "zapisnici"

    def save(self):
        if self.mail_notifikacija == True:

            plaintext = get_template('email.txt')
            htmltext = get_template('email.html')

            d = Context({ 'datum' : self.zap_date,
                'prisutni' : self.prisutni,
                'sadrzaj' : self.zap_sadrzaj })

            subject, from_email, to = 'Zapisnik sa sastanka', settings.EMAIL_HOST_USER, 'morrigan@kset.org'
            text_content = plaintext.render(d)
            html_content = htmltext.render(d)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            super(Zapisnik, self).save()
   
