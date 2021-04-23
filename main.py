from game import Game
from menu import Menu
from cards import deck
import random


def main():
    print()
    print("WELCOME TO $ COUP $")
    print()

    turno=[]
    game = Game()
    menu = Menu()
    tape = range(game.number_of_players)

    for i in game.list_of_players:
        i.show_cards()
        print()
    while True:
        for i in tape:
            print("______________________________________________________________")
            turn = True
            while turn:
                print()
                game.show_info()
                print()
                print(f"Player '{game.list_of_players[i].name}' is playing")
                print()
                game.list_of_players[i].show_cards()
                option = menu.show_options_and_choose()
                print()
                
                if option == 1:
                    game.list_of_players[i].coins+=1
                    msn=f"The '{game.list_of_players[i].name}' get 1 coin for Income "
                    turno.append(msn)
                    turn = False

                elif option == 2:
                    auxiliary_list = game.list_of_players[:]
                    auxiliary_list.pop(i)
                    counteraction = menu.ask_for_counteraction(auxiliary_list)
                    
                    if counteraction == False:
                        game.list_of_players[i].coins+=2
                        msn=f"The '{game.list_of_players[i].name}' get 2 coins for Foreign Aid "
                        turno.append(msn)
                        turn = False
                        
                    else:
                        print()
                        msn=f"Player '{counteraction.name}' is counterattacking player '{game.list_of_players[i].name}'"
                        print(f"Player '{counteraction.name}' is counterattacking player '{game.list_of_players[i].name}'")
                        turno.append(msn)
                        auxiliary_list = game.list_of_players[:]
                        auxiliary_list.remove(counteraction)
                        print()
                        challenger = menu.ask_for_challenge(auxiliary_list)

                        if challenger == False:
                            turn = False

                        else:
                            if challenger.challenge(counteraction,2) == False:
                                print()
                                msn=f"Player '{counteraction.name}' didnt have 'Duke', please player '{counteraction.name}' delate one card"
                                print(f"Player '{counteraction.name}' didnt have 'Duke', please player '{counteraction.name}' delate one card")
                                turno.append(msn)
                                print()
                                counteraction.show_cards()
                                print()
                                game.lose_card(counteraction)
                                turn = False

                            else:
                                print()
                                print(f"Player '{counteraction.name}' had the 'Duke'")
                                print("Replaceing the card %... Done")
                                counteraction.cards.remove("Duke")
                                deck.deck_of_cards.append("Duke")
                                deck.shuffle()
                                counteraction.cards.append(deck.deck_of_cards[-1])
                                deck.deck_of_cards.pop()
                                turn = False
                
                elif option == 3:
                    if game.list_of_players[i].coins<7:
                        print()
                        print("You dont have enough money, try another option")

                    else:
                        enemy = menu.select_enemy(game.list_of_players,i,game)
                        print()
                        print(f"Player '{enemy.name}', player '{game.list_of_players[i].name}' coups you")
                        print()
                        enemy.show_cards()
                        print()
                        game.lose_card(enemy)
                        turn = False

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