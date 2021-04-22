from player import Player
from menu import Menu
from cards import Cards

players = []
def generate_players():
    for i in range(ask_n_players()):
        name = input(f"Insert name player {i+1}: ")
        players.append(Player(name))

def ask_n_players():
    while True: 
        try:
            n = int(input("Insert number of players (3 or 4): ")) 

        except ValueError:
            print("NUMBER MUST BE 3 OR 4")
            continue

        if n>=5 or n<=2:
            print("NUMBER MUST BE 3 OR 4")
        
        else:
            break
    print()
    return n
def Show_players():
        print("\nPlayers:")
        print ("Number - Name - Coins - Cards")
        for (i, _) in enumerate(players):
            print(f"{i+1}: {players[i].name} {players[i].coins} {players[i].cards} ")


def main():
    print()
    generate_players()
    Cards.Deal(players, Cards.cards_list, Cards.cards_hidden)
    Show_players()
    pass



if __name__ == "__main__":
    main()   