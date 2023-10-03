from django.db import models


class OperationalUnit(models.Model):
    name = models.CharField(max_length=200)


class Oilfield(models.Model):
    name = models.CharField(max_length=200)
    operational_unit = models.ForeignKey(OperationalUnit, on_delete=models.CASCADE)


class Well(models.Model):
    name = models.CharField(max_length=200)
    oilfield = models.ForeignKey(Oilfield, on_delete=models.CASCADE)
