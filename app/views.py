from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db
from .models import User, NytArticle

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]

    users = User.query.order_by('nickname desc').all()

    return render_template("index.html",
                           title='Home',
                           users=users,
                           posts=posts)
@app.route('/blah')
def blah():
    return "Hello, Worldd!"

@app.route('/nyt')
def nyt():
    stories =  NytArticle.query.order_by('fetch_date desc, rank limit 10').all():

    return render_template("nyt.html",
                           stories=stories)


