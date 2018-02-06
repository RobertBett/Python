from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
  return render_template("index2.html")
@app.route("/process", methods=['POST'])
def process_form():
    # print request.form

    return render_template('ninja.html',name=request.form['name'],location=request.form['location'],language=request.form['language'])
app.run(debug=True)


 

