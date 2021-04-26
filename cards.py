import random

class Deck:

    def __init__(self):
        self.deck_of_cards=["Duke","Assassin","Captain","Ambassador","Countness"]*3
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck_of_cards)
        return self.deck_of_cards

deck = Deck()
<<<<<<< HEAD
=======


>>>>>>> d1d6145ad200afd33fc97f92200b1a04ca174af8
