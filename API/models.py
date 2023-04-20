from . import db

class Cheese(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	strength = db.Column(db.String(255))
	animal = db.Column(db.String(255))
	region = db.Column(db.String(255))
	pairing = db.Column(db.String(255))
	details = db.Column(db.String(2055))
	link = db.Column(db.String(2055))
	#create table cheese(id integer primary key AUTOINCREMENT, name varchar(255),strength varchar(255),animal varchar(255),region varchar(255),pairing varchar(255),details varchar(2055),link varchar(2055)); 