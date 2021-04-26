from players import Player
from cards import deck

class Game:
    
    def __init__(self):
        self.number_of_players = 0
        self.list_of_players = []
    
        self.generate_players()
        self.deal_cards()
        self.copy_of_list = self.list_of_players[:]

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
                print(f"NUMBER MUST BE BETWEEN 1 AND {len(player.cards)}")
                continue

            if select<1 or select>len(player.cards):
                print(f"NUMBER MUST BE BETWEEN 1 AND {len(player.cards)}")
            
            else:
                break
        card = player.cards[select-1]
        player.banished_cards.append(card)
        player.cards.pop(select-1)
        return card

    def show_info(self):
        print("Global information")
        print()
        for i in range(len(self.copy_of_list)):
            txt = ""
            
            for j in self.copy_of_list[i].banished_cards:
                txt += j + " "
            print(f"Player {i+1}: {self.copy_of_list[i].name}   Coins: {self.copy_of_list[i].coins}   Actual cards: {len(self.copy_of_list[i].cards)}   Banished cards: {txt}")
    
    def other_players(self,actual_player):
        auxiliary_list = self.list_of_players[:]
        auxiliary_list.remove(actual_player)
        return auxiliary_list


    def challenge(self,challenger,challenged,card): #was player challenged playing clean?
        print()
        print(f"Player '{challenger.name}' is challenging player '{challenged.name}'")
        if card not in challenged.cards:
            print()
            print(f"Player '{challenged.name}' didnt have the '{card}', player '{challenged.name}' delate one card")
            print()
            challenged.show_cards()
            print()
            self.lose_card(challenged)
            return False
        else:
            print()
            print(f"Player '{challenged.name}' had the '{card}', player '{challenger.name}' delate one card")
            print()
            challenger.show_cards()
            print()
            self.lose_card(challenger)
            print()
            print(f"Replaceing the card of player '{challenged.name}' %... Done")
            challenged.cards.remove(card)
            deck.deck_of_cards.append(card)
            deck.shuffle()
            challenged.cards.append(deck.deck_of_cards[-1])
            deck.deck_of_cards.pop()
            return True
    
    def challenge_for_2_cards(self,challenger,challenged,card1,card2):
        print()
        if card1 not in challenged.cards and card2 not in challenged.cards:
            print()
            print(f"Player '{challenged.name}' didnt have the '{card1}' or '{card2}', player '{challenged.name}' delate one card")
            print()
            challenged.show_cards()
            print()
            self.lose_card(challenged)
            return False
        else:
            print()
            print(f"Player '{challenged.name}' had the '{card1}' or '{card2}', player '{challenger.name}' delate one card")
            print()
            challenger.show_cards()
            print()
            self.lose_card(challenger)
            print()
            if card1 in challenged.cards and card2 not in challenged.cards:
                print(f"Replaceing the card of player '{challenged.name}' %... Done")
                challenged.cards.remove(card1)
                deck.deck_of_cards.append(card1)
                deck.shuffle()
                challenged.cards.append(deck.deck_of_cards[-1])
                deck.deck_of_cards.pop()
                return True
            
            elif card1 not in challenged.cards and card2 in challenged.cards:
                print(f"Replaceing the card of player '{challenged.name}' %... Done")
                challenged.cards.remove(card2)
                deck.deck_of_cards.append(card2)
                deck.shuffle()
                challenged.cards.append(deck.deck_of_cards[-1])
                deck.deck_of_cards.pop()
                return True

            else:
                card = self.lose_card(challenged)
                while card != "Ambassador" or card != "Captain":
                    challenged.cards.append(card)
                    print()
                    print("Must select the 'Ambassador' or 'Captain'")
                    card = self.lose_card(challenged)
                    challenged.banished_cards.pop()
                challenged.banished_cards.pop()
                deck.deck_of_cards.append(card)
                deck.shuffle()
                challenged.cards.append(deck.deck_of_cards[-1])
                deck.deck_of_cards.pop()
                return True

    
        


    