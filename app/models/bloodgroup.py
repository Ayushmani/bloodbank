from django.db import models

class BloodGroup(models.Model):
    name = models.CharField("Name", max_length = 3)
    description = models.CharField("Description", max_length = 250)

    class Meta:
        app_label = "app"
        db_table = "bloodgroups"

    def __unicode__(self):
        return self.name
