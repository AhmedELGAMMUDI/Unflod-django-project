# Generated by Django 5.1 on 2024-08-22 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_care', '0012_unlistedbond_unregisteredbond'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reconciliationmemo',
            name='checks_not_cleared',
        ),
        migrations.RemoveField(
            model_name='reconciliationmemo',
            name='checks_not_recorded',
        ),
    ]
