# Generated by Django 4.1.5 on 2023-09-20 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fms", "0009_alter_newfile_created_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newfile",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
