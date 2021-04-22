
from game import Game
from menu import Menu

def main():
    game = Game()
    menu = Menu()
    tape = range(0,game.number_of_players)
    cardshidden = ["*","*"]
    def Show_players():
        print("\n          Players:         ")
        print ("Number - Name - Coins - Cards")
        for (i, _) in enumerate(game.list_of_players):
            print(f"{i+1}: {game.list_of_players[i].name} {game.list_of_players[i].coins} {cardshidden} ")
    for i in tape:
        print()
        Show_players()
        print(f"\nPlayer '{game.list_of_players[i].name}' is playing")
        option = menu.show_options_and_choose()
        
        if option == 1:
            game.list_of_players[i].coins+=1
            print("opcion1")
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

        elif option == 8:
            pass

        elif option == 9:
            pass

        elif option == 10:
            
            pass

        else:
            pass
        
        
    

    

main()