# Generated by Django 3.2.20 on 2024-07-22 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smaartpro', '0007_closecash'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('groupid', models.IntegerField(default=0)),
                ('type', models.IntegerField(default=0, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]