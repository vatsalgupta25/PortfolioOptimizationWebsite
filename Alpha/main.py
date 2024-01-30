from flask import Flask, render_template, request
import re


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    user_input = request.form.get('user_input')
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_pattern, user_input):
        a = "verified"
    else:
        a = "Try again"
    return f"Status: {a}"


if __name__ == '__main__':
    app.run(debug=True)
