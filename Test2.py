if __name__=="__main__":
    a=int(input())
    b=int(input())
    c=(2*a+b*3)/2
    d=0
    g=1
    while (d<4):
        print(c)
        d=d+1
    
    if c%5==0:
        e=a/2
    elif c%5==1:
        e=a/2
    elif c%5==2:
        e=a/2
    else:
        e=a
    if b>=6:
        f=b/2
    elif b==3:
        f=3
    elif b==4:
        f=3
    elif b==5:
        f=3

    else:
        f=b
    for i in range (0,int(f),1): #sloupec
        for j in range (0,e,1): #radek      
            print("* ", end= "")
        print()
print("citim se na znamku 1")