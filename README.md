# Bulgarian Sock Puppet Generator

The Bulgarian Sock Puppet Generator is a tool for generating realistic fake identities, a.k.a. sock puppets, tailored specifically for Bulgaria. It generates random personas with authentic Bulgarian names, addresses, phone numbers, email addresses, and more.

### Features
* **Localized Data**: Utilizes data specific to Bulgaria, including names, cities, street names, valid Bulgarian unified civil number (EGN), phone numbers, and more, to generate realistic personas.
* **Customizable Gender**: Allows users to specify the gender of the generated personas (male, female, or random).
* **Comprehensive Details**: Generates a wide range of personal details, including names, addresses, phone numbers, email addresses, usernames, passwords, website domains, date of birth, and Bulgarian unified civil number (EGN).
* **Randomization**: Incorporates randomization to ensure unique and diverse personas with each generation.
* **Easy Integration**: Simple Python class structure allows for easy integration into other projects or systems.

### Future improvements
* **Random Fake Photo**: I want to add an integration with a fake person generator API so I can generate a photo to match the fake persona.
* **Improved Addresses**: Right now the addresses are a randomly generated combination of cities, streets and numbers but I want to improve the dataset so it can generate real addresses.
* **Website**: I am working on a web page that will let you generate a random persona.
* **API**: I plan on creating an API that will let you generate a fake persona with all the needed details.

### Acknowledgments
* Inspired by the [Fake Name Generator website](https://www.fakenamegenerator.com/) 
* Uses a modified version of [Miglen Evlogiev's EGN generation formula](https://github.com/miglen/egn)
