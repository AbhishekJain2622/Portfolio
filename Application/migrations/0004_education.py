# Generated by Django 5.0.4 on 2024-05-28 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0003_aboutme_img2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institiute', models.CharField(max_length=100)),
                ('cls', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=60)),
                ('timeStamp', models.DateTimeField()),
            ],
        ),
    ]