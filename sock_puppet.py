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
        self.address = self.generate_address()
        self.phone_number = self.generate_phone_number()
        self.email = self.generate_email()
        self.username = self.generate_username()
        self.password = self.generate_password()
        self.website_domain = self.generate_website_domain()

    def read_strings_from_file(self, filename):
        with open(filename, "r") as file:
            strings = file.read().splitlines()

        return strings

    def generate_first_name(self):
        if self.gender == "male":
            names = self.read_strings_from_file("./lists/male_first_names.txt")
        else:
            names = self.read_strings_from_file("./lists/female_first_names.txt")

        return random.choice(names)

    def generate_last_name(self):
        if self.gender == "male":
            names = self.read_strings_from_file("./lists/male_family_names.txt")
        else:
            names = self.read_strings_from_file("./lists/female_family_names.txt")

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

        random_digits = ''.join(random.choices(string.digits, k=4))
        egn = f"{year}{month}{day}{random_digits}"
        
        return egn

    def generate_address(self):
        cities = self.read_strings_from_file("./lists/cities.txt")
        street_number = random.randint(1, 1000)
        city = random.choice(cities)

        return f"{street_number} {street_name}, {city}, {state} {zip_code}"

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

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}\nGender: {self.gender}\nDate of Birth: {self.date_of_birth}\nEGN: {self.egn}\nAddress: {self.address}\nPhone Number: {self.phone_number}\nEmail: {self.email}\nUsername: {self.username}\nPassword: {self.password}\nWebsite Domain: {self.website_domain}"
