# Generated by Django 3.1.7 on 2021-04-15 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210415_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('squareFootage', models.DecimalField(decimal_places=3, max_digits=100)),
                ('numberOfStories', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('companyName', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('headQuaters', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Land',
            fields=[
                ('address', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('postalCode', models.CharField(max_length=60)),
                ('sqrAcres', models.DecimalField(decimal_places=3, max_digits=1000)),
                ('neighborhoodName', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.neighborhood')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('email', models.CharField(max_length=60)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('ownerId', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ResidentialBuilding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberOfBathrooms', models.IntegerField()),
                ('numberOfBedrooms', models.IntegerField()),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.building')),
            ],
        ),
        migrations.CreateModel(
            name='Renter',
            fields=[
                ('renterId', models.IntegerField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=60)),
                ('middleName', models.CharField(max_length=60)),
                ('lastName', models.CharField(max_length=60)),
                ('phoneNumber', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.building')),
            ],
        ),
        migrations.CreateModel(
            name='PersonOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=60)),
                ('middleName', models.CharField(max_length=60)),
                ('lastName', models.CharField(max_length=60)),
                ('ownerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.owner')),
            ],
        ),
        migrations.CreateModel(
            name='OwnsRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.land')),
                ('ownerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.owner')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=60)),
                ('companyType', models.CharField(max_length=60)),
                ('ownerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.owner')),
            ],
        ),
        migrations.CreateModel(
            name='CommercialBuilding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industryType', models.CharField(max_length=60)),
                ('numberOfDesks', models.IntegerField()),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.building')),
            ],
        ),
        migrations.AddField(
            model_name='building',
            name='developer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.developer'),
        ),
        migrations.AddField(
            model_name='building',
            name='land',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.land'),
        ),
        migrations.CreateModel(
            name='BankOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankName', models.CharField(max_length=60)),
                ('headQuarters', models.CharField(max_length=60)),
                ('ownerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.owner')),
            ],
        ),
    ]