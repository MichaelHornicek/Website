from flask import Flask, render_template, request, redirect, url_for
from auth.login import LoginHandler
from auth.signup import SignupHandler

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    handler = LoginHandler()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if handler.handle_login(username, password):
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    handler = SignupHandler()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_type = request.form['user_type']
        if handler.handle_signup(username, password, user_type):
            return redirect(url_for('home'))
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    return "Welcome to the Dashboard!"

if __name__ == '__main__':
    app.run(debug=True)