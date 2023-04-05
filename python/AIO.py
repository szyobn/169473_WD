# import sys
#
# print(sys.version)

#               https://pl.python.org/docs/lib/built-in-funcs.html
#               https://docs.python.org/3/library/stdtypes.html#string-methods
#               https://docs.python.org/3/library/math.html


a = 'napis\ndrugi napis'
print(a)

b = 4
c = 4.5
print(b, c)
# Liczby zespolone:
d = 3+4j
print(d)

e = b + c
print(e)

f = b // c
print(f)

g = b % c
print(g)

i = c**2
print(i)

j = pow(5, 2)
print(j)

# k = 5**1/2
# print(k)
# m = pow(5, 1/2)
# print(m)

print('b = b + 2')
b += 2
print(b)

lista = ['a0', 2, 3, 4, 5, [7, 6, 5], 5.5]
print(lista[5])

# Dodanie do końca:
lista.append(6.5)
# Dodawanie elementu na pozycję
lista.insert(1, 128)
# Dodawanie kilku elementów na koniec listy
lista.extend([6.5, 8])
print(lista)
# Usuwanie elementu po indeksie, pop() - bez podanej wartości usunie ostatni element z listy
lista.pop(0)
# usuwanie elementu po wartości elementu
lista.remove(5.5)
# Odwórcenie listy
lista.reverse()
# sortowanie
# lista.sort()
# del - usuwanie całej listy

slownik = {'a': 1, 3: 1, 5: 'b', 'a': 5}
print(slownik)
print(slownik['a'])

slownik['klucz'] = 'wartość'
print(slownik)

slownik.pop('a')
print(slownik)

print(slownik.keys())
print(slownik.values())

# Formatowanie łańcuchów znakowych
print('a = %(zm)d' %{'zm': 12})
print('a = {}, b = {}'.format(12, 14))

# Funkcje warunkowe:
# if warunek:
#   instrukcja 1
#   instrukcja 2
# elif warunek2
#   instrukcja 1
#   instrukcja 2
# else:
#   instrukcja 1

# a = input('Podaj a: ')
# b = input('Podaj b: ')
# print(a)
# print(b)
#print(type(a))
#print(type(b))


# a = int(a)
# b = int(b)
# print(type(a))
# print(type(b))
#
# if a > b:
#     print('a = ' + str(a))
# elif a < b:
#     print('b = ' + str(b))
# else:
#     print('a równe b')


# x = input('Podaj x: ')
# y = input('Podaj y: ')
#
# if a == b:
#     print('Są takie same')
# else:
#     print("Są różne od siebie")

# a = input('Podaj a: ')
# b = input('Podaj b: ')
# x = input('Podaj x: ')
# y = input('Podaj y: ')

# if (a > b) & (x > y):
#     print(a, x)
# else:
#     print('a nie jest większe b lub x nie jest większy od y')

#                                           Pętle for
# for element in sekwencja:
#   instrukcja 1
#   instrukcja 2
# else: (opcjonalnie)
#   instrukcja 1

#        range(start, stop, co ile)
for x in range(1, 6, 1):
    print(x)
for x in lista:
    print(x)
print("")

for x in range(0, len(lista)):
    print(lista[x])
#                                           Pętla while
# while warunek:
#   instrukcja 1
#   instrukcja 2
# else:
#   instrukcja 1

# liczba = 0
# while liczba != len(lista):
#     print(lista[liczba])
#     liczba += 1


# liczby = [3, 45, 12, 23, 32, 54]
# licznik = 0
# a = int(input("podaj a: "))
# while licznik != len(liczby):
#     if a - liczby[licznik] == 0:
#         print('{} - {} = 0'.format(a, liczby[licznik]))
#         break
#     licznik += 1

liczby = [1, 2, 2, 2, 2, 3]
licznik = 0

while licznik != len(liczby):
    if liczby[licznik] == 2:
        liczby.pop(licznik)
    else:
        licznik += 1

print(liczby)


import math
#                           ZAD_1a  Napisz skrypt, który policzy i wyświetli następujące wyrażenia: e^10
e = math.exp(10)
print(e)
#                           ZAD_1b  √(6&ln⁡(5+〖sin〗^2 (8)))
y = math.pow(math.log(5+math.pow(math.sin(8), 2)), 1/6)
print(y)

#                           ZAD_1c  ⌊3,55⌋
zad1c= math.floor(3.55)
print(zad1c)
#                           ZAD_1d  ⌈4,80⌉
zad1d = math.ceil(4.8)
print(zad1d)
#                           ZAD_2   Zapisz swoje imie i nazwisko w oddzielnych zmiennych wszystkie wielkimi literami.
#Użyj odpowiedniej metody by wyświetlić je pisane tak, że pierwsza litera jest wielka a pozostałe małe.
# (trzeba użyć metody capitalize)
imie= "SZYMON"
nazwisko = "SENDER"
imiee = imie.capitalize()
nazwiskoo = nazwisko.capitalize()
print(imiee, nazwiskoo)
#                           ZAD_3   Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu piosenki z
# powtarzającymi się słowami np. „la la la”. Następnie użyj odpowiedniej funkcji, która zliczy występowanie słowa „la”.
# (trzeba użyć metody count)
tekst = "La la la, la la la, la la la"

l_tekst = tekst.count("la")

print("Liczba wystąpień słowa 'la':", l_tekst)
#                           ZAD_4   Do poszczególnych elementów łańcucha możemy się odwoływać przez podanie indeksu.
#Np. pierwszy znak zapisany w zmiennej imie uzyskamy przez imie[0]. Zapisz dowolną zmienną łańcuchową i wyświetl jej
# drugą i ostatnią literę, wykorzystując indeksy.
x="siała"
print(x[1], x[4])
#                           ZAD_5   Zmienne łańcuchowe możemy dzielić, wykorzystaj zmienną z Zad. 3 i spróbuj ją
#podzielić na poszczególne wyrazy. (trzeba użyć metody split)
x = tekst.split(" ")
print(x)
#                           ZAD_6   Napisz skrypt, w którym zadeklarujesz zmienne typu: string, float i szestnastkowe.
#Następnie wyświetl je wykorzystując odpowiednie formatowanie.
strings = "Hello, world!"
floats = 3.14159
szesntastkowy = 0xFF
print("String: {}".format(strings))
print("Float: {:.2f}".format(floats))
print("Hexadecimal: {}".format(hex(szesntastkowy)))
#                           ZAD_7   Napisz skrypt, w którym tworzysz listę ulubionych sportów, odwróć ją a następnie
#dodaj mniej lubiane sporty na sam koniec.
sporty = ['narciarstwo', 'onewheel', 'downhill']
sporty.reverse()
print(sporty)
sporty.extend(['hokej', 'golf'])
#                           ZAD_8   Stwórz słownik skrótów powszechnie używanych w gazetach lub artykułach
#internetowych. Jako klucz przyjmij skrót danego słowa, wartość to rozwinięcie tego skrótu.
skroty = {
    "np.": "na przykład",
    "itd.": "i tym podobne",
    "tj.": "to jest"
}
for skrot, rozw in skroty.items():
    print("{} - {}".format(skrot, rozw))
#                           ZAD_9   Stwórz słownik z ulubionymi grami komputerowymi. Pomyśl, co może być kluczem a co
#wartością w takim słowniku. Policz liczbę elementów w słowniku.
gry = {
    "GTA": "Grand Theft Auto",
    "CS": "Counter strike",
    "LOL": "League of legends"
}
print(len(gry))
#                           ZAD_10  Napisz skrypt, który pobiera od użytkownika zdanie i liczy wystąpienia litery a.
#Użyj funkcji input
a = input("Napisz tekst: ")
l_a = a.count("a")
print("Liczba wystąpień słowa 'a':", l_a)
#                           ZAD_11  Wczytaj trzy liczby całkowite a,b,c i sprawdź, która z nich jest największa. W
#zależności od wyniku wyświetl odpowiedni komunikat.
zad11a = int(input("Podaj pierwszą liczbę całkowitą: "))
zad11b = int(input("Podaj drugą liczbę całkowitą: "))
zad11c = int(input("Podaj trzecią liczbę całkowitą: "))

if zad11a > zad11b and zad11a > zad11c:
    print("Największa liczba to", zad11a)
elif zad11b > zad11a and zad11b > zad11c:
    print("Największa liczba to", zad11b)
else:
    print("Największa liczba to", zad11c)
#                           ZAD_12  Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i float.
#Następnie za pomocą użycia pętli for podnieśa każdą liczbę do kwadratu.

lista = [1, 2.2, 3, 4.25, 5]
for i in range(len(lista)):
    lista[i] = lista[i] ** 2
print(lista)
#                           ZAD_13  Napisz skrypt, który za pomocą pętli while pobiera 10 liczb, następnie dodaje
#do listy tylko parzyste liczby.
l_parzyste = []
licznik = 0
while licznik < 10:
    liczba = int(input("Podaj liczbę do zadania 13: "))
    if liczba % 2 == 0:
        l_parzyste.append(liczba)
    licznik += 1
print("Liczby parzyste:", l_parzyste)

#                                       ZAD_1   Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
#A = {1-x: x∈<1,10>}
# B = {1,4,16,...,47}
# C = {x: x∈B i x jest liczbą podzielną przez 2}
# Zbiór A
A = {1-x for x in range(1, 11)}
print(A)
# Zbiór B
B = {i**2 for i in range(1, 7)}
print(B)
# Zbiór C
C = {x for x in B if x % 2 == 0}
print(C)
#                                       ZAD_2   Wygeneruj losowo 10 elementów, zapisz je do listy1, następnie
#wykorzystując Python Comprehension zdefiniuj nową listę, która będzie zawierała tylko parzyste elementy
import random

lista1 = [random.randint(1, 100) for x in range(10)]

lista2 = [x for x in lista1 if x % 2 == 0]

print("Lista1:", lista1)
print("Lista2 (tylko parzyste elementy z listy1):", lista2)

#                                       ZAD_3   Utwórz słownik z produktami spożywczymi do kupienia. Klucz to niech
#będzie nazwa produktu a wartość -jednostka w jakiej się je kupuje (np. sztuki, kg itd.). Wykorzystaj Python
#Comprehension do zdefiniowania nowej listy, gdzie będą produkty, których wartość to sztuki.
slownik = {'Jajka': 'szt',
            'Chleb': 'szt',
            'Pierś z kurczaka': 'kg',
            'Twaróg': 'szt',
            'Ryż': 'szt',}
print(slownik)
sztuki = [produkt for produkt, jednostka in slownik.items() if jednostka == 'szt']
print(sztuki)
#                                       ZAD_4   Zdefiniuj funkcje, która sprawdzi czy trójkąt jest prostokątny.
def trojkat(a, b, c):
    a, b, c = sorted([a, b, c])
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False
print(trojkat(12,3,6))
#                                       ZAD_5   Zdefiniuj funkcje która policzy pole trapezu. Funkcja ma przyjmować
#wartości domyślne.
def trapez(a, b, h):
    if a == 0 or b == 0 or h == 0:
        return 0
    else:
        return ((a + b) * h) / 2
print(trapez(10,12,1))
#                                       ZAD_6   Zdefiniuj funkcję która będzie liczyć iloczyn elementów ciągu.Parametry
#funkcji a1 (wartość początkowa), b (wielkość o ile mnożone są kolejne elementy), ile (ile elementów ma mnożyć)
def ciag(a1=1, b=4, ile=10):
    iloczyn = a1
    for i in range(1, ile):
        iloczyn *= a1 + i * b
    return iloczyn
print(ciag())

#                                       ZAD_7   Napisz funkcje za pomocą operatora *, która wykona te same działanie co
#w zadaniu 6.
def iloczyn(*z):
    l=1
    for i in z:
        l*=i
    print(l)

iloczyn(3,7,5,9)


#                                       ZAD_8   Napisz funkcję, która wykorzystuje symbol **. Funkcja ma przyjmować
#listę zakupów w postaci: klucz to nazwa produktu a wartość to jego koszt. Funkcja ma zliczyć ile jest wszystkich
#produktów w ogóle i zwracać całościową wartość tych produktów.
def wartosc(**produkty):
    ilosc = len(produkty)
    wartosc = sum(produkty.values())
    print(f"Na liście jest {ilosc} produktów o wartości {wartosc} złotych.")
wartosc(belt=129.0, strapsy=42.0, cover=199.9)

#                                       ZAD_9   Napisz skrypt, który liczy pierwiastek z liczby podanej przez
#użytkownika jeśli użytkownik poda wartość ujemną to powinien być wyłapany błąd.
import math

try:
    x = float(input("Podaj liczbę: "))
    if x < 0:
        raise ValueError("Liczba nie może być ujemna")
    pierwiastek = math.sqrt(x)
    print(f"Pierwiastek z {x} to {pierwiastek}")
except ValueError as e:
    print("Błąd:", e)

    #                                       ZAD_1   Wygeneruj liczby z przedziału <0,30>, następnie pomnóż je przez 2
    # i zapisz do pliku
    plik = open("Zadanie 1.txt", "w+")

    lista = []
    for i in range(0, 31):
        lista += [i]

    for i in lista:
        lista[i] *= 2

    plik.writelines(str(lista))

    plik.close()

    #                                       ZAD_2   Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość
    plik = open("Zadanie 1.txt", "r")
    l = plik.readlines()
    plik.close()
    print(l)

    #                                       ZAD_3   Wykorzystując komendę with zapisz kilka linijek tekstu do pliku a
    # następnie wyświetl je na ekranie.
    with open("tekst.txt", "a") as plik:
        for i in range(15):
            plik.write("Uga buga, ")

    o = open("tekst.txt", "r")
    l = o.readlines()
    o.close()
    print(l)


    #                                       ZAD_4   Stwórz klasę NaZakupy, która będzie przechowywać atrybuty:
    # •nazwa_produktu, ilosc, jednostka_miary, cena_jed
    # •oraz metody:•konstruktor –który nadaje wartości
    # •wyświetl_produkt() –drukuje informacje o produkcie na ekranie
    # •ile_produktu() –informacje ile danego produktu ma być czyli ilosc +
    # jednostka_miary np. 1 szt., 3 kg itd.
    # •ile_kosztuje() –oblicza ile kosztuje dana ilość produktu np. 3 kg ziemniaków a
    # cena_jed wynosi 2 zł/kg wówczas funkcja powinna zwrócić wartość 3*2
    class Zakupt:
        n_produktu = ''
        ilosc = ''
        jednostka = ''
        cena = 'zl'

        def __init__(self, n_produktu, ilosc, jednostka, cena):
            self.nazwa = n_produktu
            self.ilosc = ilosc
            self.jednostka = jednostka
            self.cena = cena

        def wyswietl(self):
            return ilosc + ' ' + ilosc + ' ' + jednostka + ' ' + cena + ' ' + ' zl'

        def ile_prod(self):
            return ilosc + ' ' + jednostka

        def koszt(self):
            wynik = int(ilosc) * int(cena)
            return str(wynik)


    nazwa = input("Podaj nazwe produktu: ")
    ilosc = input("Podaj ilosc: ")
    jednostka = input("Podaj jednostkę miary: ")
    cena = input("Podaj cenę jednostki: ")

    nowy = Zakupt(n_produktu=str(nazwa), ilosc=int(ilosc), jednostka=str(jednostka), cena=int(cena))
    print(nowy.wyswietl())

    print("ilosc produktow: " + nowy.ile_prod())

    print("Koszty: " + nowy.koszt() + " zl")


    #                                       ZAD_5   Utwórz klasę, która definiuje ciągi arytmetyczne. Wartości powinny być
    # przechowywane jako atrybut. Klasa powinna mieć metody:
    # •wyświetl_dane –drukuje elementy na ekran
    # •pobierz_elementy–pobiera konkretne wartości ciągu od użytkownika
    # •pobierz_parametry –pobiera pierwsza wartość i różnicę od użytkownika oraz
    # ilość elementów ciągu do wygenerowania.
    # •policz_sume –liczy sume elementow
    # •policz_elementy –liczy elementy jeśli pierwsza wartość i różnica jest podana
    class CiagArytmetyczny:
        def __init__(self):
            self.elementy = []

        def wyświetl_dane(self):
            print("Elementy ciągu arytmetycznego:", self.elementy)

        def pobierz_elementy(self):
            n = int(input("Podaj ilość elementów ciągu: "))
            for i in range(n):
                x = int(input("Podaj wartość elementu: "))
                self.elementy.append(x)

        def pobierz_parametry(self):
            a = int(input("Podaj pierwszą wartość ciągu: "))
            r = int(input("Podaj różnicę ciągu: "))
            n = int(input("Podaj ilość elementów ciągu: "))
            self.elementy = [a + i * r for i in range(n)]

        def policz_sume(self):
            suma = sum(self.elementy)
            print("Suma elementów ciągu arytmetycznego wynosi:", suma)

        def policz_elementy(self):
            if len(self.elementy) > 0:
                n = len(self.elementy)
                a = self.elementy[0]
                r = self.elementy[1] - self.elementy[0]
                an = a + (n - 1) * r
                print("Liczba elementów ciągu arytmetycznego wynosi:", n)
                print("Ostatni element ciągu wynosi:", an)
            else:
                print("Nie wygenerowano jeszcze elementów ciągu.")


    ciag = CiagArytmetyczny()

    ciag.pobierz_elementy()

    ciag.wyświetl_dane()

    ciag.pobierz_parametry()

    ciag.wyświetl_dane()

    ciag.policz_sume()

    ciag.policz_elementy()


    #                                       ZAD_6   Stwórz klasę Robaczek, która będzie sterować ruchami Robaczka.
    # Klasa powinna przechowywać współrzędne x, y, krok (stała wartość kroku dla
    # Robaczka), i powinna mieć następujące metody:
    # •konstruktor –który nadaje wartość dla x,y i krok
    # •idz_w_gore(ile_krokow) –metoda która przesuwa robaczka o ile_krokow * krok w
    # odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
    # •idz_w_dol(ile_krokow) –metoda która przesuwa robaczka o ile_krokow * krok w odpowiednim kierunku i ustawia nowe
    # wartości współrzędnych x i y
    # •idz_w_lewo(ile_krokow) –metoda która przesuwa robaczka o ile_krokow * krok w odpowiednim kierunku i ustawia
    # nowe wartości współrzędnych x i y
    # •idz_w_prawo(ile_krokow) –metoda która przesuwa robaczka o ile_krokow * krok w odpowiednim kierunku i ustawia nowe
    # wartości współrzędnych x i y
    # •pokaz_gdzie_jestes() –metoda, która wyświetla aktualne współrzędne Robaczka
    class Robaczek:
        def __init__(self, x, y, krok):
            self.x = x
            self.y = y
            self.krok = krok

        def idz_w_gore(self, ile_krokow):
            self.y += ile_krokow * self.krok

        def idz_w_dol(self, ile_krokow):
            self.y -= ile_krokow * self.krok

        def idz_w_lewo(self, ile_krokow):
            self.x -= ile_krokow * self.krok

        def idz_w_prawo(self, ile_krokow):
            self.x += ile_krokow * self.krok

        def pokaz_gdzie_jestes(self):
            print(f"Aktualne współrzędne: x={self.x}, y={self.y}")


    robaczek = Robaczek(0, 0, 1)
    robaczek.pokaz_gdzie_jestes()
    robaczek.idz_w_gore(5)
    robaczek.pokaz_gdzie_jestes()
    robaczek.idz_w_prawo(6)
    robaczek.pokaz_gdzie_jestes()
    robaczek.idz_w_dol(2)
    robaczek.pokaz_gdzie_jestes()
    robaczek.idz_w_lewo(3)
    robaczek.pokaz_gdzie_jestes()

    import math

    #                                       ZAD_1   Napisz skrypt, który od użytkownika z konsoli pobiera dwie liczby
    # całkowite a, b. Program ma wykonać działanie a2 + ab + b2
    # Dokonaj zapisu wyniku do pliku o nazwie zadanie1.txt.
    # W skrypcie dokonaj sprawdzenia błędów związanych z wczytywanymi wartościami, do tego celu użyj składni try-except.

print("Podaj dwie liczby całkowite: ")
a = int(input("a: "))
b = int(input("b: "))
try:
    a = int(a)
    b = int(b)
    wynik = a**2 + a*b + b**2
    print("Wynik: ", wynik)
except ValueError:
    print("Podano niepoprawną wartość")
else:
    with open("zadanie1.txt", "w") as f:
        f.write(str(wynik))

#                                       ZAD_2   Napisz funkcje, która jako argumenty przyjmuje dwie listy z liczbami
# całkowitymi. Zadaniem funkcji jest utworzenie i zwrócenie nowej listy składającej się z sumy poszczególnych elementów
# z wejściowych liczb.
def sum_list(list1, list2):
    return [x+y for x,y in zip(list1, list2)]

print(sum_list([1,2,3], [4,5,6]))
#                                       ZAD_3    Dany jest plik tekst.txt. Dokonaj wczytania pliku wraz z obsługą
# polskich znaków oraz zapisz do zmiennej znaki, 35 znaków z tekstu zaczynając od 100 znaku tekstu. Następnie wyświetl
# duże litery z wczytanego fragmentu oraz ich ilość, jeśli ich nie będzie wyświetl odpowiedni komunikat.
tekst = open("tekst1.txt", "r+", encoding="utf-8")
odczyt = tekst.read()
znaki = []
duze = []
for i in range(100, 135):
    znaki.append(odczyt[i])
    if odczyt[i].isupper():
        duze.append(odczyt[i])
try:
    a = sum(1 for i in znaki if i.isupper())
    print(duze)
    print("Duże litery: ", a)
except ValueError:
    if a == 0:
        print("Nie ma dużych liter")

#                                       ZAD_4    Napisz skrypt, w którym utworzysz listę z liczbami całkowitymioraz
# zmienną ajako liczbę, a następnie za pomocą python comprehension utwórz nową listę, która będzie zawierała tylko
# elementy z pierwszej listy większe od a.
a = 5
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nowa_lista = [x for x in lista if x > a]
print(nowa_lista)

#                                       ZAD_5    Napisz skrypt, który policzy i wyświetli następujące wyrażenie:
# √𝑒3+𝑐𝑜𝑠2(39)5+(27)3+𝜋 Wynik zaokrąglij do dwóch miejsc po przecinku
ulamek = pow((2 / 7), 3)
cos = pow(math.cos(39), 2)
e = pow(math.e, 3)
pierwiastek = pow((e + cos), (1 / 5))
wynik = pierwiastek + ulamek + math.pi
print(round(wynik, 2))

#                                       ZAD_1 Dany jest plik tekst.txt. Dokonaj wczytania pliku wraz z obsługą polskich
# znaków oraz zapisz do zmiennej znaki, 40 znaków z tekstu zaczynając od 71 znaku tekstu. Następnie wyświetl tylko ilość
# litery „A” z wczytanego fragmentu, jeśli ich nie będzie wyświetl odpowiedni komunikat.
import codecs

with codecs.open("tekst.txt", "r", "utf-8") as plik:
    znaki = plik.read(40)
    print(znaki)
    if znaki.count("A") == 0:
        print("Brak litery A")
    else:
        print(znaki.count("A"))

#                                       ZAD_2 Napisz skrypt, w którym utworzysz listę z liczbami, a następnie za pomocą
# python comprehension utwórz nową listę, która będzie zawierać tylko liczby zmiennoprzecinkowe, na koniec
# wyświetl obie listy.
#Wersja 1

lista = [1, 2, 3.5, 4, 5, 6.2, 7, 8, 9.1, 10]
lista_zmiennoprzecinkowa = [x for x in lista if x % 1 != 0]
print(lista)
print(lista_zmiennoprzecinkowa)

#Wersja 2

lista = [1, 2, 3.5, 4, 5, 6.2, 7, 8, 9.1, 10]
lista_zmiennoprzecinkowa = [x for x in lista if isinstance(x, float)]
print(lista)
print(lista_zmiennoprzecinkowa)

#Wersja 3

lista = [1, 2, 3.5, 4, 5, 6.2, 7, 8, 9.1, 10]
lista_zmiennoprzecinkowa = [x for x in lista if type(x) == float]
print(lista)
print(lista_zmiennoprzecinkowa)

#Wersja 4

lista = [1, 2, 3.5, 4, 5, 6.2, 7, 8, 9.1, 10]
lista_zmiennoprzecinkowa = [x for x in lista if str(x).find('.') != -1]
print(lista)
print(lista_zmiennoprzecinkowa)

#Wersja 5

lista = [1, 2, 3.5, 4, 5, 6.2, 7, 8, 9.1, 10]
lista_zmiennoprzecinkowa = [x for x in lista if str(x).split('.')[1] != '0']
print(lista)
print(lista_zmiennoprzecinkowa)

#Wersja 6

lista = [1, 2, 3.5, 4, 5, 6.2, 7, 8, 9.1, 10]
lista_zmiennoprzecinkowa = [x for x in lista if x - int(x) != 0]
print(lista)
print(lista_zmiennoprzecinkowa)


#                                       ZAD_3 Napisz funkcje, która jako argument przyjmuje listę z liczbami dowolnego
# typu. Zadaniem funkcji jest zrobienie sumy pierwszego elementu ze wszystkimi elementami z listy, dodanie ich na koniec
# do listy wejściowej i zwrócenie jej.

def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    list.append(sum)
    return list
print(sum_list([1, 3, 3, 7]))

#                                    ZAD_4 Napisz skrypt, który policzy i wyświetli następujące wyrażenie:
# 𝑠𝑖𝑛2(56)+√4225+𝑙𝑜𝑔3854 Wynik zaokrągli do dwóch miejsc po przecinku.
wynik = pow(math.sin(56), 2) + pow(4225, 1 / 2) + math.log(3854)
print(round(wynik, 2))

#                                       ZAD_5 Napisz skrypt, który od użytkownika z konsoli pobiera liczbę
# całkowitą n. Program ma za zadanie zrobić sumęliczbod 1 do n, łącznie z n. Dokonaj zapisu wyniku do pliku o nazwie
# zadanie5.txt. W skrypcie dokonaj sprawdzenia błędów związanych z wczytywanymi wartościami, do tego celu użyj składni
# try-except.

try:
    n = int(input("Podaj liczbę całkowitą n: "))
    if n < 1:
        raise ValueError("n musi być większe lub równe 1")
except ValueError as e:
    print(f"Wystąpił błąd: {e}")
else:
    suma = sum(range(1, n+1))
    with open("zadanie5.txt", "w+") as f:
        f.write(str(suma))
    print(f"Suma liczb od 1 do {n} wynosi {suma} i została zapisana do pliku zadanie5.txt")
    
    # Napisz skrypt, w którym utworzysz listę z liczbami, a następnie za pomocą python comprehension utworzysz nową listę,
# która nie będzie zawierała minimalnego elementu z pierwszej listy. Na koniec wyświetl obie listy.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [x for x in lista if x != min(lista)]
print(lista)
print(lista2)

# Napisz funkcję, która jako argument przyjmuje słownik. Zadaniem funkcji jest zapisanie do nowo utworzonej listy pary
# elementów (klucz, wartość), jeżeli klucz oraz wartość są liczbami zmiennoprzecinkowymi. Na końcu zwróć utworzoną listę.
def zadanie(dict):
    lista = []
    for key, value in dict.items():
        if type(key) == float and type(value) == float:
            lista.append((key, value))
    return lista


# Dany jest plik tekst.txt. Dokonaj wczytania pliku wraz z obsługą polskich znaków oraz zapisz do zmiennej znaki, 41
# znaków z tekstu zaczynając od 17 znaku tekstu. Wyświetl wczytany fragment, oraz ilość wystąpień ‚c’.

with open("tekst.txt", "r", encoding="utf-8") as f:
    znaki = f.read()[16:57]
    print(znaki)
    print(znaki.count("c"))

# Napisz skrypt, który od użytkownika z konsoli pobiera trzy liczby całkowite a, n i q. Zadaniem jest policzenie n-tego
# wyrazu ciągu geometrycznego gdzie a to pierwszy wyraz ciągu, n wyraz do policzenia i q jest ilorazem ciągu. Wynik zapisz
# do pliku. Dokonaj sprawdzenia możliwych błędów z wczytywanymi wartościami za pomocą składni try-except.
try:
    a = int(input("Podaj pierwszy wyraz ciągu: "))
    n = int(input("Podaj wyraz do policzenia: "))
    q = int(input("Podaj iloraz ciągu: "))
    if n < 1:
        raise ValueError("n musi być większe lub równe 1")
    if q == 0:
        raise ValueError("iloraz nie może być równy 0")
except ValueError as e:
    print(f"Wystąpił błąd: {e}")

# Napisz skrypt, w którym utworzysz listę z liczbami, a następnie za pomocą python comprehension utwórz nową listę,
# która będzie zawierać co trzeci element z pierwszej listy. Na koniec wyświetl obie listy.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [x for x in lista if lista.index(x) % 3 == 2]
print(lista)
print(lista2)

# Napisz funkcję, która jako argument przyjmuje listę z liczbami. Zadaniem jest zrobienie sumy pierwszego i ostatniego
# elementu, oraz sprawdzenie ile elementów z listy jest większych od utworzonej sumy. Na końcu zwróć obie wartości.

def zadanie(lista):
    suma = lista[0] + lista[-1]
    ile = len([x for x in lista if x > suma])
    return suma, ile

print(zadanie([1,2,3,4,5,6,7,8,9,10]))


# Dany jest plik tekst.txt. Dokonaj wczytania pliku wraz z obsługą polskich znaków oraz zapisz do zmiennej znaki, 25
# znaków z tekstu zaczynając od 49 znaku tekstu. Wyświetl wczytany fragment, oraz ilość dużych liter.

with open("tekst.txt", "r", encoding="utf-8") as f:
    znaki = f.read()[48:73]
    print(znaki)
    print(len([x for x in znaki if x.isupper()]))

# Napisz skrypt, który od użytkownika z konsoli pobiera trzy liczby całkowite a, b i c. Zadaniem programu jest sprawdzenie
# czy z wczytanych wartości można utworzyć trójkąt prostokątny, gdzie a i b to długości przyprostokątnych, oraz c jest
# przeciwprostokątną. Jeśli z wczytanych wartości można będzie utworzyć taki trójkąt policz jego pole i zapisz wynik do
# pliki, jeżeli nie da się utworzyć trójkąta do pliku zapisz stosowny komunikat. Dokonaj sprawdzenia możliwych błędów z
# wczytywanymi wartościami za pomocą składni try-except.

try:
    a = int(input("Podaj długość przyprostokątnej a: "))
    b = int(input("Podaj długość przyprostokątnej b: "))
    c = int(input("Podaj długość przeciwprostokątnej c: "))
    if a < 1 or b < 1 or c < 1:
        raise ValueError("długości muszą być większe lub równe 1")
    if a**2 + b**2 != c**2:
        raise ValueError("nie można utworzyć trójkąta prostokątnego")
except ValueError as e:
    print(f"Wystąpił błąd: {e}")

# Napisz skrypt, który policzy i wyświetli następujące wyrażenie pow(e**4 - log2(34), 1/3 ). Wynik zaokrągli do dwóch
#miejsc po przecinku
import math
print(round(pow(math.e**4 - math.log2(34), 1/3), 2))

# Napisz skrypt, który policzy i wyświetli następujące wyrażenie pow(ln(20)+cos(45)+3, 1/3 ). Wynik zaokrągli do dwóch
# miejsc po przecinku
print(round(pow(math.log(20)+math.cos(45)+3, 1/3), 2))
    
