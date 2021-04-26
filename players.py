class Player:

    def __init__(self,name):
        self.name = name
        self.cards = []
        self.banished_cards = []
        self.coins = 100

    def show_cards(self):
        print("YOUR CARDS: ")
        for i in range(len(self.cards)):
            print(f"{i+1}) {self.cards[i]}")

    #============================={GENERAL ACTIONS}=============================#
    def incomes(self,game):
        self.coins+=1
        game.log.append(f"-'{self.name}' gets 1 coin for incomes")
        

    def foreigne_aid(self,game,menu,deck):
        game.log.append(f"-'{self.name}' plays 'Foreigne_aid'")
        attacker = menu.ask_for(game.other_players(self),"counterattack") 
        if attacker == False:
            game.log.append(f"-No one counterattack the play of '{self.name}'")
            self.coins+=2
        else:
            game.log.append(f"-'{attacker.name}' counterattacks to '{self.name} respect to the action 'foreigne aid'")
            print()
            print(f"Player '{attacker.name}' is counterattacking player '{self.name}' with the 'Duke'")
            print()
            challenger = menu.ask_for(game.other_players(attacker),"challenge")
            if challenger == False:
                game.log.append(f"-No ones challenge the counterattack of '{attacker.name}'")
                pass
            else:
                challenge = game.challenge(challenger,attacker,"Duke")
                if challenge == False:
                    game.log.append(f"-'{challenger.name}' have the 'Duke' and wins the challenge against the counteratatck of '{attacker.name}', player '{self.name}' gets 2 coins")
                    self.coins+=2
                else:
                    game.log.append(f"-'{challenger.name}' didnt have the 'Duke' and lose the challenge against the counteratatck of '{attacker.name}', player '{self.name}' doesnt gets coins")
                    pass
                
    def coup(self,game,menu):
        self.coins-=7
        print("Choose the player you want to coup")
        print()
        enemy = menu.select_enemy(game.other_players(self))
        print()
        print(f"Player '{enemy.name}', player '{self.name}' coups you")
        print()
        enemy.show_cards()
        print()
        card = game.lose_card(enemy)
        game.log.append(f"-'{self.name}' 'Coups' '{enemy.name}' and he lose the '{card}'")

    #============================={CHARACTER ACTIONS}=============================#
    def duke_tax(self,game,menu):
        game.log.append(f"-'{self.name}' plays 'Duke tax'")
        challenger = menu.ask_for(game.other_players(self),"challenge")
        if challenger == False:
            game.log.append(f"-No one challenge the play of '{self.name}', gets 3 coins")
            self.coins+=3
            
        else:
            challenge = game.challenge(challenger,self,"Duke")
            if challenge == False:
                game.log.append(f"-'{challenge.name}' have the 'Duke' and wins the challenge agains the action of '{self.name}', player '{self.name}' doesnt gets coins")
                pass
            else:
                (f"-'{challenge.name}' didnt have the 'Duke' and lose the challenge agains the action of '{self.name}', player '{self.name}' gets 3 coins")
                self.coins+=3

    def assassin_assassinate(self,game,menu):
        challenger = menu.ask_for(game.other_players(self),"challenge")
        game.log.append(f"-'{self.name}' plays the 'Assassin'")
        if challenger == False:
            game.log.append(f"-No one challenge the play of'{self.name}'")
            attacker = menu.ask_for(game.other_players(self),"counterattack")
            if attacker == False:
                self.coins-=3
                print()
                print("Choose the player you wanto to assassinate influence")
                print()
                enemy = menu.select_enemy(game.other_players(self))
                print()
                print(f"Player '{enemy.name}', player '{self.name}' is assassinating some of your influences")
                print()
                enemy.show_cards()
                print()
                card = game.lose_card(enemy)
                game.log.append(f"-No one counterattacks the play of '{self.name}' and the '{card}' of '{attacker.name}' dies in the Assassinate")

            else:
                challenger2 = menu.ask_for(game.other_players(attacker),"challenge")
                if challenger2 == False:
                    game.log.append(f"-No one challenge the counterattack of '{attacker.name}' against the action of '{self.name}', lose 3 coins")
                    self.coins-=3
                else:
                    challenge2 = game.challenge(challenger2,attacker,"Countness")
                    if challenge2 == False:
                        self.coins-=3
                        print()
                        print("Choose the player you wanto to assassinate influence")
                        print()
                        enemy = menu.select_enemy(game.other_players(self))
                        print()
                        print(f"Player '{enemy.name}', player '{self.name}' is assassinating some of your influences")
                        print()
                        enemy.show_cards()
                        print()
                        card = game.lose_card(enemy)
                        game.log.append(f"-'{attacker.name}' have the 'Countness' and wins the challenge agains '{challenger.name}', the '{card}' of '{enemy.name}' dies in the Assassinate")
                    else:
                        
                        self.coins-=3
        else:
            challenge = game.challenge(challenger,self,"Assassin")
            if challenge == False:
                pass
            else:
                self.coins-=3
                print()
                print("Choose the player you wanto to assassinate influence")
                print()
                enemy = menu.select_enemy(game.other_players(self))
                print()
                print(f"Player '{enemy.name}', player '{self.name}' is assassinating some of your influences")
                print()
                enemy.show_cards()
                print()
<<<<<<< HEAD
                card = game.lose_card(enemy)
                
=======
                game.lose_card(enemy)
>>>>>>> d1d6145ad200afd33fc97f92200b1a04ca174af8

    def captain_steal(self,game,menu):
        challenger = menu.ask_for(game.other_players(self),"challenge")
        if challenger == False:
            attacker = menu.ask_for(game.other_players(self),"counterattack")
            if attacker == False:
                print()
                print("Choose the player you want to steal a maximum of 2 coins")
                print()
                enemy = menu.select_enemy(game.other_players(self))
                print()
                print(f"Player '{enemy.name}', player '{self.name}' is stealing your coins")
                if enemy.coins>=2:
                    enemy.coins-=2
                    self.coins+=2
                elif enemy.coins<2:
                    enemy.coins-=1
                    self.coins+=1
                else:
                    pass
            else:
                challenger2 = menu.ask_for(game.other_players(attacker),"challenge")
                if challenger2 == False:
                    pass
                else:
                    challenge2 = game.challenge_for_2_cards(challenger2,attacker,"Ambassador","Captain")
                    if challenge2 == False:
                        print()
                        print("Choose the player you want to steal a maximum of 2 coins")
                        print()
                        enemy = menu.select_enemy(game.other_players(self))
                        print()
                        print(f"Player '{enemy.name}', player '{self.name}' is stealing your coins")
                        if enemy.coins>=2:
                            enemy.coins-=2
                            self.coins+=2
                        elif enemy.coins<2:
                            enemy.coins-=1
                            self.coins+=1
                        else:
                            pass
                    else:
                        pass
        else:
            challenge = game.challenge(challenger,self,"Captain")
            if challenge == False:
                pass
            else:
                print()
                print("Choose the player you want to steal a maximum of 2 coins")
                print()
                enemy = menu.select_enemy(game.other_players(self))
                print()
                print(f"Player '{enemy.name}', player '{self.name}' is stealing your coins")
                if enemy.coins>=2:
                    enemy.coins-=2
                    self.coins+=2
                elif enemy.coins<2:
                    enemy.coins-=1
                    self.coins+=1
                else:
                    pass

    def ambassador_exchange(self,game,menu,deck):
        challenger = menu.ask_for(game.other_players(self),"challenge")
        if challenger == False:
            self.cards.append(deck.deck_of_cards[-1])
            deck.deck_of_cards.pop()
            self.cards.append(deck.deck_of_cards[-1])
            deck.deck_of_cards.pop()
            print()
            self.show_cards()
            card_1 = game.lose_card(self)
            self.banished_cards.pop()
            print()
            self.show_cards()
            card_2 = game.lose_card(self)
            self.banished_cards.pop()
            deck.deck_of_cards.append(card_1)
            deck.deck_of_cards.append(card_2)
            deck.shuffle()
        else:
            challenge = game.challenge(challenger,self,"Ambassador")
            if challenge == False:
                pass
            else:       
                self.cards.append(deck.deck_of_cards[-1])
                deck.deck_of_cards.pop()
                self.cards.append(deck.deck_of_cards[-1])
                deck.deck_of_cards.pop()
                print()
                self.show_cards()
                card_1 = game.lose_card(self)
                print()
                self.show_cards()
                card_2 = game.lose_card(self)
                deck.deck_of_cards.append(card_1)
                deck.deck_of_cards.append(card_2)
                deck.shuffle()