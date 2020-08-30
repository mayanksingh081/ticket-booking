# Generated by Django 3.1 on 2020-08-30 17:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_tickets', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Slots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('ticket_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('no_of_tickets', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('phone_no', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Expired')], default=1)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.show')),
                ('show_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.slots')),
            ],
            options={
                'ordering': ['-show_time'],
            },
        ),
    ]
