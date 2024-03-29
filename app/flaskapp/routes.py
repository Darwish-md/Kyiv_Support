#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
# pylint: disable=no-member  
# pylint: disable=import-error
from crypt import methods
import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
import logging, datetime
from flask_wtf import Form
import sys
from flaskapp import app
from flaskapp.forms import RegistrationForm, LoginForm
from flaskapp.models import Accommodation, db, Record, Volunteer, Donor, Donation

db.create_all()
db.session.commit()

#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#


def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format)

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  render_template('templates/index.html') 

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('register'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/donation_dashboard', methods=["GET"])
def donation_dashboard():
    records = Donation.query.all()
    return render_template('templates/donation_cards.html', donations=records)

    """engine = create_engine('sqlite:///app.db')
    connection=engine.connect()
    result_set = connection.execute('SELECT * FROM Donor;')
    return array"""


@app.route('/accommodation_dashboard', methods=["GET"])
def accommodation_dashboard():
    records = Accommodation.query.all()
    return render_template('templates/accommodation_cards.html', accommodations =records)





    

    