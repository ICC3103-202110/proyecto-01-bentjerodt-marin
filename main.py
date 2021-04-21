from players import Player

def generate_players():
    for i in range(ask_n_players()):
         name = input(f"Insert name player {i+1}: ")
         players.append(Player(name))

def ask_n_players():
    while True: 
        try:
            n = int(input("Inseret number of players (3 or 4): ")) 

        except ValueError:
            print("NUMBER MUST BE 3 OR 4")
            continue

        if n>=5 or n<=2:
            print("NUMBER MUST BE 3 OR 4")
        
        else:
            break
    print()
    return n

def main():
    print()
    generate_players()
    print()

    for i in players:
        print(i.name)

    pass

players = []

main()   