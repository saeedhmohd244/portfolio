# Generated by Django 5.0.7 on 2024-07-24 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_newmessages_alter_projects_link_sociallinks'),
    ]

    operations = [
        migrations.AddField(
            model_name='sociallinks',
            name='portfolio',
            field=models.CharField(max_length=300, null=True),
        ),
    ]