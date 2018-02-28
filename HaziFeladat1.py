import math as mt
import math, cmath
def feladat_1():
    a=3
    b=5
    a=a+b
    b=a-b
    a=a-b
def feladat_2():
    szam1 = int(input("Adj meg egy egesz szamot: "))
    szam2 = int(input("Adj meg egy egesz szamot: "))
    szam3 = int(input("Adj meg egy egesz szamot: "))
    lista=[szam1,szam2,szam3]
    for i in lista:
        if i<max(lista) and i>min(lista):
            print(min(lista), i, max(lista))
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
def feladat_4(a,b,c):
    lista = [a,b,c]
    for i in lista:
        if i < max(lista) and i > min(lista):
            print(min(lista), i, max(lista))
def feladat_5(a,b,c,d):
    if d>=0:
        print(a,b,c,d)
    else:
        print(a,b,d,c)
def feladat_7(a,b,hossz):
    K=2*(a+b)
    if K==hossz:
        return 0
    elif K>hossz:
        return K-hossz
    elif K<hossz:
        return hossz-K
def feladat_8_1(x):
    if x<5:
        return 3*x-5
    elif 5<=x<=10:
        return 10
    elif x>10:
        return 9*x+1
def feladat_8_2(a,b,c,d):
    if a+c>2*d and b>0:
        return d-3*b
    elif a+c<2*d and b<0:
        return d+3*b
    else:
        return 4
def feladat_9():
    a = input('Kérem a másodfokú egyenlet főegyütthatóját: ')
    a = float(a)
    while a == 0:
        print('Ez nem lesz másodfokú egyenlet; nem oldom meg.')
        a = input('Kérem a másodfokú egyenlet főegyütthatóját: ')
        a = float(a)

    b = input('Kérem az elsőfokú tag együtthatóját: ')
    c = input('Kérem a konstans tagot: ')
    b = float(b)
    c = float(c)

    d = b * b - 4 * a * c
    print('A diszkrimináns értéke', d)

    if d >= 0:
        print('Van valós megoldás.')
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        print('Az egyik megoldás', x1)
        print('A másik megoldás', x2)
    else:
        print('Nincs valós megoldás.')
        x1 = (-b - cmath.sqrt(d)) / (2 * a)
        x2 = (-b + cmath.sqrt(d)) / (2 * a)
        print('Az egyik megoldás', x1)
        print('A másik megoldás', x2)
def feladat_13(dolgozat):
    if dolgozat==5:
        print("jeles")
    elif dolgozat==4:
        print("jó")
    elif dolgozat==3:
        print("közepes")
    elif dolgozat==2:
        print("elégséges")
    elif dolgozat==1:
        print("elégtelen")
def feladat_14(honap):
    if honap==1:
        print("január")
    elif honap == 2:
        print("február")
    elif honap==3:
        print("március")
    elif honap==4:
        print("április")
    elif honap==5:
        print("május")
    elif honap==6:
        print("június")
    elif honap==7:
        print("július")
    elif honap==8:
        print("augusztus")
    elif honap==9:
        print("szeptember")
    elif honap==10:
        print("október")
    elif honap==11:
        print("november")
    elif honap==12:
        print("december")
def feladat_15(a,b):
    hanyados=0
    while a>=b:
        hanyados+=1
        a=a-b
    print(hanyados)
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
    'print(feladat_3(1))'
    #feladat_6()
    #feladat_17(131)
    #print(feladat_16(230, 300))
    #feladat_1()
    #feladat_20(10)
    #feladat_2()
    #feladat_4(2,4,3)
    #feladat_5(1,2,3,-4)
    #print(feladat_7(2,3,9))
    #print(feladat_8_1(5))
    #print(feladat_8_2(2,3,1,2))
    #feladat_9()
    #feladat_13(2)
    #feladat_14(4)
    #feladat_15(10,2)
main()