# Generated by Django 2.2.5 on 2019-10-07 07:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hackusapp', '0002_auto_20190917_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Writeup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=18, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('body', models.TextField(null=True)),
                ('onoff', models.BooleanField(default=False, verbose_name='onoff')),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writeup', to='hackusapp.Challenge')),
            ],
        ),
    ]
