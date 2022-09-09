import random as rnd
class Bojovnik():
    def __init__(self,name,atk,deff,hp):
        self.__name=name
        self.__atk=atk
        self.__deff=deff
        self.__hp=hp

    def get_name(self):
        return self.__name
    def get_atk(self):
        return self.__atk
    def get_deff(self):
        return self.__deff
    def get_hp(self):
        return self.__hp
    def set_hp(self,hp):
        self.hp=hp
        return
class Souboj():
    def __init__(self,bojovnik1,bojovnik2):
        self.__bojovnik1=bojovnik1
        self.__bojovnik2=bojovnik2
    def souboj(self):
        while(self.__bojovnik1.get_hp() >0 and self.__bojovnik2.get_hp()>0):
            boj1_atk=rnd.randint(1,self.__bojovnik1.get_atk())
            boj2_atk=rnd.randint(1,self.__bojovnik2.get_atk())
            boj1_deff=rnd.randint(1,20)
            boj2_deff=rnd.randint(1,20)
    def vypis(self):
        print(f"jmeno bojovnika je: {self.__bojovnik1.get_name()}")
if __name__=="__main__":
    fighter1=Bojovnik("Kvetoslav","14","4","115")
    fighter2=Bojovnik("Zikmund","7","13","80")
    souboj=Souboj(fighter1,fighter2)
    souboj.vypis()