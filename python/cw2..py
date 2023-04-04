

import math
#                           ZAD_1a
e = math.exp(10)
print(e)
#                           ZAD_1b
y = math.pow(math.log(5+math.pow(math.sin(8), 2)), 1/6)
print(y)

#                           ZAD_1c
zad1c= math.floor(3.55)
print(zad1c)
#                           ZAD_1d
zad1d = math.ceil(4.8)
print(zad1d)
#    ZAD_2 Zapisz swoje imie i nazwisko w oddzielnych zmiennych wszystkie wielkimi literami. Użyj odpowiedniej metody by wyświetlić je pisane tak, że pierwsza litera jest wielka a pozostałe małe. (trzeba użyć metody capitalize)
imie= "Tomasz"
nazwisko = "Szafranski"
imiee = imie.capitalize()
nazwiskoo = nazwisko.capitalize()
print(imiee, nazwiskoo)
#     ZAD_3 Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu piosenki z powtarzającymi się słowami np. „la la la”. Następnie użyj odpowiedniej funkcji, która zliczy występowanie słowa „la”. (trzeba użyć metody count)
tekst = "La la la, la la la, la la la"

l_tekst = tekst.count("la")

print("Liczba wystąpień słowa 'la':", l_tekst)
#    ZAD_4  Do poszczególnych elementów łańcucha możemy się odwoływać przez podanie indeksu. Np. pierwszy znak zapisany w zmiennej imie uzyskamy przez imie[0]. Zapisz dowolną zmienną łańcuchową i wyświetl jej drugą i ostatnią literę, wykorzystując indeksy.
x="siała"
print(x[1], x[4])
#    ZAD_5 Zmienne łańcuchowe możemy dzielić, wykorzystaj zmienną z Zad. 6 i spróbuj ją podzielić na poszczególne wyrazy. (trzeba użyć metody split)
x = tekst.split(" ")
print(x)
#   ZAD_6 Napisz skrypt, w którym zadeklarujesz zmienne typu: string, float i szestnastkowe. Następnie wyświetl je wykorzystując odpowiednie formatowanie.
strings = "Hello, world!"
floats = 3.14159
szesntastkowy = 0xFF
print("String: {}".format(strings))
print("Float: {:.2f}".format(floats))
print("Hexadecimal: {}".format(hex(szesntastkowy)))
#    ZAD_7 Napisz skrypt, w którym tworzysz listę ulubionych sportów, odwróć ją a następnie dodaj mniej lubiane sporty na sam koniec.
sporty = ['narciarstwo', 'onewheel', 'downhill']
sporty.reverse()
print(sporty)
sporty.extend(['hokej', 'golf'])
#     ZAD_8  Stwórz słownik skrótów powszechnie używanych w gazetach lub artykułach internetowych. Jako klucz przyjmij skrót danego słowa, wartość to rozwinięcie tego skrótu.
skroty = {
    "np.": "na przykład",
    "itd.": "i tym podobne",
    "tj.": "to jest"
}
for skrot, rozw in skroty.items():
    print("{} - {}".format(skrot, rozw))
#    ZAD_9 Stwórz słownik z ulubionymi grami komputerowymi. Pomyśl, co może być kluczem a co wartością w takim słowniku. Policz liczbę elementów w słowniku.
gry = {
    "GTA": "Grand Theft Auto",
    "CS": "Counter strike",
    "LOL": "League of legends"
}
print(len(gry))
#      ZAD_10 Napisz skrypt, który pobiera od użytkownika zdanie i liczy wystąpienia litery a. Użyj funkcji input
a = input("Napisz tekst: ")
l_a = a.count("a")
print("Liczba wystąpień słowa 'a':", l_a)
#    ZAD_11 Wczytaj trzy liczby całkowite a,b,c i sprawdź, która z nich jest największa. W zależności od wyniku wyświetl odpowiedni komunikat.
zad11a = int(input("Podaj pierwszą liczbę całkowitą: "))
zad11b = int(input("Podaj drugą liczbę całkowitą: "))
zad11c = int(input("Podaj trzecią liczbę całkowitą: "))

if zad11a > zad11b and zad11a > zad11c:
    print("Największa liczba to", zad11a)
elif zad11b > zad11a and zad11b > zad11c:
    print("Największa liczba to", zad11b)
else:
    print("Największa liczba to", zad11c)
#    ZAD_12 Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i float. Następnie za pomocą użycia pętli for podnieś każdą liczbę do kwadratu.

lista = [1, 2.2, 3, 4.25, 5]
for i in range(len(lista)):
    lista[i] = lista[i] ** 2
print(lista)
#   ZAD_13 Napisz skrypt, który za pomocą pętli while pobiera 10 liczb, następnie dodaje do listy tylko parzyste liczby.
l_parzyste = []
licznik = 0
while licznik < 10:
    liczba = int(input("Podaj liczbę do zadania 13: "))
    if liczba % 2 == 0:
        l_parzyste.append(liczba)
    licznik += 1
print("Liczby parzyste:", l_parzyste)