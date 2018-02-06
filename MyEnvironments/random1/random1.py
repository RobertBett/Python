from flask import Flask, render_template, request, session
import random
app = Flask(__name__)
app.secret_key="string"
@app.route('/')
def index():
	session['randnum']=random.randrange(1,1001)
	print session['randnum']
	return render_template('random1.html')
	
@app.route('/user',methods=['POST'])
def user():
	# print type(request.form['usernum'])
	usernum=int(request.form['usernum'])

	if usernum == session['randnum']:
		return render_template('correct.html')
		# return redirect('/')
	if usernum > session['randnum']:
		return render_template('high.html')
		# return redirect('/')
	if usernum < session['randnum']:
		return render_template('low.html')
		# return redirect('/')

app.run(debug=True)