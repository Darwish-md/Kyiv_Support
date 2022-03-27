#pylint: disable=no-member
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flaskapp import db

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

# to define the two functions of adding or deleting a record for the three models

class Record():
    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Donation(Record, db.Model):
    __tablename__ = 'Donation'
    donor_id = db.Column(db.Integer, db.ForeignKey('Donor.id'), primary_key=True)
    volunteer_id = db.Column(db.Integer, db.ForeignKey('Volunteer.id'), nullable=True)
    genre = db.Column(db.String(120))
    pickup_time = db.Column(db.DateTime)
    pickup_address = db.Column(db.String(120))
    donor = db.relationship("Donor", back_populates="volunteers")
    volunteer = db.relationship("Volunteer", back_populates="donors")
    
class Volunteer(Record, db.Model):
    __tablename__ = 'Volunteer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120), unique=True)
    facebook_link = db.Column(db.String(120))
    donors = db.relationship("Donation", back_populates="volunteer")
    credentials = db.relationship("Credentials", backref="Volunteer")

class Donor(Record, db.Model):
    __tablename__ = 'Donor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120), unique=True)
    facebook_link = db.Column(db.String(120))
    volunteers = db.relationship("Donation", back_populates="donor")
    credentials = db.relationship("Credentials", backref="Donor")
    accommodation = db.relationship("Accommodation", backref="Donor")
    
    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.city}')"
    
class Credentials(Record, db.Model):
    _tablename__ = 'Credentials'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    volunteer_id = db.Column(db.Integer, db.ForeignKey('Volunteer.id'))
    donor_id = db.Column(db.Integer, db.ForeignKey('Donor.id'))

class Accommodation(Record, db.Model):
    _tablename__ = 'Accommodation'
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    address = db.Column(db.String(120))
    donor_id = db.Column(db.Integer, db.ForeignKey('Donor.id'))
    
    