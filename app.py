import calculations
import sys
import json
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
sys.path.append('home/kietlai/Documents/Work/Winston-Grader/Calculations')


# Name: Kiet Lai, Nathan Story, and Jason (I DONT KNOW HOW TO SPELL YOUR LAST NAME.)

# todo: Add more routes and use redirects to change some things.
# todo: add in a home page, gpa, grade affect, save it to a server/database.
# todo: use jinja to create templates.
# todo: far future create a sign up page + login page.
# todo: later create a system to take notes that will be on a contender with others.
# todo: create a user saved page.
# REMOVE post and get from all other methods
# Open source???

messages = [{'classs': 'English',
            'percent': '100'},
            {'classs': 'Math',
            'percent': '79'}]
# data


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index-app.html')


@app.route('/gpa.html')
def gpa():
    return render_template('dropdown/Enter/gpa.html')


@app.route('/grader/', methods=('POST', 'GET'))
def grader():
    return render_template('Enter/dropdown/grader.html')


@app.route('/overall-grade/', methods=('POST', 'GET'))
def enter():
    return render_template('Enter/dropdown/ograde.html', messages=messages)


@app.route('/radar/')
def radar():
    return render_template('Enter/dropdown/radar.html')


@app.route('/contacts.html')
def contact():
    return render_template('contacts.html')


@app.route('/services.html')
def services():
    return render_template('/services')



#def gDebug(messages):
#    grades = input('what are your grades\n')
#    classname = input('what is your class name\n')
#    messages.append({'classs': classname, 'percent': grades})
#    again = input('again?\n')
#    if again == 'yes':
#        gDebug(messages)


#gDebug(messages)
