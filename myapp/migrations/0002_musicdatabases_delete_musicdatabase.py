# Generated by Django 4.1.7 on 2023-04-22 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='musicDatabases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('album', models.ImageField(upload_to='myapp')),
                ('artist', models.CharField(max_length=255)),
                ('track', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.DeleteModel(
            name='musicDatabase',
        ),
    ]
