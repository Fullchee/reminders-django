# Generated by Django 3.2.3 on 2021-07-13 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_link_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.URLField(max_length=1000, null=True, unique=True),
        ),
    ]
