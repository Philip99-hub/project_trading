# Generated by Django 4.2.6 on 2023-10-15 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_addprofit_referral_profit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addprofit',
            name='profit',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
