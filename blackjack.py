import random
deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
for card in deck:
    print(card)

class Card:
    def __init__ (self, deck):
        self.value = random.choice(deck)

    def display(self):
        
        if self.value != '10':
            return [' ----------',
            f'| {self.value}        |',
            '|          |',
            '|          |',
            '|          |',
            f'|        {self.value} |',
            ' ----------']
        if self.value == '10':
            return [' ----------',
            f'| {self.value}       |',
            '|          |',
            '|          |',
            '|          |',
            f'|        {self.value}|',
            ' ----------']

    
    def display_hidden(self):
        return ['  ----------',
        f'| ?        |',
        '|          |',
        '|          |',
        '|          |',
        f'|        ? |',
        '  ----------']


class DealerHand:
    def __init__ (self, card1, card2):
        self.card1 = card1
        self.card2 = card2

    def display_hidden(self):
        card1_lines = self.card1.display()
        card2_lines = self.card2.display_hidden()
        output = []
        for i in range(len(card1_lines)):
            output.append(card1_lines[i] + "  " + card2_lines[i])
        return "\n".join(output)

    def display(self):
        card1_lines = self.card1.display()
        card2_lines = self.card2.display()
        output = []
        output.append(card1_lines[0] + "   " + card2_lines[0])
        for i in range(1, 6):
            output.append(card1_lines[i] + "  " + card2_lines[i])
        output.append(card1_lines[6] + "   " + card2_lines[6])
        return "\n".join(output)
    
class PlayerHand():
    def __init__ (self, card1, card2, card3, card4, card5):
        self.card1 = card1
        self.card2 = card2
        self.card3 = card3
        self.card4 = card4
        self.card5 = card5

    def display(self):
        card1_lines = self.card1.display()
        card2_lines = self.card2.display()
        output = []
        output.append(card1_lines[0] + "   " + card2_lines[0])
        for i in range(1, 6):
            output.append(card1_lines[i] + "  " + card2_lines[i])
        output.append(card1_lines[6] + "   " + card2_lines[6])
        return "\n".join(output)

    def display1hit(self):
        card1_lines = self.card1.display()
        card2_lines = self.card2.display()
        card3_lines = self.card3.display()
        output = []
        output.append(card1_lines[0] + "   " + card2_lines[0] + "   " + card3_lines)
        for i in range(1, 6):
            output.append(card1_lines[i] + "  " + card2_lines[i] + "   " + card3_lines[i])
        output.append(card1_lines[6] + "   " + card2_lines[6] + "   " + card3_lines[6])
        return "\n".join(output)




class game1():
    def run(self):
        self.cards = [Card(deck) for _ in range(7)]
        self.dealerhand = DealerHand(self.cards[1], self.cards[2])
        self.dlh = self.dealerhand.display()
        self.dlhh = self.dealerhand.display_hidden()
        self.dealer_message = "The dealer's cards are out and it is your action..."
        self.player = PlayerHand(self.cards[2], self.cards[3], self.cards[4], self.cards[5], self.cards[6])
        self.plh = self.player.display()
        return self.dealer_message, self.dlh, self.dlhh, self.plh
        
    
    def hit1(self):
        self.player.display1hit()
    
