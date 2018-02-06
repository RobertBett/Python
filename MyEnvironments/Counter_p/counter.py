from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key="string"
@app.route('/')
def index():
	# session['counter'] == request.form['counter']
	# if "counter"not in session:
	#    session['counter']=0
	#    session['counter']+=1
	if session:
		session['counter']+=1
	else:
		session['counter']=0
	return render_template("counter2.html")

@app.route('/user', methods=['POST'])
def user():
	return redirect('/')
@app.route('/plus')
def plus():

	session['counter']+=1


	return redirect('/')
app.run(debug=True)
