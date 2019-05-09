# Generated by Django 2.1.7 on 2019-05-09 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190505_0547'),
    ]

    operations = [
        migrations.CreateModel(
            name='BattleCampaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(blank=True, max_length=20, null=True)),
                ('member_name', models.CharField(blank=True, max_length=50, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('coefficient', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
            ],
        ),
    ]
