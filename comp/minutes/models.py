from django.db import models

class Minutes(models.Model):
    date = models.DateTimeField('Meeting date')
    slug = models.SlugField()
    content = models.TextField('Minutes content')
    members_present = models.TextField('Present members')
    mail_notification = models.BooleanField(default=False)

    def __unicode__(self):
        return self.content[:64]

    class Meta:
        verbose_name_plural = "minutes"

