from django.db import models


class Zapisnik(models.Model):
    zap_date = models.DateTimeField('datum zapisnika')
    zap_sadrzaj = models.TextField('sadrzaj zapisnika')
    prisutni = models.CharField(max_length=200)

    def __unicode__(self):
        return self.zap_sadrzaj # Promijeniti u nesto pametnije

