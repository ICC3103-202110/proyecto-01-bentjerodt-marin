from random import shuffle
from random import randint

class Cards:

    def __init__(self, cards_list,cards_hidden,Deal,players):
        self.cards_hidden = cards_hidden
        self.__cards_list = cards_list
        self.Deal = Deal
        self.players = players

    @property
    def cards_list(self):
        return self.__cards_list
    cards_hidden=[]
    cards_list = ["Duke" , "Assassin" , "Captain", "Contessa", "Ambassador","Duke" , "Assassin" , "Captain", "Contessa", "Ambassador", "Duke" , "Assassin" , "Captain", "Contessa", "Ambassador" ]
    for i in (cards_list):
        x="*"
        cards_hidden.append(x)
    shuffle(cards_list)
    

    def Deal(players,cards_list,cards_hidden):
        x=0
        for i in (players):
            c1=randint(0,(len(cards_list)-1))
            print(c1,"c1",x)
            card1=cards_list[c1]
            cards_list.pop(c1)
            cards_hidden.pop(c1)
            c2=randint(0,(len(cards_list)-1))
            print(c2,"c2",x)
            card2=cards_list[c2]
            cards_list.pop(c2)
            cards_hidden.pop(c2)
            players[x].cards=[card1,card2]
            print(players)
            x+=1
        print (cards_list)