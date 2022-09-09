def scitani(a,b):
    return a+b
def deleni(a,b):
    return a/b
def nasobeni_2(a,b):
    return a*b
def nasobeni_3(a,b,c):
    return a*b*c
def odecitani(a,b):
    return a-b
def vypocet_obvod(a,b):
    return 2*(a+b)
def cislovani(a,b):
    for i in range (0,a,1):
        for j in range (0,b,1):
            if i%2==1:
                print(j+1, end= "")
            else:
                print("*/", end= "")
            
        print()
if __name__=="__main__":
    vyska=6
    sirka=10
    print(vypocet_obvod(vyska,sirka))
    pocet_radku=8
    pocet_sloupcu=int(pocet_radku/2)
    cislovani(pocet_radku,pocet_sloupcu)
    a=4
    b=3
    c=2
    d=deleni((nasobeni_3(b,deleni(a,c),scitani(a,5))),scitani((odecitani(odecitani(b,3),nasobeni_2(c,a))),7))
    print(d)