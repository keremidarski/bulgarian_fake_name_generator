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
        self.date_of_birth, self.bg_date_of_birth, self.age, self.star_sign = self.generate_date_of_birth()
        self.address, self.region_codes = self.generate_address()
        self.egn = self.generate_egn()
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

        # Calculate age
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        # Calculate star sign
        star_sign = self._get_star_sign(dob.month, dob.day)
        
        # Format date of birth in Bulgarian format
        bg_date_of_birth = self._format_bg_date_of_birth(dob.day, dob.month, dob.year)

        return dob.strftime("%Y-%m-%d"), bg_date_of_birth, age, star_sign

    def generate_egn(self):
        if int(self.date_of_birth[:4]) >= 2000:
            year = self.date_of_birth[:4][-2:]
            month = int(self.date_of_birth[5:7]) + 40
            day = self.date_of_birth[8:10]
            birthday = f"{year}{month:02d}{day}"
        else:
            year = self.date_of_birth[:4][-2:]
            month = self.date_of_birth[5:7]
            day = self.date_of_birth[8:10]
            birthday = f"{year}{month}{day}"

        region_start, region_end = self.region_codes

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

    def generate_address(self):
        cities = self._read_json_file("./lists/cities.json")
        city = random.choice(cities)

        city_name = city["name"]
        region_codes = city["codes"]

        streets = self._read_strings_from_file("./lists/street_names.txt")
        street = random.choice(streets)
        street_number = random.randint(1, 300)

        return (
            f"{city_name}, {street} {street_number}",
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
            [
                "abv.bg",
                "mail.bg",
                "dir.bg",
                "outlook.bg",
                "gmail.com",
                "yahoo.com",
                "hotmail.com",
            ]
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
    
    def _format_bg_date_of_birth(self, day, month, year):
        bg_month_names = {
            1: "януари",
            2: "февруари",
            3: "март",
            4: "април",
            5: "май",
            6: "юни",
            7: "юли",
            8: "август",
            9: "септември",
            10: "октомври",
            11: "ноември",
            12: "декември",
        }

        bg_date = f"{day} {bg_month_names[month]} {year}г."

        return bg_date

    def _get_star_sign(self, month, day):
        star_signs = [
            ("Козирог", (1, 1), (1, 19)),
            ("Водолей", (1, 20), (2, 18)),
            ("Риби", (2, 19), (3, 20)),
            ("Овен", (3, 21), (4, 19)),
            ("Телец", (4, 20), (5, 20)),
            ("Близнаци", (5, 21), (6, 20)),
            ("Рак", (6, 21), (7, 22)),
            ("Лъв", (7, 23), (8, 22)),
            ("Дева", (8, 23), (9, 22)),
            ("Везни", (9, 23), (10, 22)),
            ("Скорпион", (10, 23), (11, 21)),
            ("Стрелец", (11, 22), (12, 21)),
            ("Козирог", (12, 22), (12, 31)),
        ]

        for sign, start_date, end_date in star_signs:
            if (month, day) >= start_date and (month, day) <= end_date:
                return sign

    def _read_strings_from_file(self, filename):
        with open(filename, "r", encoding="utf8") as file:
            strings = file.read().splitlines()

        return strings

    def _read_json_file(self, filename):
        with open(filename, "r", encoding="utf8") as file:
            data = json.load(file)

        return data

    def __str__(self):
        return f"Име: {self.first_name} {self.last_name}\nПол: {self.gender}\nРожена дата: {self.bg_date_of_birth}\nВъзраст: {self.age} години\nЗодия: {self.star_sign}\nЕГН: {self.egn}\nАдрес: {self.address}\nТелефон: {self.phone_number}\nEmail: {self.email}\nUsername: {self.username}\nPassword: {self.password}\nWebsite: {self.website_domain}"
