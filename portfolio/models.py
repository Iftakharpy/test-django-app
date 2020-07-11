from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return f'{self.id} - {self.title}'