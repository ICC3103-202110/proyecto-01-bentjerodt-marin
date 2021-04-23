from game import Game

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
                print("NUMBER MUST BETWEEN 1 AND 7")
                continue

            if value > 7 or value < 1:
                print("NUMBER MUST BETWEEN 1 AND 7")
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
        print("  5)Assasinss-kill")
        print("  6)Captain-steal")
        print("  7)Ambassador-exchange")
        print()
        self.option=""
        return self.option

    def ask_for_counteraction(self,list_of_players):
        txt = input("Any player wants to counterattack? y/n: ")
        if  txt != str("y") and txt != str("n"):
            while txt != str("y") and txt != str("n"):
                txt = input("Any player wants to counterattack? y/n: ")

        if txt == "y":
            print()
            print("Which player wants to counterattack?")
            print()
            for i in range(len(list_of_players)):
                print(f"{i+1}) {list_of_players[i].name}")

            print()
            while True:
                try:
                    option = int(input("Choose a player: "))

                except ValueError:
                    print(f"NUMBER MUST BETWEEN 1 AND {len(list_of_players)}")
                    continue

                if option > len(list_of_players) or option < 1:
                    print(f"NUMBER MUST BETWEEN 1 AND {len(list_of_players)}")
                else:
                    break
            
            return list_of_players[option-1]

        elif txt == "n":
            return False

    def ask_for_challenge(self,list_of_players):
        txt = input("Any player wants to challenge? y/n: ")
        if  txt != str("y") and txt != str("n"):
            while txt != str("y") and txt != str("n"):
                txt = input("Any player wants to challenge? y/n: ")

        if txt == "y":
            print()
            print("Which player wants to challenge?")
            print()
            for i in range(len(list_of_players)):
                print(f"{i+1}) {list_of_players[i].name}")

            print()
            while True:
                try:
                    option = int(input("Choose a player: "))

                except ValueError:
                    print(f"NUMBER MUST BETWEEN 1 AND {len(list_of_players)}")
                    continue

                if option > len(list_of_players) or option < 1:
                    print(f"NUMBER MUST BETWEEN 1 AND {len(list_of_players)}")
                else:
                    break
            
            return list_of_players[option-1]

        elif txt == "n":
            return False

    def select_enemy(self,list_of_players,actual_player,machine):
        auxiliary_list = machine.list_of_players[:]
        auxiliary_list.pop(actual_player)

        for i in range(len(auxiliary_list)):
            print(f"{i+1}) {auxiliary_list[i].name}")

        print()
        while True:
            try:
                optioN= int(input("Select a player: "))

            except ValueError:
                print(f"NUMBER MUST BETWEEN 1 AND {len(auxiliary_list)}")
                continue

            if optioN > len(list_of_players) or optioN < 1:
                print(f"NUMBER MUST BETWEEN 1 AND {len(auxiliary_list)}")
            else:
                break

        return auxiliary_list[optioN-1]
