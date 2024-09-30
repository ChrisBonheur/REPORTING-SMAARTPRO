# Generated by Django 5.0.4 on 2024-09-27 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smaartpro', '0009_bulletin_studentcard'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvisPaiement',
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