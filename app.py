from flask import Flask, render_template, request
from wumpus import HuntTheWumpus
from blackjack import game1
wumpus_game = HuntTheWumpus()
blackjack_game = game1()
blackjack_game.run()

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

hits = 0
@app.route('/blackjack', methods=['POST', 'GET'])
def blackjack():
    if request.method == 'POST':
        action = request.form['hit']

        if action == 'hit' and hits == 0:
            blackjack_game.plh = blackjack_game.hit1()
            hits += 1

    return render_template('blackjack.html', game1=blackjack_game, dlh=blackjack_game.dlh, 
                           dlhh=blackjack_game.dlhh, dealer_message=blackjack_game.dealer_message, 
                           plh=blackjack_game.plh, dltt=blackjack_game.dltt, pltt=blackjack_game.pltt)

if __name__ == "__main__":
    app.run()