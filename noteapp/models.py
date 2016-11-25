from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Note(models.Model):
    text = models.CharField(max_length=500, unique=False, default="Enter text...")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return(self.text + '  id: ' + str(self.id))

