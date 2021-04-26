class Player:

    def __init__(self,name):
        self.name = name
        self.cards = []
        self.banished_cards = []
        self.coins = 2

    def show_cards(self):
        print("YOUR CARDS: ")
        for i in range(len(self.cards)):
            print(f"{i+1}) {self.cards[i]}")

    def challenge(self,player_challenged,action):
        if action == 1:
            pass
<<<<<<< HEAD
=======

>>>>>>> 03a8df9d20894b6fbf0b34a24f21f835ae10df76
        elif action == 2:
            if "Duke" not in player_challenged.cards:
                return False
            else:
                return True

        elif action == 3:
            pass

        elif action == 4:
            if "Duke" not in player_challenged.cards:
                return False
            else:
                return True

        elif action == 5:
            if "Countness" not in player_challenged.cards:
                return False
            else:
                return True

        elif action == 6:
<<<<<<< HEAD
            pass
=======
            if ("Ambassador" not in player_challenged.cards) and ("Captain" not in player_challenged.cards):
                return False
            else:
                return True
        elif action == 66:
            if "Captain" not in player_challenged.cards:
                return False
            else:
                return True
>>>>>>> 03a8df9d20894b6fbf0b34a24f21f835ae10df76

        elif action == 7:
            pass

        else:
            pass



    
       
        
   