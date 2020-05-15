import os
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'b56362ae8d7b62f9c23b5e8047259ba6'

posts = [
    {
        'author': 'Orla Madden',
        'title': 'Post One',
        'content': 'First post content',
        'date_posted': 'May 13, 2020'
    },
    {
        'author': 'Vivian Leigh',
        'title': 'Post Two',
        'content': 'Second post content',
        'date_posted': 'May 27, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", "5000")), debug=True)