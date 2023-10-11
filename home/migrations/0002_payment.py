# Generated by Django 4.2.6 on 2023-10-11 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_name', models.CharField(max_length=100)),
                ('transaction_id', models.CharField(max_length=100)),
                ('user_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.user_plan')),
            ],
        ),
    ]
