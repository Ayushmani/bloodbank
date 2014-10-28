from django.db import models
from bloodgroup import BloodGroup

class Individual(models.Model):
    bloodgroup = models.ForeignKey(BloodGroup)
    name = models.CharField("Name", max_length = 80)
    phone_number = models.CharField("Phone number", max_length = 13)

    class Meta:
        app_label = "app"
        db_table = "individuals"

    def __unicode__(self):
        return self.name
