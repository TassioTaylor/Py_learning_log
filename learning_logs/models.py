from django.db import models
from django.utils import timezone


# Create your models here.

class Topic(models.Model):
    entry_set = None
    objects = None
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text


class Entry(models.Model):
    objects = None
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'entries'

        def __str__(self):
            return self.text[:50] + "..."
