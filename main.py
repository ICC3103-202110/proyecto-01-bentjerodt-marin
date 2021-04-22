
from game import Game
from menu import Menu

def main():
    game = Game()
    menu = Menu()
    tape = range(0,game.number_of_players)

    for i in tape:
        print()
        print(f"Player '{game.list_of_players[i].name}' is playing")
        option = menu.show_options_and_choose()
        
        if option == 1:
            game.list_of_players[i].coins+=1

        elif option == 2:
            pass

        elif option == 3:
            pass

        elif option == 4:
            pass

        elif option == 5:
            pass

        elif option == 6:
            pass
        
        elif option == 7:
            pass
        
        else:
            pass
        
        
    

    

main()