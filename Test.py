if __name__=="__main__":
    a=int(input())
    b=int(input())
    c=a*b
    d=0

    while (d<4):
        print(c)
        d=d+1
    
    if a>=5:
        e=int(a/2)
    else:
        e=a
    if b<5:
        f=int(b/4)
    else:
        f=b

    for i in range (0,e,1):
        for j in range (0,f,1):
            if c%2==0: 
                print("* ", end= "")
            else:
                print("/ ", end= "")
        print()
    print("citim se na znamku 1")