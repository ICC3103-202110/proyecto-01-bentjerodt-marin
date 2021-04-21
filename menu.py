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
                print("NUMBER MUST BE 1 or 7")
                continue

            if value > 7 or value < 1:
                print("NUMBER MUST BE 1 OR 7")
            else:
                break
        self.__option = value
        return self.__option
        
    def show_options_and_choose(self):
        print()
        print("GENERAL ACTIONS")
        print("  1)Incomes")
        print("  2)External help")
        print("  3)Coup")
        print("CHARACTER ACTIONS")
        print("  4)Duke-tax")
        print("  5)Assasinss-kill")
        print("  6)Captain-extorsionate")
        print("  7)Ambassador-change")
        print()
        self.option=""

    

    
menu = Menu()
menu.show_options_and_choose()
print(menu.option)

