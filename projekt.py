class Producent:
    def __init__(self, nazwa):
        self.nazwa = str(nazwa)

    def __str__(self):
        return self.nazwa


class Rodzaj:
    def __init__(self, rodzaj):
        self.rodzaj = str(rodzaj)

    def __str__(self):
        return self.rodzaj


class Material:
    def __init__(self, material):
        self.material = str(material)

    def __str__(self):
        return self.material


class RowerSz:
    def __init__(self, producent, model, rodzaj, material):
        self.producent = Producent(producent)
        self.model = str(model)
        self.rodzaj = Rodzaj(rodzaj)
        self.material = Material(material)

    def pobierzNazweProducenta(self):
        return self.producent.__str__()

    def pobierzNazweModelu(self):
        return self.model

    def pobierzRodzaj(self):
        return self.rodzaj.__str__()

    def pobierzNazweMaterialu(self):
        return self.material.__str__()


class Rower:
    def __init__(self, numer, cena, szczegoly):
        self.numer = str(numer)
        self.cena = float(cena)
        self.szczegoly = RowerSz(szczegoly)

    def pobierzNumer(self):
        return self.numer

    def pobierzCene(self):
        return self.cena

    def ustawCene(self, cena):
        self.cena = float(cena)

    def pobierzSzczegoly(self):
        return self.szczegoly

    def pobierzSzczegolyJakoTekst(self):
        zmienna = 'Producent: ' + self.szczegoly.pobierzNazweProducenta() + '| cena: ' + str(self.pobierzCene()) + '| model: ' + self.szczegoly.pobierzNazweModelu() + '| rodzaj: ' + self.szczegoly.pobierzRodzaj() + '| material: ' + self.szczegoly.pobierzNazweMaterialu()
        str(zmienna)
        return zmienna


class DoroslySz(RowerSz):
    def __init__(self, producent, model, rodzaj, material):
        self.producent = Producent(producent)
        self.model = str(model)
        self.rodzaj = Rodzaj(rodzaj)
        self.material = Material(material)


class Dorosly(Rower):
    def __init__(self, numer, cena, szczegoly):
        self.numer = str(numer)
        self.cena = float(cena)
        self.szczegoly = szczegoly

    def pobierzSzczegolyJakoTekst(self):
        zmienna = 'Producent: ' + self.szczegoly.pobierzNazweProducenta() + '| cena: ' + str(self.pobierzCene()) + '| model: ' + self.szczegoly.pobierzNazweModelu() + '| rodzaj: ' + self.szczegoly.pobierzRodzaj() + '| material: ' + self.szczegoly.pobierzNazweMaterialu()
        str(zmienna)
        return zmienna


class DzieckoSz(RowerSz):
    def __init__(self, producent, model, rodzaj, material, iloscKol):
        self.producent = Producent(producent)
        self.model = str(model)
        self.rodzaj = Rodzaj(rodzaj)
        self.material = Material(material)
        self.iloscKol = int(iloscKol)

    def pobierzIloscKol(self):
        return self.iloscKol


class Dziecko(Rower):
    def __init__(self, numer, cena, szczegoly):
        self.numer = str(numer)
        self.cena = float(cena)
        self.szczegoly = szczegoly


    def pobierzSzczegolyJakoTekst(self):
        zmienna = 'Producent: ' + self.szczegoly.pobierzNazweProducenta() + '| cena: ' + str(self.pobierzCene()) + '| model: ' + self.szczegoly.pobierzNazweModelu() + '| rodzaj: ' + self.szczegoly.pobierzRodzaj() + '| material: ' + self.szczegoly.pobierzNazweMaterialu() + '| ilosc kol: ' + str(self.szczegoly.pobierzIloscKol())
        str(zmienna)
        return zmienna


class Magazyn:
    def __init__(self):
        self.lista = []

    def dodajRower(self, rower):
        self.rower = rower
        self.lista.append(rower)

    def pobierz(self, numer):
        self.numer = str(numer)
        for p in self.lista:
            if p.pobierzNumer() == numer:
                print('Znalazlem rower o takim numerze:')
                return p
        print('Nie znalazlem roweru o takim numerze' + '\n')

    def wyswietlRowery(self):
        print('Lista rowerow:' + '\n')
        for p in self.lista:
            print(p.pobierzSzczegolyJakoTekst() + '\n')


prod1 = Producent("Kross")
prod2 = Producent("Author")

rodz1 = Rodzaj("trekingowy")
rodz2 = Rodzaj("szosowy")
rodz3 = Rodzaj("gorski")

mate1 = Material("aluminiowy")
mate2 = Material("stalowy")
mate3 = Material("carbon")

sz1 = DoroslySz(prod1, "Navigo", rodz1, mate1)
rower1 = Dorosly("M945", 980.00, sz1)
sz2 = DoroslySz(prod1, "Jasen", rodz2, mate2)
rower2 = Dorosly("G570", 799.00, sz2)
sz3 = DoroslySz(prod2, "Kim", rodz1, mate2)
rower3 = Dorosly("P456", 459.00, sz3)
sz4 = DoroslySz(prod2, "Olsen", rodz3, mate3)
rower4 = Dorosly("S909", 1000.00, sz4)
sz5 = DoroslySz(prod1, "Bravo", rodz3, mate1)
rower5 = Dorosly("F538", 999.00, sz5)

sz6 = DzieckoSz(prod1, "Kido", rodz1, mate1, 2)
rower6 = Dziecko("P456", 459.00, sz6)
sz7 = DzieckoSz(prod1, "Asid", rodz1, mate3, 2)
rower7 = Dziecko("A345", 298.00, sz7)
sz8 = DzieckoSz(prod2, "Bobo", rodz1, mate1, 4)
rower8 = Dziecko("D387", 199.00, sz8)
sz9 = DzieckoSz(prod2, "Jim", rodz1, mate2, 2)
rower9 = Dziecko("O231", 537.00, sz9)
sz10 = DzieckoSz(prod1, "Niko", rodz1, mate3, 4)
rower10 = Dziecko("J505", 101.00, sz10)

magazyn = Magazyn()
magazyn.dodajRower(rower1)
magazyn.dodajRower(rower2)
magazyn.dodajRower(rower3)
magazyn.dodajRower(rower4)
magazyn.dodajRower(rower5)
magazyn.dodajRower(rower6)
magazyn.dodajRower(rower7)
magazyn.dodajRower(rower8)
magazyn.dodajRower(rower9)
magazyn.dodajRower(rower10)

pytanie = input('Czy wyswietlic wszystkie rowery w magazynie? [Tak/Nie]' + '\n')
if pytanie == 'Tak':
    magazyn.wyswietlRowery()
else:
    print('Zamiast wyswietlic wszystkie rowery wyszukajmy jeden przykladowy po numerze seryjnym (np. P456)' + '\n')


numer = input('Podaj numer roweru ktory szukasz: ')

wyszukanyRower = magazyn.pobierz(numer)
if wyszukanyRower.pobierzNumer() != numer:
    print('Nie ma takiego roweru w magazynie' + '\n')
else:
    print(wyszukanyRower.pobierzSzczegolyJakoTekst() + '\n')
    pytanie2 = input('Czy zmienic cene wyszukanego roweru? [Tak/Nie]' + '\n')
    if pytanie2 == 'Tak':
        cena = input('Podaj cene: ')
        wyszukanyRower.ustawCene(cena)
        print('Szczegoly roweru po zmianie ceny:')
        szczegoly = wyszukanyRower.pobierzSzczegolyJakoTekst()
        print(szczegoly + '\n')


print('Dziekuje za skorzystanie z programu [nacisnij klawisz aby zamknac program].')