class Menu:
    
    def __init__(self,option):
        self.__option = option

    @property
    def option(self):
        return self.__option

    def show_options(self, value):
        if value < 0 :
            print("malo")
    
    
     