from django.db import models




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

    def __str__(self):
        return f'{self.organ}'
    

class OrganRecipient(models.Model):
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    organ = models.ForeignKey(OrganData, on_delete=models.CASCADE)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
    maximum_waiting_time = models.PositiveIntegerField()
    skin_color = models.CharField(max_length=10, choices=SKIN_COLOR_CHOICES)
    price = models.PositiveIntegerField(help_text="in Dollars")
    location = models.CharField(max_length=30, default='Wroclaw')
   
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
    # owner
    apperance = models.PositiveSmallIntegerField(default=1, choices=SCALE_TO_TWENTY_CHOICES, help_text='Scale from 1 to 20')
    vehicle = models.ManyToManyField(Vehicle, related_name='clinics', blank=True)
    vehicle_storages = models.ManyToManyField(VehicleStorageArea, related_name='clinics', blank=True) #Zmiana na VehicleStorageArea?
    helipad = models.BooleanField(default=False)
    runway = models.BooleanField(default=False)
    mortuary_capacity = models.IntegerField(default=0)
    organ_fridge = models.BooleanField(default=False) #miejsce do składowania organow
    technical_staff = models.ManyToManyField(TechnicalStaff, related_name='clinics', blank=True)
    medical_personnel = models.ManyToManyField(MedicalStaff, related_name='clinics', blank=True)
    rating = models.IntegerField(default=90, help_text='Rating scale from 1 to 100')

    def __str__(self):
        return self.name
    


    




# class OrganPossessed(models.Model):
    # pass







