# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime
from datetime import timedelta
import jwt, json
import os

class Admins(models.Model):
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'admins'

    is_authenticated = False

    def generate_jwt_token(self):
        dt = datetime.now() + timedelta(minutes = 3)
        token = jwt.encode({
            'id':self.pk,
            'email':self.email,
            'exp':dt
        },os.environ['SECRETKEY'])
        return token

    @property
    def token(self):
        return self.generate_jwt_token()


class Customers(models.Model):
    identificationnumber = models.CharField(db_column='identificationNumber', max_length=30)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=60)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=60)  # Field name made lowercase.
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'customers'

    is_authenticated = False

    def generate_jwt_token(self):
        dt = datetime.now() + timedelta(minutes = 3)
        token = jwt.encode({
            'id':self.pk,
            'email':self.email,
            'exp':dt
        },os.environ['SECRETKEY'])
        return token

    @property
    def token(self):
        return self.generate_jwt_token()

class Mechanics(models.Model):
    identificationnumber = models.CharField(db_column='identificationNumber', max_length=30)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=60)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=60)  # Field name made lowercase.
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=64)
    socialsecuritynumber = models.CharField(db_column='socialSecurityNumber', max_length=11)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mechanics'

    is_authenticated = False

    def generate_jwt_token(self):
        dt = datetime.now() + timedelta(minutes = 3)
        token = jwt.encode({
            'id':self.pk,
            'email':self.email,
            'exp':dt
        },os.environ['SECRETKEY'])
        return token

    @property
    def token(self):
        return self.generate_jwt_token()

class Receptionist(models.Model):
    identificationnumber = models.CharField(db_column='identificationNumber', max_length=30)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=60)  # Field name made lowercase.
    lastname = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=64)
    socialsecuritynumber = models.CharField(db_column='socialSecurityNumber', max_length=11)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'receptionist'

    is_authenticated = False

    def generate_jwt_token(self):
        dt = datetime.now() + timedelta(minutes = 3)
        token = jwt.encode({
            'id':self.pk,
            'email':self.email,
            'exp':dt
        },os.environ['SECRETKEY'])
        return token

    @property
    def token(self):
        return self.generate_jwt_token()
