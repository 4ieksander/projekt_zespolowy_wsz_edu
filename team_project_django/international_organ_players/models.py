from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone





GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
]
BLOOD_TYPE_CHOICES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-')
]
HEALTH_CHOICES = [
    ('healthy', 'Healthy'),
    ('sick', 'Sick')
]
ETHNICITY_CHOICES = [
    ('White', 'White'),
    ('Black', 'Black'),
    ('Hispanic', 'Hispanic'),
    ('Asian', 'Asian'),
    ('Other', 'Other')
]
SKIN_COLOR_CHOICES = [
    ('Light', 'Light'),
    ('Medium', 'Medium'),
    ('Dark', 'Dark')
]
SCALE_TO_TWENTY_CHOICES = [
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (7,7),
    (8,8),
    (9,9),
    (10,10),
    (11,11),
    (12,12),
    (13,13),
    (14,14),
    (15,15),
    (16,16),
    (17,17),
    (18,18),
    (19,19),
    (20,20),
]

SCALE_TO_TEN_CHOICES = [
    (0,0),
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (7,7),
    (8,8),
    (9,9),
    (10,10),
]
SCALE_TO_FIVE_CHOICES = [
    (0,0),
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
]




class PlayerAttributes(models.Model):
    attribute = models.CharField(max_length=20)
    multiplier_for_operation_skills = models.FloatField()
    change_over_time = models.FloatField(help_text="per hour")

    def __str__(self):
        return self.attribute


class Booster(models.Model):   
    name_of_booster = models.CharField(max_length=20)
    which_improves = models.ManyToManyField(PlayerAttributes, related_name='booster_improves', blank=True)
    which_worsens = models.ManyToManyField(PlayerAttributes, related_name='booster_worses', blank=True)
    how_long_it_takes = models.PositiveSmallIntegerField()
   
    def __str__(self):
        return self.name_of_booster


class Procedure(models.Model):
    id_of_procedure = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'id: {self.id_of_procedure}, {self.name}'


class Equipment(models.Model):
    name_of_equipment = models.CharField(max_length=20)
    enables_the_procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, related_name='equipment')
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name_of_equipment
    

class Location(models.Model):
    location_name = models.CharField(max_length=30)
    coordinator_x = models.FloatField()
    coordinator_y = models.FloatField()

    def __str__(self):
        return self.location_name
    

class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.PositiveSmallIntegerField(help_text="ID of avatar")     #czy uzytkownik moze wrzucic swoj avatar czy jest lista do wyboru? jaka rozdzielczosc?
    nickname = models.CharField(max_length=30)
    stamina = models.PositiveSmallIntegerField(choices=SCALE_TO_TEN_CHOICES, default=10)    #czy może te wszystkie skale powinny być typu float?
    alcohol = models.PositiveSmallIntegerField(choices=SCALE_TO_TEN_CHOICES, default=0)     # wtedy będzie mógł płynnie spadać według czasu 
    temperature = models.FloatField(default=36.6)
    sight = models.PositiveSmallIntegerField(choices=SCALE_TO_FIVE_CHOICES, default=5)
    hunger = models.PositiveSmallIntegerField(choices=SCALE_TO_TEN_CHOICES, default=0) #czy głód 0 -> najedzony, czy odwrotnie?
    mental_state =models.PositiveSmallIntegerField(choices=SCALE_TO_TEN_CHOICES, default=10)
    drugs = models.ManyToManyField(Booster, related_name='players',blank=True) #zmienić na boosters? czy to będzie deklarowane przy tworzeniu czy wgl jak to ma działać?
    dementia = models.PositiveSmallIntegerField(choices=SCALE_TO_TEN_CHOICES, default=0)
    knowledge = models.PositiveSmallIntegerField(choices=SCALE_TO_TEN_CHOICES)
    intelligence =models.PositiveSmallIntegerField(choices=SCALE_TO_TEN_CHOICES)
    time_per_shift = models.PositiveSmallIntegerField(choices=SCALE_TO_TEN_CHOICES)     #czy będzie można rozwijać umiejętności i czy będzie takie coś jak poziom? 
    created_at = models.DateTimeField(default=timezone.now)
    equipment = models.ManyToManyField(Equipment, related_name='players', blank=True)
    nationality = models.CharField(max_length=30) # lista krajów? 
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='players', blank=True)
    dollars = models.BigIntegerField(default=100000)
    bitcoins = models.DecimalField(default=0.5, max_digits=20, decimal_places=6)

    def __str__(self):
            return self.nickname


class OrganDonor(models.Model):
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
    weight = models.FloatField()
    height = models.FloatField()
    temperature = models.FloatField()
    health = models.CharField(max_length=10, choices=HEALTH_CHOICES)
    diabetes = models.BooleanField(default=False)
    drug_addict = models.BooleanField(default=False)
    smoker = models.BooleanField(default=False)
    after_heart_attack = models.BooleanField(default=False)
    alcoholic = models.BooleanField(default=False)
    aids = models.BooleanField(default=False)
    cancer = models.BooleanField(default=False)
    alcohol_in_process = models.BooleanField(default=False)
    drugs_in_process = models.BooleanField(default=False)
    mental_illness = models.BooleanField(default=False)
    ethnicity = models.CharField(max_length=10, choices=ETHNICITY_CHOICES)
    skin_color = models.CharField(max_length=10, choices=SKIN_COLOR_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)
    # clicic ( foregin key ? )
    # alive (true/false?)
    # date of death? 
    def __str__(self):
        return f"{self.gender} patient, age {self.age}"


class OrganData(models.Model): 
    organ = models.CharField(max_length=32, primary_key=True)
    operation_time = models.PositiveIntegerField()    
    min_price = models.PositiveIntegerField(help_text="in Dollars")
    max_price = models.PositiveIntegerField(help_text="in Dollars")
    difficulty_of_transport = models.PositiveSmallIntegerField(choices=SCALE_TO_FIVE_CHOICES)
    difficulty_of_operation = models.PositiveSmallIntegerField(choices=SCALE_TO_TEN_CHOICES)
    max_alive_time = models.PositiveIntegerField(help_text='in minutes')
    difficulty_of_depot = models.PositiveSmallIntegerField(choices=SCALE_TO_FIVE_CHOICES, default=1) #organ_deppot_level
    people_to_transport = models.PositiveSmallIntegerField(choices=SCALE_TO_FIVE_CHOICES) #level_of_transportability
    nurses_on_the_operation = models.PositiveSmallIntegerField(choices=SCALE_TO_FIVE_CHOICES)
    anesthesiologists_on_the_operation = models.PositiveSmallIntegerField(choices=SCALE_TO_FIVE_CHOICES)
    surgeons_on_the_operation = models.PositiveSmallIntegerField(choices=SCALE_TO_FIVE_CHOICES)
    procedures = models.ManyToManyField(Procedure, related_name='organs')
    does_blood_type_matter = models.BooleanField(default=True)
    does_skin_color_matter = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.organ}'


class OrganRecipient(models.Model):
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    organ = models.ForeignKey(OrganData, on_delete=models.CASCADE, related_name='organ_recipients')
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
    maximum_waiting_time = models.PositiveIntegerField()
    skin_color = models.CharField(max_length=10, choices=SKIN_COLOR_CHOICES)
    price = models.PositiveIntegerField(help_text="in Dollars")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='organ_recipients')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.organ} with blood type {self.blood_type} and from {self.location}'


class MedicalStaff(models.Model):
    MEDICAL_PROFESSION_CHOICES = [
        ('nurse', 'Nurse'),
        ('surgeon', 'Surgeon'),
        ('anesthesiologist', 'Anesthesiologist'),
        ]
    
    profession = models.CharField(max_length=20, choices=MEDICAL_PROFESSION_CHOICES)
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    age = models.PositiveSmallIntegerField()
    skill = models.PositiveSmallIntegerField(choices=SCALE_TO_TEN_CHOICES)
    cost_per_hour = models.PositiveIntegerField()
    max_time_per_shift = models.PositiveSmallIntegerField(choices=SCALE_TO_TWENTY_CHOICES)
    number_of_vacation_days = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.profession} {self.surname} age {self.age}'


class TechnicalStaff(models.Model):
    TECHNICAL_PROFFESION_CHOICES = [
        ('electrician', 'Electrician'),
        ('cleaner', 'Cleaner'),
        ('secretary', 'Secretary'),
        ('gangster', 'Gangster'),
        ('gravedigger', 'Gravedigger'),
        ('driver', 'Driver'),
        ]
    
    profession = models.CharField(max_length=20, choices=TECHNICAL_PROFFESION_CHOICES)
    username = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    age = models.PositiveSmallIntegerField()
    skill = models.PositiveSmallIntegerField(choices=SCALE_TO_TEN_CHOICES)
    cost_per_hour = models.PositiveIntegerField()
    max_time_per_shift = models.PositiveSmallIntegerField(choices=SCALE_TO_TWENTY_CHOICES)
    number_of_vacation_days = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.profession} {self.surname} age {self.age}'


class VehicleStorageArea(models.Model):
    storage_name = models.CharField(max_length=30)
    capacity = models.PositiveSmallIntegerField(choices=SCALE_TO_TWENTY_CHOICES)
    storage_level = models.PositiveSmallIntegerField(choices=SCALE_TO_FIVE_CHOICES)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.storage_name


class Vehicle(models.Model):
    vehicle= models.CharField(max_length=20)
    speed = models.PositiveSmallIntegerField(help_text='in km/h')
    level_of_transportability = models.PositiveSmallIntegerField(choices=SCALE_TO_FIVE_CHOICES)
    storage_level = models.PositiveSmallIntegerField(choices=SCALE_TO_FIVE_CHOICES)
    purchase_price = models.PositiveIntegerField()
    maintenance_price = models.PositiveIntegerField(help_text='per day')
    price_per_km = models.PositiveSmallIntegerField()
    minimum_distance = models.PositiveSmallIntegerField(default=0)
    
    def __str__(self):
        return f'{self.vehicle}, max speed {self.speed} km/h, transportability level: {self.level_of_transportability}'


class OrganStorageArea(models.Model):
    storage_name = models.CharField(max_length=20)
    organ_depot_level = models.PositiveSmallIntegerField(choices=SCALE_TO_FIVE_CHOICES)
    capacity = models.PositiveSmallIntegerField(choices=SCALE_TO_TWENTY_CHOICES)
    multiplier_for_organ_suitability = models.FloatField(default=1.00, help_text="type = float")
    is_mobile = models.BooleanField(default=False)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.storage_name


class Clinic(models.Model):
    name = models.CharField(max_length=100)
    owner = models.OneToOneField(Player, on_delete=models.CASCADE, related_name='clinics')
    apperance = models.PositiveSmallIntegerField(default=1, choices=SCALE_TO_TWENTY_CHOICES, help_text='Scale from 1 to 20')
    vehicle = models.ManyToManyField(Vehicle, related_name='clinics', blank=True)
    vehicle_storages = models.ManyToManyField(VehicleStorageArea, related_name='clinics', blank=True) 
    helipad = models.BooleanField(default=False)
    runway = models.BooleanField(default=False)
    mortuary_capacity = models.IntegerField(default=0)
    organ_storage_area = models.ManyToManyField(OrganStorageArea, related_name='clinics', blank=True) 
    technical_staff = models.ManyToManyField(TechnicalStaff, related_name='clinics', blank=True)
    medical_personnel = models.ManyToManyField(MedicalStaff, related_name='clinics', blank=True)
    rating = models.IntegerField(default=90, help_text='Rating scale from 1 to 100')
    equipment = models.ManyToManyField(Equipment, related_name='clinics', blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="clinics")
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name
    

class OrganPossessed(models.Model):
    organ = models.ForeignKey(OrganData, on_delete=models.CASCADE, related_name='existings')
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='organs')
    donor = models.ForeignKey(OrganDonor, on_delete=models.CASCADE, related_name='organs')
    acquisition_time = models.DateTimeField(default=timezone.now)









