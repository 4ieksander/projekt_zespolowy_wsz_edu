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

SCALE_TO_TEN_CHOICES = [
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
    max_delivery_time = models.PositiveIntegerField()
    difficulty_of_operation = models.CharField(max_length=2, choices=SCALE_TO_TEN_CHOICES)
    min_price = models.PositiveIntegerField(help_text="counted in thousans Dollars")
    max_price = models.PositiveIntegerField(help_text="counted in thousans Dollars")
    difficulty_of_transportation = models.CharField(max_length=64, default='easy')
    people_to_transport = models.PositiveIntegerField()
    nurses_on_the_operation = models.PositiveIntegerField()
    anesthesiologists_on_the_operation = models.PositiveIntegerField()
    surgeons_on_the_operation = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.organ}'
    

class OrganRecipient(models.Model):
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    organ = models.ForeignKey(OrganData, on_delete=models.CASCADE)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
    maximum_waiting_time = models.PositiveIntegerField()
    skin_color = models.CharField(max_length=10, choices=SKIN_COLOR_CHOICES)
    price = models.PositiveIntegerField()
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
    username = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    age = models.PositiveSmallIntegerField()
    skill = models.PositiveSmallIntegerField(choices=SCALE_TO_TEN_CHOICES)
    cost_per_hour = models.PositiveIntegerField()
    maximum_time_of_shift = models.PositiveSmallIntegerField()
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
    maximum_time_of_shift = models.PositiveSmallIntegerField()
    number_of_vacation_days = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.profession} {self.surname} age {self.age}'

class Clinic(models.Model):
    name = models.CharField(max_length=100)
    appearance_scale = models.PositiveSmallIntegerField(default=1, help_text='Scale from 1 to 20')
    vehicle = models.CharField(max_length=50, default='bicycle')
    garage = models.BooleanField(default=False)
    helipad = models.BooleanField(default=False)
    runway = models.BooleanField(default=False)
    hangar = models.BooleanField(default=False)
    mortuary_capacity = models.IntegerField(default=0, help_text='Capacity for number of persons')
    organ_fridge = models.BooleanField(default=False)
    technical_staff = models.ManyToManyField(TechnicalStaff, related_name='clinics')
    medical_personnel = models.ManyToManyField(MedicalStaff, related_name='clinics')
    rating = models.IntegerField(default=100, help_text='Rating scale from 1 to 100')

    def __str__(self):
        return self.name
    


    




# class OrganPossessed(models.Model):
    # pass







