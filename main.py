from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about') 
def about(): 
    return render_template('about.html')

@app.route('/add_numbers', methods=['GET', 'POST']) 
def add_numbers(): 
    result = None 
    if request.method == 'POST': 
        number1 = request.form['number1'] 
        number2 = request.form['number2'] 
        result = int(number1) + int(number2) 
    return render_template('add_numbers.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
