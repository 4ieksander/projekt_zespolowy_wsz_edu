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
    difficulty_of_operation = models.CharField(max_length=32, default='easy')
    min_price = models.PositiveIntegerField()
    max_price = models.PositiveIntegerField()
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

# class OrganPossessed(models.Model):
    # pass







