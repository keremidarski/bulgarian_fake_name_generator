import json
import copy
import random
import string
from datetime import datetime, timedelta


class SockPuppet:
    def __init__(self, gender=None):
        if gender == "random":
            self.gender = random.choice(["мъжки", "женски"])
        else:
            self.gender = "мъжки" if gender == "male" else "женски"

        self.name_info = self.generate_name_info()
        self.cyrillic_first_name = self.name_info["cyrillic_first_name"]
        self.cyrillic_family_name = self.name_info["cyrillic_family_name"]
        self.latin_first_name = self.name_info["latin_first_name"]
        self.latin_family_name = self.name_info["latin_family_name"]

        self.photo = self.generate_photo()

        self.dob, self.age = self.generate_date_of_birth()
        self.bg_date_of_birth = self._format_bg_date_of_birth(
            self.dob.day, self.dob.month, self.dob.year
        )
        self.star_sign = self._get_star_sign(self.dob.month, self.dob.day)

        self.address, self.region_codes = self.generate_address()
        self.egn = self.generate_egn()
        self.phone_number = self.generate_phone_number()

        self._generator = random.Random()
        self._generator.seed()
        self._credit_card = self.generate_credit_card_number()

        self.email = self.generate_email()
        self.username = self.generate_username()
        self.password = self.generate_password()
        self.website_domain = self.generate_website_domain()

    def generate_name_info(self):
        if self.gender == "мъжки":
            first_names = self._read_json_file("./lists/male_first_names.json")
            family_names = self._read_json_file("./lists/male_family_names.json")
        else:
            first_names = self._read_json_file("./lists/female_first_names.json")
            family_names = self._read_json_file("./lists/female_family_names.json")

        first_name = random.choice(first_names)
        last_name = random.choice(family_names)

        name_info = {
            "cyrillic_first_name": first_name["cyrillic"],
            "cyrillic_family_name": last_name["cyrillic"],
            "latin_first_name": first_name["latin"],
            "latin_family_name": last_name["latin"],
        }

        return name_info

    def generate_photo(self):
        if self.gender == "мъжки":
            return "https://xsgames.co/randomusers/avatar.php?g=male"
        else:
            return "https://xsgames.co/randomusers/avatar.php?g=female"

    def generate_date_of_birth(self):
        today = datetime.now()
        earliest_birth_date = today - timedelta(days=70 * 365)
        latest_birth_date = today - timedelta(days=18 * 365)
        dob = earliest_birth_date + timedelta(
            days=random.randint(0, (latest_birth_date - earliest_birth_date).days)
        )

        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        return dob, age

    def generate_egn(self):
        dob_to_parse = self.dob.strftime("%Y-%m-%d")

        if int(dob_to_parse[:4]) >= 2000:
            year = dob_to_parse[:4][-2:]
            month = int(dob_to_parse[5:7]) + 40
            day = dob_to_parse[8:10]
            birthday = f"{year}{month:02d}{day}"
        else:
            year = dob_to_parse[:4][-2:]
            month = dob_to_parse[5:7]
            day = dob_to_parse[8:10]
            birthday = f"{year}{month}{day}"

        region_start, region_end = self.region_codes

        while True:
            if self.gender == "мъжки":
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
        street_number = random.randint(1, 130)

        return (
            f"{city_name}, ул. {street} {street_number}",
            region_codes,
        )

    def generate_phone_number(self):
        prefix = random.choice(
            [
                "0877",
                "0878",
                "0879",
                "0882",
                "0883",
                "0884",
                "0885",
                "0886",
                "0887",
                "0888",
                "0889",
                "0892",
                "0893",
                "0894",
                "0895",
                "0896",
                "0897",
                "0898",
                "0899",
            ]
        )
        middle_part = "".join(random.choices(string.digits, k=3))
        last_part = "".join(random.choices(string.digits, k=3))

        return f"{prefix} {middle_part} {last_part}"

    def generate_credit_card_number(self):
        visa_prefix_list = [
            ["4", "5", "3", "9"],
            ["4", "5", "5", "6"],
            ["4", "9", "1", "6"],
            ["4", "5", "3", "2"],
            ["4", "9", "2", "9"],
            ["4", "0", "2", "4", "0", "0", "7", "1"],
            ["4", "4", "8", "6"],
            ["4", "7", "1", "6"],
            ["4"],
        ]

        mastercard_prefix_list = [
            ["5", "1"],
            ["5", "2"],
            ["5", "3"],
            ["5", "4"],
            ["5", "5"],
        ]

        if random.choice([True, False]):
            return self._credit_card_number(visa_prefix_list, 16)
        else:
            return self._credit_card_number(mastercard_prefix_list, 16)

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

        first_name_components = [
            self.latin_first_name.lower(),
            self.latin_first_name.lower()[0],
            self.latin_first_name.lower()[:3],
        ]
        last_name_components = [
            self.latin_family_name.lower(),
            self.latin_family_name.lower()[0],
            self.latin_family_name.lower()[:3],
        ]
        year_components = [self.bg_date_of_birth[-4:], self.bg_date_of_birth[-2:]]

        first_name_component = random.choice(first_name_components)
        last_name_component = random.choice(last_name_components)
        year_component = random.choice(year_components)

        separators = ["_", "-", ".", ""]
        separator = random.choice(separators)

        name_choices = [
            f"{first_name_component}{last_name_component}{year_component}",
            f"{first_name_component}{separator}{last_name_component}",
            f"{last_name_component}{year_component}",
            f"{first_name_component}{last_name_component}",
        ]
        name_choice = random.choice(name_choices)

        return f"{name_choice}@{domain}"

    def generate_username(self):
        first_name_components = [
            self.latin_first_name.lower(),
            self.latin_first_name.lower()[0],
            self.latin_first_name.lower()[:3],
        ]
        last_name_components = [
            self.latin_family_name.lower(),
            self.latin_family_name.lower()[0],
            self.latin_family_name.lower()[:3],
        ]
        year_components = [self.bg_date_of_birth[-4:], self.bg_date_of_birth[-2:]]

        first_name_component = random.choice(first_name_components)
        last_name_component = random.choice(last_name_components)
        year_component = random.choice(year_components)

        separators = ["_", "-", ".", ""]
        separator = random.choice(separators)

        components_order = [first_name_component, last_name_component, year_component]
        random.shuffle(components_order)

        username_parts = []

        for component in components_order:
            username_parts.append(component)

            if len(username_parts) < 3:
                username_parts.append(separator)

        username = "".join(username_parts)

        return username

    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation

        return "".join(random.choices(characters, k=16))

    def generate_website_domain(self):
        return f"www.{random.choice([self.latin_first_name.lower(), self.latin_family_name.lower(), self.latin_first_name.lower() + self.latin_family_name.lower(), self.latin_family_name.lower() + self.bg_date_of_birth[-2:]])}.{random.choice(['bg', 'eu', 'io', 'fun', 'store', 'com', 'net', 'org'])}"

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

        bg_date = f"{day} {bg_month_names[month]} {year}"

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

    def _completed_number(self, prefix, length):
        ccnumber = prefix

        while len(ccnumber) < (length - 1):
            digit = str(self._generator.choice(range(0, 10)))
            ccnumber.append(digit)

        sum = 0
        pos = 0

        reversedCCnumber = []
        reversedCCnumber.extend(ccnumber)
        reversedCCnumber.reverse()

        while pos < length - 1:
            odd = int(reversedCCnumber[pos]) * 2
            if odd > 9:
                odd -= 9
            sum += odd

            if pos != (length - 2):
                sum += int(reversedCCnumber[pos + 1])

            pos += 2

        checkdigit = ((sum // 10 + 1) * 10 - sum) % 10

        ccnumber.append(str(checkdigit))

        cc_number_str = "".join(ccnumber)

        # Format the credit card number with spaces after every four digits
        formatted_cc_number = " ".join(
            cc_number_str[i : i + 4] for i in range(0, len(cc_number_str), 4)
        )

        return formatted_cc_number

    def _credit_card_number(self, prefix_list, length):
        ccnumber = copy.copy(self._generator.choice(prefix_list))
        return self._completed_number(ccnumber, length)

    def _read_strings_from_file(self, filename):
        with open(filename, "r", encoding="utf8") as file:
            strings = file.read().splitlines()

        return strings

    def _read_json_file(self, filename):
        with open(filename, "r", encoding="utf8") as file:
            data = json.load(file)

        return data

    def __str__(self):
        return f"Име: {self.cyrillic_first_name} {self.cyrillic_family_name}\nПол: {self.gender}\nДата на раждане: {self.bg_date_of_birth}г.\nВъзраст: {self.age} години\nЗодия: {self.star_sign}\nЕГН: {self.egn}\nАдрес: {self.address}\nТелефон: {self.phone_number}\nБанкова карта: {self._credit_card}\nEmail: {self.email}\nUsername: {self.username}\nPassword: {self.password}\nWebsite: {self.website_domain}"
