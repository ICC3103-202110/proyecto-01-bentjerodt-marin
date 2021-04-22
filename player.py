class Player:

    def __init__(self,name,cards=["*","*"],coins=2):
        self.__name = name
        self.__cards = cards
        self.__coins = coins

    @property
    def name (self):
       return self.__name

    @property
    def cards (self):
        return self.__cards
    
    @cards.setter
    def cards (self, value):
        self.__cards = value

    @property
    def coins (self):
        return self.__coins
    
    @coins.setter
    def coins(self, value):
        if value < 0:
            self.__coins = 0
        else:
            self.__coins = value
    
