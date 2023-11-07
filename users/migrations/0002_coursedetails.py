# Generated by Django 4.0 on 2023-11-07 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('amount', models.ImageField(max_length=200, upload_to='')),
                ('amount_in_words', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]