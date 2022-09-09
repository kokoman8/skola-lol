class Zvire():
    def __init__(self,nazev,jmeno,vek,pocet_zubu):
        self.__nazev=nazev
        self.__jmeno=jmeno
        self.vek=vek
        self.pocet_zubu=pocet_zubu
    #Gettry
    def get_nazev(self):
        return self.__nazev
    def get_jmeno(self):
        return self.__jmeno
    #Settry
    def narozeniny(self,vek):
        self.vek=vek
        
if __name__==__main__:
    zvire1 = Zvire("pes","alik", "3","42")
    zvire2 = Zvire("kocka","mourek","5", "30")
    print(zvire1.get_nazev())
    print(zvire1.get_jmeno())
    print(zvire2.get_nazev())
    print(zvire2.get_jmeno())
    for i in range(len(Zvire)):
        print(f"Zvire{} nazev: {}, jmeuje se: {}, vek: {}, ma {} zubu.".format(i,nazev[i],jmeno[i],vek[i],pocet_zubu[i]))