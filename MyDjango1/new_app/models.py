from __future__ import unicode_literals

from django.db import models

class paragraph(models.Model):
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Add_line1 = models.TextField()
    Add_line2 = models.TextField()
    City = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    Zip = models.CharField(max_length=30)
    Email = models.CharField(max_length=20)
    Phone = models.CharField(max_length=30)

    def __str__(self):
        return self.Last_name
