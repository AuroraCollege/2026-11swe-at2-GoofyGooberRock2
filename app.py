from flask import Flask, render_template, request
from wumpus import HuntTheWumpus
from blackjack import game1
wumpus_game = HuntTheWumpus()
blackjack_game = game1()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wumpus', methods=['POST', 'GET'])
def wumpus():
    if request.method == 'POST':
        message = wumpus_game.play(request.form)
    else:
        message = wumpus_game.new_game()
    return render_template('wumpus.html', message=message, game=wumpus_game)

@app.route('/blackjack', methods=['POST', 'GET'])
def blackjack():
    return render_template('blackjack.html', game1=blackjack_game, dlh=blackjack_game.dlh)

if __name__ == "__main__":
    app.run()