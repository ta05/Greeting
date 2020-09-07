from django.db import models

# Create your models here.
class Message(models.Model):
    message_text = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.message_text
