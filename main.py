def citirelista():
    l=[]
    string=input("Dati lista cu elemente separate cu virgula:")
    numere=string.split(",")
    for x in numere:
        l.append(int(x))
    return l

def lista_fara_nr_prime(l):
    rezultat=[]
    for i in range (len(l)):
        ok=1
        if l[i]<=1:
            return false
        else:
            for d in range (2,l[i]//2):
                if l[i]%d==0:
                    ok=0
            if ok==1:
                rezultat.append(l[i])
    return rezultat

def numar_mai_mare_decat_media_nr(l,x):
    suma=0
    for i in range (len(l)):
        suma=suma+l[i]
    if suma//len(l)>x:
        return True
    else:
        return False

def adaugare_nr_div_proprii(l):
    rezultat=[]
    for i in range (len(l)):
        nrdediv=0
        for d in range (2,l[i]//2):
            if l[i]%d==0:
                nrdediv=nrdediv+1
        rezultat.append(l[i])
        rezultat.append(nrdediv)
    return rezultat

def test_lista_fara_nr_prime(l):
    assert lista_fara_nr_prime(l)
    assert lista_fara_nr_prime(l)
    assert lista_fara_nr_prime(l)

def test_numar_mai_mare_decat_media_nr(l,x):
    assert numar_mai_mare_decat_media_nr(l,x)
    assert numar_mai_mare_decat_media_nr(l, x)
    assert numar_mai_mare_decat_media_nr(l, x)

def test_adaugare_nr_div_proprii(l):
    assert adaugare_nr_div_proprii(l)
    assert adaugare_nr_div_proprii(l)
    assert adaugare_nr_div_proprii(l)


def main():
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
            print(2)

        elif optiune == 6:
            break



main()