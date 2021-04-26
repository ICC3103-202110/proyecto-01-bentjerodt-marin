import random

class Deck:

        

    def __init__(self):
        self.deck_of_cards=["Duke","Assassin","Captain","Ambassador","Countness"]*3
        self.shuffle()
        self.exchange = []
   
    element=0
    
    def shuffle(self):
        random.shuffle(self.deck_of_cards)
        return self.deck_of_cards

    def cards_exchange(self):
        self.exchange=[]
        x=1
        while x <= 2:
            element = random.randint(0,len(self.deck_of_cards))
            self.exchange.append(self.deck_of_cards[element-1])
            self.deck_of_cards.pop()
            x+=1
        return self.exchange

deck = Deck()
