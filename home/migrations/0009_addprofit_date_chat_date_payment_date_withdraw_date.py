# Generated by Django 4.2.6 on 2023-10-20 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_chat_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='addprofit',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='chat',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='withdraw',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
