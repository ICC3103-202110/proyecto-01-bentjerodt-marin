class Menu:

    def __init__(self):
        self.__option = ""

    @property
    def option(self):
        return self.__option

    @option.setter
    def option(self,value):
        while True:
            try:
                value = int(input("Choose an option: "))

            except ValueError:
                print("NUMBER MUST BE BETWEEN 1 AND 8")
                continue

            if value > 8 or value < 1:
                print("NUMBER MUST BE BETWEEN 1 AND 8")
            else:
                break
        self.__option = value
        return self.__option
        
    def show_options_and_choose(self):
        print()
        print("GENERAL ACTIONS")
        print("  1)Incomes")
        print("  2)Foreigne aid")
        print("  3)Coup")
        print("CHARACTER ACTIONS")
        print("  4)Duke-tax")
        print("  5)Assassin-assassinate")
        print("  6)Captain-steal")
        print("  7)Ambassador-exchange")
        print("EXTRA ACTION")
        print("  8)Log")
        print()
        self.option=""
        return self.option

    def ask_for(self,list_of_players,action):
        txt = input(f"Any player wants to {action}? y/n: ")
        if  txt != str("y") and txt != str("n"):
            while txt != str("y") and txt != str("n"):
                txt = input(f"Any player wants to {action}? y/n: ")

        if txt == "y":
            print()
            print(f"Which player wants to {action}?")
            print()
            for i in range(len(list_of_players)):
                print(f"{i+1}) {list_of_players[i].name}")

            print()
            while True:
                try:
                    optioN = int(input("Choose a player: "))

                except ValueError:
                    print(f"NUMBER MUST BE BETWEEN 1 AND {len(list_of_players)}")
                    continue

                if optioN > len(list_of_players) or optioN < 1:
                    print(f"NUMBER MUST BE BETWEEN 1 AND {len(list_of_players)}")
                else:
                    break
            
            return list_of_players[optioN-1]

        elif txt == "n":
            return False

    def select_enemy(self,list_of_players):

        for i in range(len(list_of_players)):
            print(f"{i+1}) {list_of_players[i].name}")

        print()
        while True:
            try:
                optioN= int(input("Select a player: "))

            except ValueError:
                print(f"NUMBER MUST BETWEEN 1 AND {len(list_of_players)}")
                continue

            if optioN > len(list_of_players) or optioN < 1:
                print(f"NUMBER MUST BETWEEN 1 AND {len(list_of_players)}")
            else:
                break

        return list_of_players[optioN-1]