from django.db import models

# Create your models here.
class Followup(models.Model):
    followup_id = models.AutoField(primary_key=True)
    date_of_followup = models.DateField()
    response = models.CharField(max_length=100, blank=True)
    medium_used = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.response

class Lead(models.Model):
    lead_id = models.AutoField(primary_key=True)
    contact_person = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    address = models.CharField(max_length=100, blank=True)
    source = models.CharField(max_length=100, blank=True)
    current_stage = models.CharField(max_length=100, blank=True)
    #Followup fields
    followup_id = models.ManyToManyField(Followup)
