from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=20)
    permalink  = models.CharField(max_length=20, unique=True)
    update_date = models.DateTimeField('last_updated')
    bodytext = models.TextField('Page Content', blank=True)


    def __str__(self):
        return self.title




