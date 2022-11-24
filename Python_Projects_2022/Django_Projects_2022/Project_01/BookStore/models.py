from django.db import models


class AvailableBooks(models.Model):
    book_code = models.IntegerField()
    book_name = models.CharField(max_length=200)
    copies_number = models.PositiveSmallIntegerField()
    book_describtion = models.TextField()
    book_price = models.FloatField()
    book_availability = models.BooleanField()
