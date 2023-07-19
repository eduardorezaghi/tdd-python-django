from django.db import models


class Item(models.Model):
    """Model definition for Item."""

    text = models.TextField(default="")
    list = models.ForeignKey(
        "List", default=None, null=True, on_delete=models.CASCADE
    )


class List(models.Model):
    """Model definition for List."""
    pass
