from flask import Flask, render_template, request, jsonify, redirect
from sock_puppet import SockPuppet

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    puppet = SockPuppet("random")

    puppet_data = {
        "photo": puppet.photo,
        "cyrillic_first_name": puppet.cyrillic_first_name,
        "cyrillic_family_name": puppet.cyrillic_family_name,
        "gender": puppet.gender,
        "dob": puppet.bg_date_of_birth,
        "age": puppet.age,
        "star_sign": puppet.star_sign,
        "egn": puppet.egn,
        "address": puppet.address,
        "phone_number": puppet.phone_number,
        "credit_card": puppet._credit_card,
        "email": puppet.email,
        "username": puppet.username,
        "password": puppet.password,
        "website_domain": puppet.website_domain,
    }

    return jsonify(puppet_data)

if __name__ == '__main__':
    app.run(debug=True)
