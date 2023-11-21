# Name: Tessa Melli
# Date: 4/25/2023
# Course: CS493-400
# Assignment: Assignment 3 - Build a Restful API

# ***** BEGIN CITED CODE *****
# The following code is not wholly my own
# SOURCE: https://canvas.oregonstate.edu/courses/1915173/files/98341662?wrap=1
# Description: python app to provide functionality for Rest API. Modeled from
#   the Lodging App from the course content of Module 3.


# imports
from flask import Flask, request
import json
import random
import constants

# defining the app
app = Flask(__name__)

# routing for the base app URL
@app.route('/')
def index():
    return "Please navigate to /username_generator to use this API"\

# routing for boats
@app.route('/username_generator', methods=['POST'])
def boats_get_post():
    # POST method
    if request.method == 'POST':
        content = request.get_json()
        # error handling for missing attributes in the request
       
        if not ("email" in content):
            error_msg = {"Error":"The request object is missing an email address"}
            return(json.dumps(error_msg), 400)
        
        username_list = []
        options = {}

        user_email = content["email"]
        base_username = user_email[:user_email.index('@')]

        random.seed()

        # Random Generator 1: a 6-digit number
        rand_int = ''
        for i in range(7):
            rand_int += str(random.randint(0, 9))

        username_list.append(base_username + rand_int)

        # Random Generator 2: a verb-noun pairing
        rand_phrase = random.choice(constants.verb_list) + random.choice(constants.noun_list)

        username_list.append(base_username + rand_phrase)

        # Random Generator 3: an alphanumeric jumble
        rand_alpha_num = ''
        for i in range(8):
            if i == 0:
                first_char = random.choice(constants.alpha_num_list)
                if first_char.isalpha():
                    rand_alpha_num += first_char.upper()
                else:
                    rand_alpha_num += first_char
            else:
                rand_alpha_num += random.choice(constants.alpha_num_list)

        username_list.append(base_username + rand_alpha_num)

        options["usernames"] = username_list

        if ("source" in content):
            options["source"] = content["source"]

        return(json.dumps(options), 200)
    
    else:
        return 'Method not recognized'

        
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

# ***** END CITED CODE *****