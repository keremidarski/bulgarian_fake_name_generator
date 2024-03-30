import json
import random
import string
from datetime import datetime, timedelta


class SockPuppet:
    def __init__(self, gender=None):
        if gender == "random":
            self.gender = random.choice(["male", "female"])
        elif gender in ["male", "female"]:
            self.gender = gender

        self.first_name = self.generate_first_name()
        self.last_name = self.generate_last_name()
        self.date_of_birth = self.generate_date_of_birth()
        self.egn = self.generate_egn()
        self.address, self.region = self.generate_address()
        self.phone_number = self.generate_phone_number()
        self.email = self.generate_email()
        self.username = self.generate_username()
        self.password = self.generate_password()
        self.website_domain = self.generate_website_domain()

    def generate_first_name(self):
        if self.gender == "male":
            names = self._read_strings_from_file("./lists/male_first_names.txt")
        else:
            names = self._read_strings_from_file("./lists/female_first_names.txt")

        return random.choice(names)

    def generate_last_name(self):
        if self.gender == "male":
            names = self._read_strings_from_file("./lists/male_family_names.txt")
        else:
            names = self._read_strings_from_file("./lists/female_family_names.txt")

        return random.choice(names)

    def generate_date_of_birth(self):
        today = datetime.now()
        earliest_birth_date = today - timedelta(days=70 * 365)
        latest_birth_date = today - timedelta(days=18 * 365)
        dob = earliest_birth_date + timedelta(
            days=random.randint(0, (latest_birth_date - earliest_birth_date).days)
        )

        return dob.strftime("%Y-%m-%d")

    def generate_egn(self):
        year = self.date_of_birth[:4][-2:]
        month = self.date_of_birth[5:7]
        day = self.date_of_birth[8:10]
        birthday = f"{year}{month}{day}"

        region_start, region_end = self.region_codes
        region_range = range(region_start, region_end)

        while True:
            if self.gender == "male":
                possible_region_codes = [
                    x for x in range(region_start, region_end) if x % 2 == 0
                ]  # Even numbers for male
            else:  # Female
                possible_region_codes = [
                    x for x in range(region_start, region_end) if x % 2 != 0
                ]  # Odd numbers for female

            region_code = random.choice(possible_region_codes)

            # Generate the EGN
            for check_num in range(0, 10):
                egn = f"{birthday}{region_code:02d}{check_num}"

                if self._validate_egn(egn):
                    return egn

        return egn

    def generate_address(self):
        cities = self._read_json_file("./lists/cities.json")
        city = random.choice(cities)

        city_name = city["name"]
        region_codes = city["codes"]
        
        streets = self._read_strings_from_file("./lists/streets.txt")
        street = random.choice(streets)
        street_number = random.randint(1, 1000)

        return (
            f"{city}, {street} {street_number}",
            region_codes,
        )

    def generate_phone_number(self):
        prefix = random.choice(["087", "088", "089"])
        fourth_digit = random.choice(string.digits)
        middle_part = "".join(random.choices(string.digits, k=3))
        last_part = "".join(random.choices(string.digits, k=3))

        return f"{prefix}{fourth_digit} {middle_part} {last_part}"

    def generate_email(self):
        domain = random.choice(
            ["abv.bg", "mail.bg", "gmail.com", "yahoo.com", "hotmail.com"]
        )

        return f"{self.first_name.lower()}.{self.last_name.lower()}@{domain}"

    def generate_username(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}_{random.randint(100, 999)}"

    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        
        return "".join(random.choices(characters, k=8))

    def generate_website_domain(self):
        return f"www.{random.choice(['example', 'test', 'demo'])}.{random.choice(['bg', 'eu', 'io', 'fun', 'store', 'com', 'net', 'org'])}"

    def _validate_egn(self, egn):
        egn_weights = (2, 4, 8, 5, 10, 9, 7, 3, 6)
        egn_sum = sum([weight * int(digit) for weight, digit in zip(egn_weights, egn)])
        
        return int(egn[-1]) == egn_sum % 11 % 10
    
    def _read_strings_from_file(self, filename):
        with open(filename, "r") as file:
            strings = file.read().splitlines()

        return strings

    def _read_json_file(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)
            
        return data

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}\nGender: {self.gender}\nDate of Birth: {self.date_of_birth}\nEGN: {self.egn}\nAddress: {self.address}\nPhone Number: {self.phone_number}\nEmail: {self.email}\nUsername: {self.username}\nPassword: {self.password}\nWebsite Domain: {self.website_domain}"
