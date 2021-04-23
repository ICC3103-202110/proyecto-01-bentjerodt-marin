class Player:

    def __init__(self,name):
        self.name = name
        self.cards = []
        self.banished_cards = []
        self.coins = 2

    def show_cards(self):
        print("Cards: ")
        for i in self.cards:
            print(f"-{i}")
   