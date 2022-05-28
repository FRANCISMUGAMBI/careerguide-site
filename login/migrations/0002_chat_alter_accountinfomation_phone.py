# Generated by Django 4.0.3 on 2022-04-15 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_to', models.CharField(max_length=50)),
                ('sent_from', models.CharField(max_length=50)),
                ('message_to', models.CharField(max_length=200)),
                ('message_from', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='accountinfomation',
            name='phone',
            field=models.CharField(default=254712345678, max_length=15),
        ),
    ]
