# --- zad 1 Wygeneruj liczby z przedziału <0,30>, następnie pomnóż je przez 2 i zapisz do pliku
import random
liczby1 = [random.randint(0, 30) for i in range(30)]
liczby2 = [2 * liczba for liczba in liczby1]

with open("liczby.txt", "w") as plik:
    for liczba in liczby2:
        plik.write(str(liczba) + "\n")

# --- zad 2 Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość

with open("liczby.txt", "r") as plik:
    lines = plik.readlines()

for line in lines:
    print(line.strip())

# --- zad 3 Wykorzystując komendę with zapisz kilka linijek tekstu do pliku a następnie wyświetl je na ekranie.

with open("tekst.txt", "w", encoding="utf8") as f:
    f.write(
        "Litwo! Ojczyzno moja! Ty DDjesteś jak zdrowie. Nazywał się niedawno w wielkiej peruce, którą do ojca Podkomorzego,")
    f.write(
        "Mościwego Pana zastępuje i bagnami skradał się dowie kto go myślano do dworu. Tu Kościuszko w polskiej szacie ")
    f.write(
        "siedzi jak noga moja nie mogą. Słońce ostatnich nie czytano w Pańskim pisano zakonie i z Warszaw mam list, ")
    f.write("to mówiąc, że nasi synowie i wróciwszy w miechu. Starzy na to mówiąc, że go kaznodzieją, że zamczysko ")
    f.write(
        "wzięliśmy w posiadłość. Wszakże kto cię stracił. Dziś człowieka rodu, obyczajów! Dość, że oko pańskie jachał ")
    f.write("szlachcic młody panek i już to mówiąc, że nasi synowie i nazwisko.")
with open("tekst.txt", "r", encoding="utf8") as f:
    for line in f:
        print(line.strip())

# --- zad 4 Stwórz klasę NaZakupy, która będzie przechowywać atrybuty:
# •nazwa_produktu, ilosc, jednostka_miary, cena_jed •oraz metody:
# •konstruktor –który nadaje wartości
# •wyświetl_produkt()
# –drukuje informacje o produkcie na ekranie
# •ile_produktu() –informacje ile danego produktu ma być czyli ilosc + jednostka_miary np. 1 szt., 3 kg itd.
# •ile_kosztuje()
# –oblicza ile kosztuje dana ilość produktu np. 3 kg ziemniaków a cena_jed wynosi 2 zł/kg wówczas funkcja powinna zwrócić wartość 3*2


class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        print(f"Nazwa produktu: {self.nazwa_produktu}")
        print(f"Ilość: {self.ilosc} {self.jednostka_miary}")
        print(f"Cena za jednostkę: {self.cena_jed} zł")

    def ile_produktu(self):
        return f"{self.ilosc} {self.jednostka_miary}"

    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed

# --- zad 5 twórz klasę, która definiuje ciągi arytmetyczne. Wartości powinny być przechowywane jako atrybut. Klasa powinna mieć metody:
# •wyświetl_dane –drukuje elementy na ekran
# •pobierz_elementy–pobiera konkretne wartości ciągu od użytkownika
# •pobierz_parametry –pobiera pierwsza wartość i różnicę od użytkownika oraz ilość elementów ciągu do wygenerowania.
# •policz_sume –liczy sume elementow•policz_elementy –liczy elementy jeśli pierwsza wartość i różnica jest podana
#•policz_elementy –liczy elementy jeśli pierwsza wartość i różnica jest podana
# Stwórz instancję klasy i sprawdź działanie wszystkich metod.


class CiagArytmetyczny:
    def __init__(self):
        self.elementy = []

    def wyswietl_dane(self):
        print("Elementy ciągu:", self.elementy)

    def pobierz_elementy(self):
        n = int(input("Liczba elementów ciągu: "))
        self.elementy = [float(input(f"Podaj {i}-ty element ciągu: ")) for i in range(1, n + 1)]

    def pobierz_parametry(self):
        a1 = float(input("Pierwszy element ciągu: "))
        r = float(input("Różnica ciągu: "))
        n = int(input("Liczba elementów do wygenerowania: "))
        self.elementy = [a1 + i * r for i in range(n)]

    def policz_sume(self):
        suma = sum(self.elementy)
        print("Suma elementów ciągu: ", suma)

    def policz_elementy(self, a, r, n):
        self.elementy = [a + i * r for i in range(n)]
        print("Elementy ciągu: ", self.elementy)


ciag = CiagArytmetyczny()

ciag.pobierz_elementy()
ciag.wyswietl_dane()

ciag.pobierz_parametry()
ciag.wyswietl_dane()

ciag.policz_sume()

ciag.policz_elementy(1, 3, 5)

# --- zad 6 Stwórz klasę Robaczek, która będzie sterować ruchami Robaczka. Klasa powinna przechowywać współrzędne x, y, krok (stała wartość kroku dla Robaczka), i powinna mieć następujące metody:
# •konstruktor –który nadaje wartość dla x,y i krok•idz_w_gore(ile_krokow) –metoda która przesuwa robaczka o ile_krokow * krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# •idz_w_dol(ile_krokow) –metoda która przesuwa robaczka o ile_krokow * krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# •idz_w_lewo(ile_krokow) –metoda która przesuwa robaczka o ile_krokow * krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# •idz_w_prawo(ile_krokow) –metoda która przesuwa robaczka o ile_krokow * krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# •pokaz_gdzie_jestes() –metoda, która wyświetla aktualne współrzędne RobaczkaStwórz instancję klasy i sprawdź jak działają wszystkie metody
#Stwórz instancję klasy i sprawdź jak działają wszystkie metody

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
        print("Aktualne współrzędne: x =", self.x, ", y =", self.y)

        robaczek = Robaczek(0, 0, 5)
        robaczek.idz_w_gore(2)
        robaczek.idz_w_lewo(1)
        robaczek.idz_w_dol(1)
        robaczek.idz_w_prawo(3)
        robaczek.pokaz_gdzie_jestes()

