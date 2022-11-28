from django.db import models


class MyNotes(models.Model):
    # ID column mades by default

    title = models.CharField(max_length=200)

    # like CharField but with unlimited characters
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
