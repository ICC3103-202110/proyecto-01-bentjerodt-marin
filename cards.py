import random

<<<<<<< HEAD
=======

>>>>>>> 94593e264f4ab4be9946da2691367f19087c6eb5
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
deck = Deck()
>>>>>>> 94593e264f4ab4be9946da2691367f19087c6eb5
