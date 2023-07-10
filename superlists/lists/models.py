from django.db import models

class Item(models.Model):
    """Model definition for Item.
    """
    text = models.TextField(default="")