from django.db import models

# Create your models here.
class Table(models.Model):
    api_well_number = models.AutoField(db_column='API WELL  NUMBER',primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    oil = models.IntegerField(db_column='OIL', blank=True, null=True)  # Field name made lowercase.
    gas = models.IntegerField(db_column='GAS', blank=True, null=True)  # Field name made lowercase.
    brine = models.IntegerField(db_column='BRINE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'table'