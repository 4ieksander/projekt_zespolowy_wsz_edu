from random import randint, random
from .models import OrganDonor, GENDER_CHOICES, BLOOD_TYPE_CHOICES, HEALTH_CHOICES, ETHNICITY_CHOICES, SKIN_COLOR_CHOICES

def create():
    pass
class CreateRandomOrganDonor():
    def __init__(self):
        #zdefiniowanie list zawierających dostępne opcje dla każdego pola w modelu
        self.gender_choices = [choice[0] for choice in GENDER_CHOICES]
        self.blood_type_choices = [choice[0] for choice in BLOOD_TYPE_CHOICES]
        self.health_choices = [choice[0] for choice in HEALTH_CHOICES]
        self.ethnicity_choices = [choice[0] for choice in ETHNICITY_CHOICES]
        self.skin_color_choices = [choice[0] for choice in SKIN_COLOR_CHOICES]

    def create_random_organ_donor(self):
        self.assign_random_values_to_option_variables()
        self.assign_random_values_to_boolean_variables()
        self.assign_random_values_to_float_variables()
        self.create_a_record_in_the_database()

    def assign_random_values_to_option_variables(self):
        self.gender = self.generate_random_option(self.gender_choices)
        self.blood_type = self.generate_random_option(self.blood_type_choices)
        self.health = self.generate_random_option(self.health_choices)
        self.ethnicity = self.generate_random_option(self.ethnicity_choices)
        self.skin_color = self.generate_random_option(self.skin_color_choices)

    def generate_random_option(self, choices):
        return choices[randint(0, len(choices)-1)]

    def assign_random_values_to_boolean_variables(self):
        self.diabetes = self.generate_bool_random_value_with_incidence_rate(0.5)
        self.drug_addict = self.generate_bool_random_value_with_incidence_rate(0.5)
        self.smoker = self.generate_bool_random_value_with_incidence_rate(0.7)
        self.after_heart_attack = self.generate_bool_random_value_with_incidence_rate(0.5)
        self.alcoholic = self.generate_bool_random_value_with_incidence_rate(0.6)
        self.aids = self.generate_bool_random_value_with_incidence_rate(0.3)
        self.cancer = self.generate_bool_random_value_with_incidence_rate(0.45)
        self.alcohol_in_process = self.generate_bool_random_value_with_incidence_rate(0.6)
        self.drugs_in_process = self.generate_bool_random_value_with_incidence_rate(0.5)
        self.mental_illness = self.generate_bool_random_value_with_incidence_rate(0.45)

    def generate_bool_random_value_with_incidence_rate(self, incidence):
        random_value = random()
        if random_value <= incidence:
            return True
        elif random_value > incidence:
            return False


    def assign_random_values_to_float_variables(self):
        self.age = self.generate_int_random_value_in_the_range(18, 100)
        self.temperature = self.generate_int_random_value_in_the_range(34, 42)
        beggin_of_weight_range, end_of_weight_range, beggin_of_height_range, end_of_height_range = self.select_range_for_height_and_weight()
        self.weight = self.generate_int_random_value_in_the_range(beggin_of_weight_range, end_of_weight_range)
        self.height = self.generate_int_random_value_in_the_range(beggin_of_height_range, end_of_height_range)

    def select_range_for_height_and_weight(self):
       
        if self.gender == 'F':
            beggin_of_weight_range = 45
            end_of_weight_range = 110
            beggin_of_height_range = 150
            end_of_height_range = 190
        elif self.gender == 'M':
            beggin_of_weight_range = 50
            end_of_weight_range = 150
            beggin_of_height_range = 155
            end_of_height_range = 205
        elif self.age <=100:
            beggin_of_weight_range = 50
            end_of_weight_range = 120
            beggin_of_height_range = 150
            end_of_height_range = 200

        return beggin_of_weight_range, end_of_weight_range, beggin_of_height_range, end_of_height_range
        
    def generate_int_random_value_in_the_range(self, beggin_of_range, end_of_range):
        return randint(beggin_of_range, end_of_range)

    def create_a_record_in_the_database(self):
        organ_donor = OrganDonor.objects.create(
            gender=self.gender,
            age=self.age,
            blood_type=self.blood_type,
            weight=self.weight,
            height=self.height,
            temperature=self.temperature,
            health=self.health,
            diabetes=self.diabetes,
            drug_addict=self.drug_addict,
            smoker=self.smoker,
            after_heart_attack=self.after_heart_attack,
            alcoholic=self.alcoholic,
            aids=self.aids,
            cancer=self.cancer,
            alcohol_in_process=self.alcohol_in_process,
            drugs_in_process=self.drugs_in_process,
            mental_illness=self.mental_illness,
            ethnicity=self.ethnicity,
            skin_color=self.skin_color
        )
        return organ_donor
    

if __name__ == "__main__":
    random_organ_donor = CreateRandomOrganDonor()
