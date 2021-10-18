'''
functia citire citeste lista data
'''
def citirelista():
    l=[]
    string=input("Dati lista cu elemente separate cu virgula:")
    numere=string.split(",")
    for x in numere:
        l.append(int(x))
    return l

'''
functia lista_fara_nr_prime elimina numerele prime din listă
'''
def lista_fara_nr_prime(l):
    rezultat=[]
    for i in range (len(l)):
        y=l[i]
        nrprim=True
        if y==1:
            rezultat.append(y)
        elif y==0:
            rezultat.append(y)
        else:
            for d in range (2,y//2+1):
                if y%d==0:
                    nrprim=False
            if nrprim==False:
                rezultat.append(y)
    return rezultat


'''
functia numar_mai_mare_decat_media_nr dacă media aritmetică a numerelor este mai mare decât un număr x dat
'''
def numar_mai_mare_decat_media_nr(l,x):
    suma=0
    for i in range (len(l)):
        suma=suma+l[i]
    if suma//len(l)>x:
        return True
    else:
        return False

'''
functia adaugare_nr_div_proprii adăuga după fiecare element numărul de divizori proprii ai elementului
'''
def adaugare_nr_div_proprii(l):
    rezultat=[]
    for i in range (len(l)):
        nrdediv=0
        for d in range (2,l[i]//2+1):
            if l[i]%d==0:
                nrdediv=nrdediv+1
        rezultat.append(l[i])
        rezultat.append(nrdediv)
    return rezultat

def lista_intiala_schimbata_cu_tuplu(l):
    rez=l[:]
    for i in range (len(l)):
        rez[i][0]=l[i]
        rez[i][1]=i
        nr=0
        for d in range (len(l)):
            if l[i]==l[d]:
                nr=nr+1
        rez[i][2]=nr
    return rez


def test_lista_fara_nr_prime():
    assert lista_fara_nr_prime([1,2,3,4])==[1,4]
    assert lista_fara_nr_prime([1,7,9,20])==[1,9,20]

def test_numar_mai_mare_decat_media_nr():
    assert numar_mai_mare_decat_media_nr([1,2,3,4],1)==True
    assert numar_mai_mare_decat_media_nr([1,2,3,4],3)==False

def test_adaugare_nr_div_proprii():
    assert adaugare_nr_div_proprii([9,7,20])==[9,1,7,0,20,4]
    assert adaugare_nr_div_proprii([10,5,3])==[10,2,5,0,3,0]


def main():
    test_lista_fara_nr_prime()
    test_numar_mai_mare_decat_media_nr()
    test_adaugare_nr_div_proprii()
    while True:
        print("1.Citirea unei liste de numere întregi. Citirile repetate suprascriu listele precedente.")
        print("2.Afișarea listei după eliminarea numerelor prime din listă")
        print("3.Să se afișeze dacă media aritmetică a numerelor este mai mare decât un număr n dat.")
        print("4.Afișarea listei obținută prin adăugarea după fiecare element numărul de divizori proprii ai elementului.")
        print("5.Afișarea listei obținute din lista inițială în care numerele sunt înlocuite cu un tuplu în care pe prima poziție este numărul, pe a doua poziție va fi indexul elementului din listă, iar pe a treia poziție apare numărul de apariții a numărului.")
        print("6.Iesire")

        optiune=int(input("Alegeti comanda: "))
        if optiune==1:
            l=citirelista()
        elif optiune==2:
            print(lista_fara_nr_prime(l))
        elif optiune==3:
            numar=int(input("Dati numar cerut: "))
            if numar_mai_mare_decat_media_nr(l,numar):
                print("Da")
            else:
                print("Nu")
        elif optiune==4:
            print(adaugare_nr_div_proprii(l))
        elif optiune == 5:
            print(lista_intiala_schimbata_cu_tuplu(l))
        elif optiune == 6:
            break



main()