# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Beta(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    friends = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beta'


class Futures(models.Model):
    date = models.DateField(primary_key=True)
    time = models.TimeField(blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    total_volume = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'futures'
