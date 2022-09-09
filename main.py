class Auto():
    def __init__(self,barva,rok,motor,karoserie,tachometr):
        self.barva=barva
        self.rok=rok
        self.__motor=motor
        self.karoserie=karoserie
        self.__tachometr=tachometr
    #Gettry
    def get_motor(self):
        return self.__motor
    #Settry
    def set_motor(self,motor):
        self.__motor=motor
    def snizit_tachometr(self,percent):
        self.__tachometr *=((100-percent)/100)
    def get_tachometr(self):
        return self.__tachometr
        
if __name__=="__main__":
    auto1 = Auto("zluta",1999, "1.7","sedan",190203)
    print(auto1.get_motor())
    auto1.set_motor("2.5")
    auto1.snizit_tachometr(25)
    print(auto1.get_tachometr())
    # barvy=["zluta","modra","fialova","zelena","cervena"]
    # motor=["1.7","1.8","2.0","1.0","0.9"]
    # rok=["2010","1999","2004","2000","2003"]
    # karoserie=["sedan","limuzina","kombi","hatchback",None]

    # for i in range(len(barvy)):
    #     print("Auto{} ma barvu {}, motorizaci {}, vyrobeno roku {}, a je to {}.".format(i,barvy[i],motor[i],rok[i]))