from __future__ import unicode_literals

from django.db import models

# Create your models here.




class Note(models.Model):
    owner = models.ForeignKey('auth.User', related_name='text', on_delete=models.CASCADE)
    text = models.CharField(max_length=500, unique=False, default="Enter text...")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return(self.text + '  id: ' + str(self.id))

    def save(self, *args, **kwargs):

        super(Note, self).save(*args, **kwargs)



