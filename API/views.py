from flask import Blueprint, jsonify, request
from . import db
from .models import Cheese
from flask_cors import CORS
import urllib.request, json 
main = Blueprint('main', __name__)

CORS(main, supports_credentials=True)


#works fine
#add_Cheese
@main.route('/add_Cheese', methods=['POST'])
def add_cheese():
	#print('test')
	Cheese_data = request.get_json()
	print(Cheese_data)
	new_cheese = Cheese(name=Cheese_data['name'],strength=Cheese_data['strength'],animal=Cheese_data['animal'],region=Cheese_data['region'],pairing=Cheese_data['pairing'],details=Cheese_data['details'],link=Cheese_data['link'])
	print(new_cheese)
	db.session.add(new_cheese)
	db.session.commit()

	return 'Done', 201

@main.route('/filter_Cheese', methods=['GET'])
def filter_cheese():
	Searchquery=db.session.query(Cheese).filter(Cheese.id >0)
	animal = request.args.get('animal') ;
	region = request.args.get('region') ;
	strength = request.args.get('strength') ;
	name = request.args.get('name') ;
	id= request.args.get('id') ;
	#Json object used to change variables on code end if needed
	Jsun={
		'animal':animal,
		'region':region,
		'strength':strength,
		'name':name,
		'id':id
	}
	
	if Jsun['animal']!=None:
		Searchquery=Searchquery.filter(Cheese.animal.like(Jsun['animal']))
	if Jsun['region']!=None:
		Searchquery=Searchquery.filter(Cheese.region.like(Jsun['region']))
	if Jsun['strength']!=None:
		Searchquery=Searchquery.filter(Cheese.strength.like(Jsun['strength']))
	if Jsun['name']!=None:
		Searchquery=Searchquery.filter(Cheese.name.like(Jsun['name']))
	if Jsun['id']!=None:
		Searchquery=Searchquery.filter(Cheese.id ==Jsun['id'])
	
	#Searchquery=db.session.query(Cheese).filter(Cheese.id >0)
	cheeses = []
	for Slice in Searchquery:
		#print(Slice)
		cheeses.append({'name' : Slice.name,'strength' : Slice.strength,'animal' : Slice.animal, 'region' : Slice.region, 'pairing' : Slice.pairing, 'details' : Slice.details, 'link' : Slice.link, 'id': Slice.id })

	return jsonify ({'cheeses': cheeses}),299
	#return 'Done', 201
	#return Return
@main.route('/cheese')
def cheeses():
	
	#list3=db.session.query(colum('name'))
	cheese_list = Cheese.query.all()
	#list2=Cheese.query.all()
	#print(result)
	print(cheese_list)
	cheeses = []

	for Slice in cheese_list:
		print(Slice)
		cheeses.append({'name' : Slice.name,'strength' : Slice.strength,'animal' : Slice.animal, 'region' : Slice.region, 'pairing' : Slice.pairing, 'details' : Slice.details, 'link' : Slice.link })

	return jsonify ({'cheeses': cheeses})


