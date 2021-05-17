from django.db import models


# Create your models here.
class User_table(models.Model):
    brand = models.CharField(max_length=70)
    invamt = models.IntegerField()
    invdate = models.DateField(null=True, blank=True)
    cltnamt = models.IntegerField()
    cltndate = models.DateField(null=True, blank=True)
    customer = models.CharField(max_length=70)
    customercode = models.CharField(max_length=70)
    collectedby = models.CharField(max_length=70)
    paymentmode = models.CharField(max_length=70)
    cheque = models.IntegerField()
    bank = models.CharField(max_length=70)
    duedate = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=70, default='Pending')
    doptdate = models.DateField(null=True, blank=True)
    utrno = models.IntegerField()
    bksc = models.IntegerField()


