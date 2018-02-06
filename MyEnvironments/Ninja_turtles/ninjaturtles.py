from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
  return render_template("ninja1st.html")

@app.route('/ninja')
def ninjas():
  return render_template("ninja2nd.html")

@app.route('/ninja/blue')
def blue():
  return render_template('blue.html')

@app.route('/ninja/red')
def red():
  return render_template("red.html")

@app.route('/ninja/purple')
def purple():
  return render_template("purple.html")

@app.route('/ninja/orange')
def orange():
  return render_template("orange.html")
@app.route('/ninja/notapril')
def notapril():
  return render_template("notapril.html")
app.run(debug=True)