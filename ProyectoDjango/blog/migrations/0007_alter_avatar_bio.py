# Generated by Django 4.2.5 on 2023-10-09 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_avatar_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='bio',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
