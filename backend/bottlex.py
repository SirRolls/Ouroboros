from flask import Flask, render_template, request,redirect, url_for
import mongoLib

db = mongoLib

#TODO: Rewrite SQLlite3 CRUD, import CassandraCRUD Lib, test cassandraLib, Further Reddis Lib, Add Cinvert queries lib and display

app = Flask(__name__)

###############################################################
#Structure                                                    #
#@app,route: If the browaer asks for this url, what do we do? #
#def (name): What the route is doing.                         #
###############################################################

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/ConvertQueries.html')
def ConvertQueries():
	return render_template('ConvertQueries.html')
@app.route('/AlarmClock.html')
def AlarmClock():
	return render_template('AlarmClock.html')
@app.route('/CreateQueries.html')
def CreateQueries():
	return render_template('CreateQueries.html')
@app.route('/MongoDBCreate.html', methods=["GET","POST"])
def MongoDBCreate():
	#If the request frim the browser is post, we know a user has entered something
	
	if request.method == "POST":
		#debug, remove in final
		print(request.form['element'])
		#Connect to the db. In the future, this will also come from the user (Collection and db string)
		db.Connect('mongodb://localhost:27017','test','test')
		#If the form for element is empty, we assume that they wrote a complex query
		#With future versions, it may be better to have a try here with an error page
		if request.form['element'] != '':
			q = '{'+ request.form['element'] + ':' + '/"' + request.form['table'] + '/"' + '}'
		else:
			q = request.form['complex']
		#debug, remove in final
		print(q)
		#Running the thing and getting the results. Future version allow user input for finding one or many
		global results = db.Read(q,True)
		#Debug solution for displaying results 0, will redirect to results page with results run through a parser
		print(results)
		return redirect(url_for(results.html))
	else:
		#If the request is a get or some other method, we just give them the og page
		return render_template('MongoDBCreate.html')
@app.route('/Results.html')
def Results():
	#Results template will use global vars to display last results and wipe the var once we;re done
	return render_template('Results.html', result=results)
	
@app.route('/CassandraCreate.html')
def CassandraCreate():
	return render_template('CassandraCreate.html')	
	if request.method == "POST":
		print("placeholder for cassandra lib")
	else:
		print("we got a get yo")
@app.route('/ReddisCreate.html')
def ReddisCreate():
	return render_template('ReddisCreate.html')
		
@app.route('/SQLCreate.html')
def SQLCreate():
	#OLD REWRITE NEEDED, Code Deleted
	return render_template('SQLCreate.html')

	
@app.route('/Neo4jCreate.html')
def Neo4jCreate():
	#Dont know where to start here. Custom Lib?
	return render_template('Neo4j.html')

@app.route('/SwitchTo.html')
def SwitchTo():
	return render_template('SwitchTo.html')	

@app.route('/index.html')	
def indexRedirect():
	#just a redirect to home for results
	return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
