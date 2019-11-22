try:
	import pymongo, sys
	from pymongo import MongoClient
except: 
	print("install pymongo")
	sys.exit(2)

def Connect(Client,DbStr,CollectionStr):
	global collection
	try:
		client = MongoClient(Client)
		print("Client connected")
	except:
		print("Connection error. Is the server running? MongoDB Functions wont work without a server.")
	try:
		db1 = client[CollectionStr]
		collection = db1[DbStr]
		print(collection)
	except:
		print("db or collection doesnt exist")
	
	
def Create(record): 
	collection.insert_one(record)
	
def Read(record, findAll):
	if findAll == True:
		return collection.find(record)
	else:
		return collection.find_one(record)

def Update(record,newRecord, updateAll):
	if updateAll == True:
		collection.update(record,newRecord)
	else:
		collection.update_one(record,newRecord)

def Delete(Record,deleteMany):
	if deleteMany == True:
		collection.delete_many(Record)
	else: 
		collection.delete_one(Record)
