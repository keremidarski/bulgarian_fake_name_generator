from flask import Flask, render_template, request
from sock_puppet import SockPuppet

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    gender = request.form.get('gender', 'random')
    puppet = SockPuppet(gender)

    return render_template('index.html', puppet=puppet)

if __name__ == '__main__':
    app.run(debug=True)
