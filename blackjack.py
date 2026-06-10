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
            return ['  ----------',
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
     
card1 = Card(deck= deck)
card2 = Card(deck= deck)
dealerhand = DealerHand(card1= card1, card2= card2)
dealerhand.display_hidden()
dealerhand.display()

class game1():
    def __init__ (self):
        self.dlh = dealerhand.display()
    
    def i (self):
        return self.dlh
    
