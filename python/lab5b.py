#ZAD 1  Dany jest plik tekst.txt. Dokonaj wczytania pliku wraz z obsługą polskich znaków oraz zapisz do zmiennej znaki, 40 znaków z tekstu zaczynając od 71znaku tekstu.
# Następnie wyświetl tylko ilość litery „A” z wczytanego fragmentu, jeśli ich nie będzie wyświetl odpowiedni komunikat.
with open('tekst.txt', 'r', encoding='utf-8') as f:
    tekst = f.read()

znaki = tekst[71:111]

liczba_A = znaki.count('A')

if liczba_A > 0:
    print("Liczba liter 'A' w fragmencie: ", liczba_A)
else:
    print("Nie ma liter 'A' w fragmencie.")
#ZAD 2 Napisz skrypt, w którym utworzysz listę z liczbami, a następnie za pomocą python comprehension utwórz nową listę,
# która będzie zawierać tylko liczby zmiennoprzecinkowe, na koniec wyświetl obie listy
liczby = [1, 2, 3.5, 4, 5.8, 6, 7.3, 8, 9.2, 10]
liczby_zmiennoprzecinkowe = [x for x in liczby if isinstance(x, float)]

print("Lista wszystkich liczb: ", liczby)
print("Lista liczb zmiennoprzecinkowych: ", liczby_zmiennoprzecinkowe)
#ZAD 3 Napisz funkcje, która jako argument przyjmuje listę z liczbami dowolnego typu.
# Zadaniem funkcji jest zrobienie sumy pierwszego elementu ze wszystkimi elementami z listy, dodanie ich na koniec do listy wejściowej i zwrócenie je
def suma_pierwszego_elementu(lista):
    suma = sum(lista[1:])  # oblicz sumę wszystkich elementów oprócz pierwszego
    lista.append(suma + lista[0])  # dodaj sumę na końcu listy wraz z pierwszym elementem
    return lista

przykladowa_lista = [1, 2, 3, 4, 5]
zmodyfikowana_lista = suma_pierwszego_elementu(przykladowa_lista)
print(zmodyfikowana_lista)
#ZAD 4  Napisz skrypt, który policzy i wyświetli następujące wyrażenie: 𝑠𝑖𝑛2(56)+√4225+𝑙𝑜𝑔3854 Wynik zaokrągli do dwóch miejsc po przecinku.
import math

wynik = math.sin(56)**2 + math.sqrt(4)*(4**2/25) + math.log(85)
wynik = round(wynik, 2)
print("Wynik to:", wynik)
#ZAD 5 Napisz skrypt, który od użytkownika z konsoli pobiera dwie liczby całkowite n.
# Program ma za zadanie zrobić sumęliczbod 1 do n, łącznie z n. Dokonaj zapisu wyniku do pliku o nazwie zadanie5.txt. W skrypcie dokonaj sprawdzenia błędów związanych z wczytywanymi wartościami, do tego celu użyj składni try-except.
try:
    n = int(input("Podaj liczbę całkowitą n: "))
    suma = int(sum(range(1, n+1)))
    with open("zadanie5.txt", "w") as plik:
        plik.write(f"Suma liczb od 1 do {n}  wynosi: {suma}")
        plik.close()
    print(f"Suma liczb od 1 do {n} wynosi: {suma}")
except ValueError :
    print(f"Wystąpił błąd:")

