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
                turn = False

            elif option == 2:
                auxiliary_list = game.list_of_players[:]
                auxiliary_list.pop(i)
                counteraction = menu.ask_for_counteraction(auxiliary_list)
                
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
                auxiliary_list = game.list_of_players[:]
                auxiliary_list.pop(i)
                challenger = menu.ask_for_challenge(auxiliary_list)

                if challenger == False:
                    counteraction = menu.ask_for_counteraction(auxiliary_list)
                    if counteraction == False:
                        print()
                        print("Choose the player you wanto to steal coins")
                        print()
                        enemy = menu.select_enemy(game.list_of_players,i,game)
                        print()
                        print(f"Player '{enemy.name}', player '{game.list_of_players[i].name}' will steal your coins (max 2) ")
                        print()
                        if enemy.coins>=2:
                            enemy.coins-=2
                            game.list_of_players[i].coins+=2
                            turn = False
                        elif enemy.coins==1:
                            enemy.coins-=1
                            game.list_of_players[i].coins+=1
                            turn = False
                        else:
                            turn = False
                         
                    else:
                        auxiliary_list = game.list_of_players[:]
                        auxiliary_list.remove(counteraction)
                        challenger2 = menu.ask_for_challenge(auxiliary_list)
                        if challenger2 == False:
                            print()
                            print(f"No one challenge, player '{game.list_of_players[i].name}' your action could not be performed")
                            turn = False

                        else: 
                            if challenger2.challenge(counteraction,6) == False:
                                print()
                                print(f"Player '{counteraction.name}' didnt have 'Captain' or 'Ambassador', please player '{counteraction.name}' delate one card")
                                print()
                                counteraction.show_cards()
                                print()
                                game.lose_card(counteraction)
                                turn = False

                            else:
                                print()
                                print(f"Player '{counteraction.name}' had the 'Captain' or 'Ambassador")
                                print("Replaceing the card %... Done")
                                if "captain" in counteraction.cards:
                                    counteraction.cards.remove("Captain")
                                    deck.deck_of_cards.append("Captain")
                                elif "Ambassador" in counteraction.cards:
                                    counteraction.cards.remove("Ambassador")
                                    deck.deck_of_cards.append("Ambassador")

                                deck.shuffle()
                                counteraction.cards.append(deck.deck_of_cards[-1])
                                deck.deck_of_cards.pop()
                                turn = False
                else:
                    if challenger.challenge(game.list_of_players[i],66) == False:
                        print()
                        print(f"Player '{game.list_of_players[i].name}' didnt have 'Captain', please player '{game.list_of_players[i].name}' delate one card")
                        print()
                        challenger.show_cards()
                        print()
                        game.lose_card(challenger)
                        turn = False

                    else:
                        print()
                        print(f"Player '{game.list_of_players[i].name}' had the 'Captain'")
                        print("Replaceing the card %... Done")
                        game.list_of_players[i].cards.remove("Captain")
                        deck.deck_of_cards.append("Captain")
                        deck.shuffle()
                        game.list_of_players[i].cards.append(deck.deck_of_cards[-1])
                        deck.deck_of_cards.pop()
                        turn = False
                        print()
                        print("Choose the player you wanto to steal coins")
                        print()
                        enemy = menu.select_enemy(game.list_of_players,i,game)
                        print()
                        print(f"Player '{enemy.name}', player '{game.list_of_players[i].name}' will steal your coins (max 2) ")
                        print()
                        if enemy.coins>=2:
                            enemy.coins-=2
                            game.list_of_players[i].coins+=2
                            turn = False
                        elif enemy.coins==1:
                            enemy.coins-=1
                            game.list_of_players[i].coins+=1
                            turn = False
                        else:
                            turn = False


                
            
            elif option == 7:
                pass

            else:
                pass
    
main()
