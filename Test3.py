if __name__=="__main__":
    a=int(input())
    b=int(input())
    c=1
    list2d=[]
    for i in range(0,a,1):
        radek=[]
        for j in range(0,a,1):
            radek.append(c)
            print(" {} ".format(radek[j]),end="")
        list2d.append(radek)
        print()