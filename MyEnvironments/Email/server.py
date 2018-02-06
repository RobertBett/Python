from flask import Flask,request,redirect,render_template,sessions,flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'emails')
app.secret_key = "abcde12345"
@app.route('/')

def index():
	return render_template('index.html')


@app.route('/user',methods=['POST'])
def create():
	# add a friend to the database!
	
	query ="""INSERT INTO email_val(Email_info)VALUES(:Email_info)"""
	data = {
			'Email_info':request.form['Email_info']
			}
	check = mysql.query_db("SELECT email_val.Email_info FROM email_val")
	print check
	mysql.query_db(query,data)
	return redirect('/')
app.run(debug=True)
