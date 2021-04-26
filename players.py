class Player:

    def __init__(self,name):
        self.name = name
        self.cards = []
        self.banished_cards = []
        self.coins = 2

    def show_cards(self):
        print("YOUR CARDS: ")
        if len(self.cards)==1:
            print(f"{1}) {self.cards[0]}")
        elif len(self.cards)==2:
            for i in range(len(self.cards)):
                print(f"{i+1}) {self.cards[i]}")
        elif len(self.cards)==0:
            print("YOU LOST")
        

    def challenge(self,player_challenged,action):
        if action == 1:
            pass
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
            pass

        elif action == 7:
            pass

        else:
            pass



    
       
        
   