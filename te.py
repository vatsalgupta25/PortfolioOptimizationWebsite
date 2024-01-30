from flask import Flask, render_template, request, render_template_string
from logic import data
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    user_input = request.form.get('user_input')
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_pattern, user_input):
        a = render_template('Details.html')
        return a
    else:
        a = render_template('index.html')
        return a
    return 0

@app.route('/logic', methods = ['POST'])
def logic():
    param1 = int(request.form['age'])
    a = data(param1,100)
    return render_template('logic.html', a=a)

if __name__ == '__main__':
    app.run(debug=True)
