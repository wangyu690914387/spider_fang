from django.db import models

class City(models.Model):
    city = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'


class Home(models.Model):
    home_type = models.CharField(max_length=255, blank=True, null=True)
    beauty = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'home'


class Img(models.Model):
    img = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'img'


class Info(models.Model):
    cid = models.ForeignKey(City, models.DO_NOTHING, db_column='cid', blank=True, null=True)
    master = models.CharField(max_length=255, blank=True, null=True)
    master_tel = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    size_type = models.CharField(max_length=255, blank=True, null=True)
    use_type = models.CharField(max_length=255, blank=True, null=True)
    header = models.CharField(max_length=255, blank=True, null=True)
    addr = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    img = models.ForeignKey(Img, models.DO_NOTHING, blank=True, null=True)
    hid = models.ForeignKey(Home, models.DO_NOTHING, db_column='hid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'info'
