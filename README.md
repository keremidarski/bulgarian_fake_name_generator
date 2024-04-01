# Bulgarian Sock Puppet Generator

The Bulgarian Sock Puppet Generator is a tool for generating realistic fake identities, a.k.a. sock puppets, tailored specifically for Bulgaria. It generates random personas with authentic Bulgarian names, addresses, phone numbers, email addresses, and more.

### Features
![image](https://github.com/keremidarski/bulgarian_sock_puppet/assets/12044844/59df640e-f84f-490e-b005-22c9ce37318c)
* Generates a random **name** with Cyrillic and Latin representations.
* Provides a randomly generated **photo URL** based on the puppet's gender.
* Generates a random **date of birth** and calculates the **age** and **zodiac sign**.
* Generates a random **address** with a **street name**, **street number**, **city**, and **region**.
* Generates a **valid Bulgarian personal identification number (EGN)** based on the puppet's gender and date of birth, **passing official validation**.

![image](https://github.com/keremidarski/bulgarian_sock_puppet/assets/12044844/425fccdb-c2b9-4c85-bece-aca1f64e8303)
* Generates a random **Bulgarian phone number**.
* Generates a random **credit card number** with a **valid checksum**, formatted as XXXX XXXX XXXX XXXX, **passing the MOD 10 check (Luhn formula)**.

![318520838-7c0117b9-21d0-4239-bc44-f4a3807fec2d (1)](https://github.com/keremidarski/bulgarian_sock_puppet/assets/12044844/032fa602-0dc2-4bb2-a241-1d73e007f0d3)
* Generates a random **email address** based on the puppet's name, birth year, and a random domain.
* Generates a random **username** based on the puppet's name and birth year, with random separators.
* Generates a random **password** with 16 characters, including letters, digits, and punctuation marks.
* Generates a random **website domain** based on the puppet's name and birth year, with a random top-level domain.

### Future improvements
* **Random Fake Photo**: I want to add an integration with a fake person generator API so I can generate a photo to match the fake persona.
* **Improved Addresses**: Right now the addresses are a randomly generated combination of cities, streets and numbers but I want to improve the dataset so it can generate real addresses.
* **Website**: I am working on a web page that will let you generate a random persona.
* **API**: I plan on creating an API that will let you generate a fake persona with all the needed details.

### Acknowledgments
* Inspired by the [Fake Name Generator website](https://www.fakenamegenerator.com/) 
* Uses a modified version of [Miglen Evlogiev's EGN generation formula](https://github.com/miglen/egn)
