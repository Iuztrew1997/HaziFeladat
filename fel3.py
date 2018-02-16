'''
def generacio(n):
    a=1
    b=1
    k=1
    fajl=open("generacio.txt",mode="w")
    while k<n:
        fajl.write("%.4f " % (a/b))
        a=a+b
        b=a-b
        k=k+1
    fajl.close()

def sor_szamlalo(fajl_nev):
    fajl=open(fajl_nev,mode="r")
    max=0
    max_sor=''
    for sor in fajl:
        sor=sor.strip()
        if(sor[0].isupper() and len(sor)>max):
            max=len(sor)
            max_sor=sor
    print(max, max_sor)
    fajl.close()
    '''
def feladat2():
    fajl=open("be1.txt",mode="r")
    for sor in fajl:
        if("   " in sor):
            fajl=open("ki1.txt", mode="w")
            fajl.write(sor)
            fajl.close()
            break
def feladat3(lista,betu):
    li=[]
    fajl=open("ki2.txt",mode="w")
    for i in lista:
        if i[0]==betu:
            li.append(i)
    fajl.write(str(li))
    fajl.close()
def main():
    #generacio(20)
    #sor_szamlalo("be1.txt")
    feladat2()
    feladat3(["alma", "ananasz", "narancs"], 'a')
main()