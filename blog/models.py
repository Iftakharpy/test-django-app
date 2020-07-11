from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateField()

    def summary(self, num_words=20):
        words = self.description.split()
        summery = ' '.join(words[:num_words])
        if len(words)>num_words:
            summery+='...'
        return summery

    def __str__(self):
        return f'{self.id} - {self.title}'