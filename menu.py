class Menu:
    
    def __init__(self,option):
        self.__option = option

    @property
    def option(self):
        return self.__option

    def show_options_general(self, value):
        print("\nSelect the type of action you want:")
        print("1. Character action")
        print("2. General action")
        print("3. To challenge")
        print('4. Counter')
        #print("0. Salir") no se puede pasar turno
        return int(input())
    
    def show_options_specific(self,value):
        
        if value == 1:
            #aqui acciones de personajes
            pass
        elif value == 2:
            print("\nSelect the type of action you want:")
            print("1. Income")
            print("2. Foreign aid")
            print("3. Coup")
        elif value == 3:
            print("Challenge")
            #aqui acciones de desafio 
        elif value == 4:
            print ("Counter")
            # aca acciones de contraataque segun carta
        else:
            print("malo")
            #aqui poner excepcion que elija correctamente
        return int(input())