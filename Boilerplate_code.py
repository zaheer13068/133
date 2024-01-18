#Importing flask module in the project
from flask import Flask

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/father")
@app.route("/mother")
@app.route("/friends")

def home():
    name = "Zaheer"
    age = "16"






#‘/’ URL is bound with first_flask function.
def first_flask():

    return "This is my first flask program"

< img src = "#" alt = "Reference your image present in the static folder" width = "200"/>

#run the application on local server
app.run()

