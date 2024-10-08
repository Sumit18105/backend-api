# Generated by Django 5.0.3 on 2024-08-17 16:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_Authentication',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('language_preference', models.CharField(choices=[('EN', 'English'), ('HN', 'Hindi'), ('Tl', 'Telugu'), ('KN', 'Kannada')], max_length=15)),
                ('experience', models.IntegerField()),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('qualifications_proof', models.ImageField(blank=True, null=True, upload_to='qualification_proofs/')),
                ('id_proof', models.ImageField(blank=True, null=True, upload_to='id_proofs/')),
                ('specialization', models.CharField(choices=[('DVM', 'Doctor of Veterinary Medicine (DVM)'), ('BVSc', 'Bachelor of Veterinary Science (BVSc)'), ('MVSc', 'Master of Veterinary Science (MVSc)'), ('PhD', 'Doctor of Philosophy (PhD)'), ('Diplomate_ACVS', 'Diplomate, American College of Veterinary Surgeons (ACVS)'), ('Diplomate_ACVIM', 'Diplomate, American College of Veterinary Internal Medicine (ACVIM)'), ('Diplomate_ACVR', 'Diplomate, American College of Veterinary Radiology (ACVR)'), ('Diplomate_ACVO', 'Diplomate, American College of Veterinary Ophthalmologists (ACVO)'), ('Diplomate_ACVD', 'Diplomate, American College of Veterinary Dermatology (ACVD)'), ('Diplomate_ACVAA', 'Diplomate, American College of Veterinary Anesthesia and Analgesia (ACVAA)'), ('Diplomate_ACVN', 'Diplomate, American College of Veterinary Nutrition (ACVN)'), ('Diplomate_ACVPM', 'Diplomate, American College of Veterinary Preventive Medicine (ACVPM)'), ('Diplomate_ACVB', 'Diplomate, American College of Veterinary Behaviorists (ACVB)'), ('other', 'Other')], max_length=20)),
                ('qualifications', models.CharField(choices=[('Small Animal Surgery', 'Small Animal Surgery'), ('Large Animal Surgery', 'Large Animal Surgery'), ('Internal Medicine', 'Internal Medicine'), ('Anesthesiology', 'Anesthesiology'), ('Dermatology', 'Dermatology'), ('Cardiology', 'Cardiology'), ('Oncology', 'Oncology'), ('Radiology', 'Radiology'), ('Ophthalmology', 'Ophthalmology'), ('Dentistry', 'Dentistry'), ('Behavioral Medicine', 'Behavioral Medicine'), ('Emergency and Critical Care', 'Emergency and Critical Care'), ('Exotic Animal Medicine', 'Exotic Animal Medicine'), ('Zoo Medicine', 'Zoo Medicine'), ('Nutrition', 'Nutrition'), ('Neurology', 'Neurology'), ('Rehabilitation and Sports Medicine', 'Rehabilitation and Sports Medicine'), ('Pathology', 'Pathology'), ('Reproductive Medicine', 'Reproductive Medicine'), ('Toxicology', 'Toxicology'), ('Public Health', 'Public Health'), ('other', 'Other')], max_length=200)),
                ('about', models.TextField()),
                ('number_of_consultations', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User_Authentication',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('pet_type', models.CharField(choices=[('dog', 'Dog'), ('cat', 'Cat'), ('parrot', 'Parrot'), ('bird', 'Bird'), ('reptile', 'Reptile'), ('other', 'Other')], max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Accounts_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toatal_earning', models.IntegerField(default=0)),
                ('total_refunds', models.IntegerField(default=0)),
                ('bank_name', models.CharField(max_length=20)),
                ('branch_name', models.CharField(max_length=20)),
                ('account_number', models.IntegerField()),
                ('ifsc_code', models.CharField(max_length=20)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.doctor_authentication')),
            ],
        ),
    ]
