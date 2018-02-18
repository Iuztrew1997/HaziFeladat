import math as mt
def feladat_1():
    a=3
    b=5
    a=a+b
    b=a-b
    a=a-b
def feladat_3(x):
    if x>-2 and x<0:
        return 2*x
    elif x>=0 and x<2:
        return x**2
    elif x>2:
        return 10
    else:
        print("a fg nem ertelmezett!")
        return
def feladat_20(n):
    a=1
    b=1
    if n ==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        c=a+b
        print(a,b,c)
        k=3
        while k<n:
            a=b
            b=c
            c=a+b
            print(c)
            k+=1
def feladat_17(n):
    masolat=n
    uj_szam=0
    while n!=0:
        szj=n%10
        uj_szam=uj_szam*10+szj
        n=n//10
    return uj_szam==masolat
def feladat_16(a,b):
    while True:
        r=a%b
        a=b
        b=r
        if r==0:
            break
    return a
def feladat_6():
    while True:
        a = float(input("A harom szog egyik oldala:"))
        b = float(input("A harom szog egyik oldala:"))
        c = float(input("A harom szog egyik oldala:"))
        if a<=0 or b<=0 or c<=0:
            print("Nem megfelelo adat!")
        else:
            break
    if a+b>c and b+c>a and c+a>b:
        p=(a+b+c)/2
        T=mt.sqrt(p*(p-a)*(p-b)*(p-c))
        r=T/p
        R=(a*b*c)/4*T
        print("R=%.2f Es r=%.2f" % (R,r))
    else:
        print("Nem kepezhetik!")

def main():
    print(feladat_3(1))
    feladat_6()
    feladat_17(131)
    print(feladat_16(230, 300))
    feladat_1()
    feladat_20(10)
main()