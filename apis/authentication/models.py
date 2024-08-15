from django.db import models

# Create your models here.

class User_Authentication(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=13)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=16,
                                choices=[
                                     ('dog', 'Dog'),
                                     ('cat', 'Cat'),
                                     ('parrot', 'Parrot'),
                                     ('bird', 'Bird'),
                                     ('reptile', 'Reptile'),
                                     ('other', 'Other')
                                     ])
class Doctor_Authentication(models.Model):
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=20)

# class User_Details(models.Model):
class Doctor_Authentication(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=13)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    language_preference = models.CharField(
        max_length=15,
        choices=[
            ('EN', 'English'),
            ('HN', 'Hindi'),
            ('Tl', 'Telugu'),
            ('KN', 'Kannada')
        ]
    )
    experience = models.IntegerField()

    # Media Files
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    qualifications_proof = models.ImageField(upload_to='qualification_proofs/', blank=True, null=True)
    id_proof = models.ImageField(upload_to='id_proofs/', blank=True, null=True)

    specialization = models.CharField(max_length=20,
                                      choices=[
                                            ('DVM', 'Doctor of Veterinary Medicine (DVM)'),
                                            ('BVSc', 'Bachelor of Veterinary Science (BVSc)'),
                                            ('MVSc', 'Master of Veterinary Science (MVSc)'),
                                            ('PhD', 'Doctor of Philosophy (PhD)'),
                                            ('Diplomate_ACVS', 'Diplomate, American College of Veterinary Surgeons (ACVS)'),
                                            ('Diplomate_ACVIM', 'Diplomate, American College of Veterinary Internal Medicine (ACVIM)'),
                                            ('Diplomate_ACVR', 'Diplomate, American College of Veterinary Radiology (ACVR)'),
                                            ('Diplomate_ACVO', 'Diplomate, American College of Veterinary Ophthalmologists (ACVO)'),
                                            ('Diplomate_ACVD', 'Diplomate, American College of Veterinary Dermatology (ACVD)'),
                                            ('Diplomate_ACVAA', 'Diplomate, American College of Veterinary Anesthesia and Analgesia (ACVAA)'),
                                            ('Diplomate_ACVN', 'Diplomate, American College of Veterinary Nutrition (ACVN)'),
                                            ('Diplomate_ACVPM', 'Diplomate, American College of Veterinary Preventive Medicine (ACVPM)'),
                                            ('Diplomate_ACVB', 'Diplomate, American College of Veterinary Behaviorists (ACVB)'),
                                            ('other', 'Other')

                                      ])
    qualifications = models.CharField(max_length=200,choices=[
        ('Small Animal Surgery', 'Small Animal Surgery'),
        ('Large Animal Surgery', 'Large Animal Surgery'),
        ('Internal Medicine', 'Internal Medicine'),
        ('Anesthesiology', 'Anesthesiology'),
        ('Dermatology', 'Dermatology'),
        ('Cardiology', 'Cardiology'),
        ('Oncology', 'Oncology'),
        ('Radiology', 'Radiology'),
        ('Ophthalmology', 'Ophthalmology'),
        ('Dentistry', 'Dentistry'),
        ('Behavioral Medicine', 'Behavioral Medicine'),
        ('Emergency and Critical Care', 'Emergency and Critical Care'),
        ('Exotic Animal Medicine', 'Exotic Animal Medicine'),
        ('Zoo Medicine', 'Zoo Medicine'),
        ('Nutrition', 'Nutrition'),
        ('Neurology', 'Neurology'),
        ('Rehabilitation and Sports Medicine', 'Rehabilitation and Sports Medicine'),
        ('Pathology', 'Pathology'),
        ('Reproductive Medicine', 'Reproductive Medicine'),
        ('Toxicology', 'Toxicology'),
        ('Public Health', 'Public Health'),
        ('other', 'Other')
    ])
    about = models.TextField()
    number_of_consultations = models.IntegerField(default = 0)

class Accounts_Details(models.Model):
    email = models.ForeignKey(Doctor_Authentication, on_delete = models.CASCADE)
    toatal_earning = models.IntegerField(default = 0)
    total_refunds = models.IntegerField(default = 0)
    bank_name = models.CharField(max_length = 20)
    branch_name = models.CharField(max_length = 20)
    account_number = models.IntegerField()
    ifsc_code = models.CharField(max_length = 20)
