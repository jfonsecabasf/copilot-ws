import flask
from flask import request, jsonify
from main import determine_winner, play_game
import random

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Rock, Paper, Scissors, Lizard, Spock!</h1>
<p>A prototype API for playing Rock, Paper, Scissors, Lizard, Spock.</p>'''


@app.route('/api/v1/playgame', methods=['GET'])
def api_playgame():
    # create a list of options
    options = ["rock", "paper", "scissors", "lizard", "spock"]

    # get the user's choice from the query string
    user_choice = request.args.get('user_choice')

    # create a variable to store the computer's choice
    computer_choice = random.choice(options)

    # determine the winner
    result = determine_winner(user_choice, computer_choice)

    # return the results
    return jsonify(result)


@app.route('/api/v1/playgame', methods=['POST'])
def api_playgame_post():
    # create a list of options
    options = ["rock", "paper", "scissors", "lizard", "spock"]

    # get the user's choice from the query string
    user_choice = request.json['user_choice']

    # create a variable to store the computer's choice
    computer_choice = random.choice(options)

    # determine the winner
    result = determine_winner(user_choice, computer_choice)

    # return the results
    return jsonify(result)


app.run()
