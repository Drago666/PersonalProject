from flask import Flask, render_template #allows a render of other codes

app = Flask(__name__)

#list of dictionaries
posts = [
    {'first':"1",
     'second':"2",
     'third':"3"
     },
    {'first': "4",
     'second': "5",
     'third':"6"
     }
]
@app.route("/data")
def showData():
    return render_template("FlaskData.html", posts=posts)

if __name__=="__main__":
    app.run(debug=True)