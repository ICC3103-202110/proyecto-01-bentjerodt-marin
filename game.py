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
                self.number_of_players = int(input("Inseret number of players (3 or 4): ")) 

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

    def lose_card(self,player):
        while True: 
            try:
                select = int(input("Choose the card you want to drop: ")) 

            except ValueError:
                print(f"NUMBER MUST BETWEEN 1 AND {len(player.cards)}")
                continue

            if select<1 or select>len(player.cards):
                print(f"NUMBER MUST BETWEEN 1 AND {len(player.cards)}")
            
            else:
                break
<<<<<<< HEAD
        
        player.banished_cards.append (player.cards[select-1])
        player.cards.pop(select-1)
=======
        card = player.cards[select-1]
        player.banished_cards.append(card)
        player.cards.pop(select-1)
        return card
>>>>>>> 03a8df9d20894b6fbf0b34a24f21f835ae10df76

    def show_info(self):
        print("Global information")
        print()
        
        for i in range(self.number_of_players):
            txt = ""
            for j in self.list_of_players[i].banished_cards:
                txt += j + " "
            print(f"Player {i+1}: {self.list_of_players[i].name}   Coins: {self.list_of_players[i].coins}   Banished cards: {txt}")
  
