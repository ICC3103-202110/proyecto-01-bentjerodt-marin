from game import Game
from menu import Menu
from cards import deck
import random
""" This game """
def main():
    print()
    print("WELCOME TO $ COUP $")
    print()

    game = Game()
    menu = Menu()
    
    ponderation = 30
    tape = game.list_of_players*ponderation
    for i in tape:
        actual_player = i
        print("______________________________________________________________")
        turn = True
        while turn:
            print()
            game.show_info()
            print()
            print(f"Player '{actual_player.name}' is playing")
            print()
            actual_player.show_cards()
            option = menu.show_options_and_choose()
            print()
            
            if option == 1:
                actual_player.incomes(game)
                input("Press any key to pass the turn: ")
                turn = False
                
            elif option == 2:
                actual_player.foreigne_aid(game,menu,deck)
                print()
                input("Press any key to pass the turn: ")
                turn = False

            elif option == 3:
                if actual_player.coins<7:
                    print("You dont have enough coins")
                    print()
                    input("Press any key to pass the turn: ")
                else:
                    actual_player.coup(game,menu)
                    print()
                    input("Press any key to pass the turn: ")
                    turn = False

            elif option == 4:
                actual_player.duke_tax(game,menu)
                print()
                input("Press any key to pass the turn: ")
                turn = False
                
            elif option == 5:
                if actual_player.coins<3:
                    print("You dont have enough coins")
                    print()
                    input("Press any key to pass the turn: ")
                else:
                    actual_player.assassin_assassinate(game,menu)
                    print()
                    input("Press any key to pass the turn: ")
                    turn = False

            elif option == 6:
                actual_player.captain_steal(game,menu)
                print()
                input("Press any key to pass the turn: ")
                turn = False

            elif option == 7:
                actual_player.ambassador_exchange(game,menu,deck)
                print()
                input("Press any key to pass the turn: ")
                turn = False    

            else: 
                for j in game.log:
                    print(j)
                print()
                print("ATTENTION: INCOMPLETED ACTION ")
                input("Press any key to continue: ")

        if len(tape) == 1:
            print()
            print(f"CONGRATULATIONS PLAYER '{i.name}, YOU WIN!'")
            break

        for i in game.list_of_players:
            if len(i.cards) == 0:
                game.list_of_players.remove(i)
                for j in tape:
                    if j == i:
                        tape.remove(i)  
        if len(tape) == ponderation:
            print()
            print(f"CONGRATULATIONS PLAYER '{actual_player.name}' YOU ARE THE $ WINNER $ ")
            print()
            break
main()