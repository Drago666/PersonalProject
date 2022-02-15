from flask import Flask, render_template #allows a render of other codes

app = Flask(__name__)
#This is asking object "@" from flask to run "route"
#@app.route("/")
#def hello_world():
#    return "<p>Hello World</p>"

@app.route("/another")
def another_function():
    return "<p>This is a new page</p>"
@app.route("/contact")
def contact():
    return "<p>You are in the contact page</p>"
@app.route("/name")
def name():
    full="<p>my name is Ryon</p>"+contact()
    return full
@app.route("/<name>")
def New_Contact(name):
    return "Hello My name is "+name

@app.route("/")
def indexPage():
    return render_template('home.html')

@app.route("/example")
def examplePage():
    return render_template('example.html')

if __name__=="__main__":
    app.run(debug=True)