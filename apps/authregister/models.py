# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admins(models.Model):
    email = models.CharField(max_length=60)
    password = models.TextField()

    class Meta:
        managed = False
        db_table = 'admins'

class Customers(models.Model):
    identificationnumber = models.CharField(db_column='identificationNumber', max_length=30)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=60)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=60)  # Field name made lowercase.
    email = models.CharField(max_length=60)
    password = models.TextField()

    class Meta:
        managed = False
        db_table = 'customers'


class Mechanics(models.Model):
    id = models.IntegerField(primary_key=True)
    identificationnumber = models.CharField(db_column='identificationNumber', max_length=30)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=60)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=60)  # Field name made lowercase.
    email = models.CharField(max_length=60)
    password = models.TextField()

    class Meta:
        managed = False
        db_table = 'mechanics'

class Receptionist(models.Model):
    identificationnumber = models.CharField(db_column='identificationNumber', max_length=30)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=60)  # Field name made lowercase.
    apellido = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    password = models.TextField()

    class Meta:
        managed = False
        db_table = 'receptionist'
