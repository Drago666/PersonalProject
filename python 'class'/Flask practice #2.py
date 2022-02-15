from flask import Flask, render_template, flash, redirect, url_for #allows a render of other codes
from form import RegistrationForm
app = Flask(__name__)
app.config['SECRET_KEY']="elatedgiant"


#list of dictionaries
posts = [
    {'title':"Title1",
     'author':"Ryon",
     'date':"Jan 3"
     },
    {'title': "Title2",
     'author': "Connor",
     'date':"Feb 6"
     }
]
@app.route("/first")
def showFirst():
    return render_template("first.html", posts=posts)
@app.route("/second")
def showSecond():
    return render_template("Second.html", posts=posts)
@app.route("/")
def BootstrapExample():
    return render_template("Bootstrap example.html")

# @app.route("/register", methods=['GET','POST'])
# def register():
#     form=RegistrationForm()
#     if form.validate_on_submit():
#         #flash(f'Account created for {form.username.data}!', 'success')
#         return redirect("showSecond")
#
#    return render_template("register.html", form=form)









if __name__=="__main__":
    app.run(debug=True)

#https://www.youtube.com/watch?v=xIgPMguqyws