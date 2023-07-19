# Generated by Django 4.2.3 on 2023-07-19 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("lists", "0003_list"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="list",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="lists.list",
            ),
        ),
    ]