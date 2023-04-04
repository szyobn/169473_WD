#zadanie 1 Napisz skrypt, który od użytkownika z konsoli pobiera trzy liczby całkowite a, b. Program ma wykonać działanie a2 + ab + b2
#Dokonaj zapisu wyniku do pliku o nazwie zadanie1.txt. W skrypcie dokonaj sprawdzenia błędów związanych z wczytywanymi wartościami, 
#do tego celu użyj składni try-excep
a=int(input("podaj liczbę a: "))

b=int(input("podaj liczbę b:" ))
print(a * a + a * b + b * b)


#zadanie 2 Napisz funkcje, która jako argumenty przyjmuje dwie listy z liczbami całkowitymi.
#Zadaniem funkcji jest utworzenie i zwrócenie nowej listy składającej się z sumy poszczególnych elementów z wejściowych liczb
lista1=[2,5,7,3,2,7]
lista2=[6,44,8,2,8]
lista3=[]
lista3.append(lista1[2]+lista2[3])
print(lista3)

#zadanie 3 Dany jest plik tekst.txt. Dokonaj wczytania pliku wraz z obsługą polskich znaków oraz zapisz do zmiennej znaki, 35 znaków z tekstu zaczynając od 100 znaku tekstu. 
#Następnie wyświetl duże litery z wczytanego fragmentu oraz ich ilość, jeśli ich nie będzie wyświetl odpowiedni komunikat. 
tekst= open("tekst1.txt", "r+", encoding="utf-8 ")
    tekst=tekst.read()
    znaki=[]
    litery=[]
    for i in range(100, 135):
        znaki.append(tekst[i])
        if tekst[i].isupper():
        litery.append(tekst[i])
        try:
            a=sum(1 for i in znaki if i.supper())
            print(litery)
            print("litery:", a)
        except ValueError:
            if a==0:
                print("nie ma litter")

#zadanie 4  Napisz skrypt, w którym utworzysz listę z liczbami całkowitymi oraz zmienną a jako liczbę, a następnie za pomocą python comprehension utwórz nową listę
# która będzie zawierała tylko elementy z pierwszej listy większe od a.
import math
lista=[2,5,7,2]
a=10
zadanie4=[lista[i] for i in range(len(lista)) if lista[i]>b]
print(zadanie4)

#zadanie 5  Napisz skrypt, który policzy i wyświetli następujące wyrażenie: √𝑒3+𝑐𝑜𝑠2(39)5+(27)3+𝜋Wynik zaokrągli do dwóch miejsc po przecinku
a=pow((2/7),3)
cos=pow(math.cos(39),2)
e=pow(math.e, 3)
b=pow((e+cos),(1/5))
wynik=a+b+math.pi
print(round(wynik, 2))


