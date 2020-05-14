import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

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

app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", "5000")), debug=True) 