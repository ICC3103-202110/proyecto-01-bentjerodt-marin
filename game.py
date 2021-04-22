from players import Player
from cards import deck

class Game:

    def __init__(self):
        self.number_of_players = 0
        self.list_of_players = []
        
        self.generate_players()
        self.deal_cards()


    def ask_n_players(self):
        while True: 
            try:
                self.number_of_players = int(input("\nInseret number of players (3 or 4): ")) 

            except ValueError:
                print("NUMBER MUST BE 3 OR 4")
                continue

            if self.number_of_players>=5 or self.number_of_players<=2:
                print("NUMBER MUST BE 3 OR 4")
            
            else:
                break
        print()
        return self.number_of_players

    def generate_players(self):
        for i in range(self.ask_n_players()):
            name = input(f"Insert name player {i+1}: ")
            self.list_of_players.append(Player(name))

    def deal_cards(self):
        for i in range(self.number_of_players):
            self.list_of_players[i].cards.append(deck.deck_of_cards[-1])
            deck.deck_of_cards.pop()
            self.list_of_players[i].cards.append(deck.deck_of_cards[-1])
            deck.deck_of_cards.pop()






