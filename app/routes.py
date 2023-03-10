from flask import Flask                         #From the flask module import the Flask class.

app = Flask(__name__)                           #Create an instance of Flask into a variable called "app".
                                                #From this point forward, app is an "object".

@app.get("/")                                   #Flask specific decorator to create routes.
def about_me():                                 #View function. Functions mapped to routes are called
    me = {                                      #View functions.
        "first_name": "Brayan",                 #On line 8, we are creating a dictionary 
        "last_name": "Ornelas",
        "hobbies": "Gameplayer",
        "active": True
    }

    return me                                  #When we return a dictionary from a view function,
                                               #flask automatically converts it to JSON.