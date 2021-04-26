from game import Game
from menu import Menu
from cards import deck
import random

def main():
    print()
    print("WELCOME TO $ COUP $")
    print()

    game = Game()
    menu = Menu()
    tape = range(game.number_of_players)
    
    for i in game.list_of_players:
        i.show_cards()
        print()
    while True:
        game_turn=[] 
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
                    msn = f"{game.list_of_players[i].name} gets 1 coin for Income."
                    game_turn.append(msn)
                    game.list_of_players[i].coins+=1
                    turn = False

                elif option == 2:
                    auxiliary_list = game.list_of_players[:]
                    auxiliary_list.pop(i)
                    counteraction = menu.ask_for_counteraction(auxiliary_list)
                    msn = f"{game.list_of_players[i].name} get 3 coins for Foreign Aid."
                    game_turn.append(msn)
                    if counteraction == False:
                        game.list_of_players[i].coins+=2
                        turn = False

                    else:
                        print()
                        print(f"Player '{counteraction.name}' is counterattacking player '{game.list_of_players[i].name}'")
                        auxiliary_list = game.list_of_players[:]
                        auxiliary_list.remove(counteraction)
                        print()
                        challenger = menu.ask_for_challenge(auxiliary_list)
                        msn = f"Player '{counteraction.name}' is counterattacking player '{game.list_of_players[i].name}'"
                        game_turn.append(msn)
                        if challenger == False:
                            turn = False

                        else:
                            if challenger.challenge(counteraction,2) == False:
                                print()
                                print(f"Player '{counteraction.name}' didnt have 'Duke', please player '{counteraction.name}' delate one card")
                                print()
                                counteraction.show_cards()
                                print()
                                game.lose_card(counteraction)
                                msn = f"Player '{counteraction.name}' lose influence in the challenge"
                                game_turn.append(msn)
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
                        print("Choose the player you want to coup")
                        print()
                        enemy = menu.select_enemy(game.list_of_players,i,game)
                        print()
                        print(f"Player '{enemy.name}', player '{game.list_of_players[i].name}' coups you")
                        print()
                        enemy.show_cards()
                        print()
                        game.lose_card(enemy)
                        msn = f" Player {game.list_of_players[i].name} take a coup '{enemy.name}' "
                        game_turn.append(msn)
                        msn = f" Player {enemy.name} lose influence in the coup "
                        game_turn.append(msn)
                        turn = False

                elif option == 4:
                    auxiliary_list = game.list_of_players[:]
                    auxiliary_list.pop(i)
                    challenger = menu.ask_for_challenge(auxiliary_list)

                    if challenger == False:
                        game.list_of_players[i].coins += 3
                        turn = False

                    else:
                        if challenger.challenge(game.list_of_players[i],4) == False:
                            print()
                            print(f"Player '{game.list_of_players[i].name}' didnt have 'Duke', please player '{game.list_of_players[i].name}' delate one card")
                            print()
                            game.list_of_players[i].show_cards()
                            print()
                            game.lose_card(game.list_of_players[i])
                            turn = False

                        else:
                            print()
                            print(f"Player '{game.list_of_players[i].name}' had the 'Duke'")
                            print("Replaceing the card %... Done")
                            game.list_of_players[i].cards.remove("Duke")
                            deck.deck_of_cards.append("Duke")
                            deck.shuffle()
                            game.list_of_players[i].cards.append(deck.deck_of_cards[-1])
                            deck.deck_of_cards.pop()
                            turn = False

                elif option == 5:
                    if game.list_of_players[i].coins<3:
                        print()
                        print("You dont have enough money, try another option")

                    else:
                        game.list_of_players[i].coins-=3
                        auxiliary_list = game.list_of_players[:]
                        auxiliary_list.pop(i)
                        counteraction = menu.ask_for_counteraction(auxiliary_list)

                        if counteraction == False:
                            print()
                            print("Choose the player you wanto to assassinate influence")
                            print()
                            enemy = menu.select_enemy(game.list_of_players,i,game)
                            print()
                            print(f"Player '{enemy.name}', player '{game.list_of_players[i].name}' wants to assassinate some of your influences")
                            print()
                            enemy.show_cards()
                            print()
                            game.lose_card(enemy)
                            msn = f" Player {game.list_of_players[i].name} use the Assassination action against '{enemy.name}' "
                            game_turn.append(msn)
                            turn = False

                        else:
                            print()
                            print(f"Player '{counteraction.name}' is counterattacking player '{game.list_of_players[i].name}'")
                            auxiliary_list = game.list_of_players[:]
                            auxiliary_list.remove(counteraction)
                            print()
                            challenger = menu.ask_for_challenge(auxiliary_list)

                            if challenger == False:
                                print()
                                print(f"No one challenge player '{counteraction.name}', player '{game.list_of_players[i].name}' your action could not be performed")
                                turn = False

                            else:
                                if challenger.challenge(counteraction,5) == False:
                                    print()
                                    print(f"Player '{counteraction.name}' didnt have 'Countness', please player '{counteraction.name}' delate one card")
                                    print()
                                    counteraction.show_cards()
                                    print()
                                    game.lose_card(counteraction)
                                    turn = False

                                else:
                                    print()
                                    print(f"Player '{counteraction.name}' had the 'Countness'")
                                    print("Replaceing the card %... Done")
                                    counteraction.cards.remove("Countness")
                                    deck.deck_of_cards.append("Countness")
                                    deck.shuffle()
                                    counteraction.cards.append(deck.deck_of_cards[-1])
                                    deck.deck_of_cards.pop()
                                    turn = False



                elif option == 6:
                    print(f"Select which player to extort: ")
                    auxiliary_list = game.list_of_players[:]
                    auxiliary_list.pop(i)
                    enemy = menu.select_enemy(game.list_of_players,i,game)
                    challenger = menu.ask_for_challenge(auxiliary_list)
                    
                    if challenger == False:
                        if enemy.coins < 2:
                            game.list_of_players[i].coins+=1
                            enemy.coins-=1
                            msn = f" Player {game.list_of_players[i].name} extorted {enemy.name} for 1 coins "
                            game_turn.append(msn)
                        elif enemy.coins >= 2:
                            game.list_of_players[i].coins += 2
                            enemy.coins-=2
                            msn = f" Player {game.list_of_players[i].name} extorted {enemy.name} for 2 coins "
                            game_turn.append(msn)
                        turn = False
                    
                
                elif option == 7:
                    cartas=[]
                    print()
                    cartas=deck.cards_exchange()
                    for p in range(len(game.list_of_players[i].cards)):
                        cartas.append(game.list_of_players[i].cards[p])
                    print("DECK CARDS - YOUR CARDS ")
                    for c in range(len(cartas)):
                        print(f"{c+1}) {cartas[c]}")
                    if len(game.list_of_players[i].cards)==1:
                        print("\nSelect 1 of the 3 cards: ")
                        elect=int(input())
                        camb=cartas[elect-1]
                        game.list_of_players[i].cards[0]=camb
                        cartas.pop()
                        for u in range(len(cartas)):
                            deck.deck_of_cards.append(cartas[u])
                        deck.shuffle()
                        msn = f" Player {game.list_of_players[i].name} performs card exchange "
                        game_turn.append(msn)
                        turn = False   

                    elif len(game.list_of_players[i].cards)==2:
                        print("\nSelect 2 of the 4 cards: \n")
                        c1=int(input("Select the first card: "))
                        camb=cartas[c1-1]
                        game.list_of_players[i].cards[0]=camb
                        cartas.pop()
                        c2=int(input("Select the second card: "))
                        camb=cartas[c2-1]
                        game.list_of_players[i].cards[1]=camb
                        cartas.pop()
                        for u in range(len(cartas)):
                            deck.deck_of_cards.append(cartas[u])
                        deck.shuffle()
                        msn = f" Player {game.list_of_players[i].name} performs card exchange "
                        game_turn.append(msn)
                        turn = False

                else:
                    pass
        print ("\n-------- SHIFT LOG ---------")
        for i in range(len(game_turn)):
            print(f"'{i}'. {game_turn[i]}")
        print()
        
main()


