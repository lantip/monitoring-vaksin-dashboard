from django.db import models


class Progress(models.Model):
    tanggal = models.CharField(max_length=100)
    data    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Progress Vaksin"
        verbose_name_plural = "Progress Vaksin"

    def __str__(self):
        return self.title

    def __unicode__(str):
        return  self.title

'''
class ProgressDetail(models.Model):
    title   = models.CharField(max_length=255)
    amount  = models.IntegerField(default=0)
    percentage = models.CharField(max_length=255, null=True, blank=True)
'''

class Province(models.Model):
    tanggal = models.DateTimeField()
    data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Progress Province"
        verbose_name_plural = "Progress Province"

    def __str__(self):
        return self.tahap 

    def __unicode__(self):
        return self.tahap


'''
class ProvinceDetail(mdoesl.Model):

    tahap = models.CharField(max_length=10, default="Tahap 1")
    kab_kota = models.CharField(max_length=255, null=True, blank=True)
    provinsi = models.CharField(max_length=255, null=True, blank=True)
    total = models.IntegerField(default=0)
    percentage = models.CharField(max_length=255, null=True, blank=True)
'''