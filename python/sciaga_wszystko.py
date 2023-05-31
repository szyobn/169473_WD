# # # # # # # # # # # Wykresy # # # # # # # # # # # # # #

#-------------------------------------------------------------------------------------------------------------------
# Kolory i rodzaje lini
# Oznaczenia kolorów:
#
# 'b' - niebieski (blue)
# 'g' - zielony (green)
# 'r' - czerwony (red)
# 'c' - cyjan (cyan)
# 'm' - magenta (purpurowy)
# 'y' - żółty (yellow)
# 'k' - czarny (black)
# 'w' - biały (white)
# Oznaczenia stylu linii:
#
# '-' - ciągła linia
# '--' - przerywana linia
# '-.' - linia przerywano-kropkowa
# ':' - linia kropkowa
# Oznaczenia stylu punktów:
#
# '.' - kropka
# ',' - piksele
# 'o' - kółko
# 'v' - strzałka skierowana w dół
# '^' - strzałka skierowana w górę
# '<' - strzałka skierowana w lewo
# '>' - strzałka skierowana w prawo
# '1' - trójkąt skierowany w dół
# '2' - trójkąt skierowany w górę
# '3' - trójkąt skierowany w lewo
# '4' - trójkąt skierowany w prawo
# 's' - kwadrat
# 'p' - pięciokąt
# '*' - gwiazdka
# 'h' - sześciokąt1
# 'H' - sześciokąt2
# '+' - plus
# 'x' - krzyżyk
# Przykłady użycia:
#
# 'ro' - czerwone kropki
# 'g--' - zielona przerywana linia
# 'b^' - niebieskie strzałki skierowane w górę

#-----------------------------------------------------------------------------------------------------------------------------

              # # # # # # # # # # # # # # # Legenda # # # # # # # # # # # # # # # # #


# Lokalizacja legendy:
#
# 'best': Automatycznie znajduje najdogodniejsze miejsce do umieszczenia legendy.
# 'upper right': W prawym górnym rogu.
# 'upper left': W lewym górnym rogu.
# 'lower right': W prawym dolnym rogu.
# 'lower left': W lewym dolnym rogu.
# 'right': Po prawej stronie.
# 'center left': Na środku po lewej stronie.
# 'center right': Na środku po prawej stronie.
# 'lower center': Na środku na dole.
# 'upper center': Na środku na górze.
# 'center': Na środku.
#
#
# Inne ustawienia:
#
# bbox_to_anchor: Pozwala precyzyjnie określić położenie legendy w oparciu o wartości względem osi.
# title: Dodaje tytuł do legendy.
# fontsize: Określa rozmiar czcionki legendy.
# shadow: Określa, czy legenda ma mieć cień.
# frameon: Określa, czy ramka legendy ma być widoczna.
# framealpha: Określa przeźroczystość ramki legendy.
# ncol: Określa liczbę kolumn w legendzie.

#------------------------------------------------------------------------------------------------------------------------

                                 # # # # # #  # # importy # # # # # # # # # # #


import matplotlib.pyplot as plt  # Biblioteka graficzna do tworzenia wykresów
import numpy as np  # Biblioteka do manipulacji danymi numerycznymi
import pandas as pd
import seaborn as sns
#---------------------------------------------------------------------------------------------------------------------------

                                 # # # # # # Przykład wykresu # # # # # #
# x = np.array([1, 2, 3, 4])  # Tworzenie tablicy x z wartościami [1, 2, 3, 4]
# y = x**2  # Obliczanie tablicy y poprzez podniesienie każdego elementu x do kwadratu
#
# plt.plot(x, y, 'ro-')  # Tworzenie wykresu z punktami, liniami i kolorami (czerwone kropki połączone liniami)
# plt.axis([0, 6, 0, 20])  # Ustalenie zakresu osi x i y na wykresie
#
# plt.plot(x, y, 'r-')  # Tworzenie wykresu z samymi liniami
# plt.plot(x, y, 'o')  # Dodawanie punktów na wykresie
#
# plt.axis([0, 6, 0, 20])  # Ponowne ustalenie zakresu osi x i y na wykresie (min x, max x, min y, max y)
# plt.show()  # Wyświetlenie wykresu
#-----------------------------------------------------------------------------------------------------------------------------
# # Tworzenie danych do wykresu
# a = np.linspace(0, 20, 20)  # Tworzenie tablicy a zawierającej 100 równoodległych wartości od 0 do 5
#
# # Tworzenie wykresu z trzema seriami danych
# plt.plot(a, a, 'r-', label='liniowa')  # Wykres liniowy dla danych (a, a) w kolorze czerwonym, oznaczony etykietą 'liniowa'
# plt.plot(a, a**2, 'g-')  # Dodatkowa linia łącząca niebieskie kwadraty zieloną linią
# plt.plot(a, a**2, 'bs', label='kwadratowa')  # Wykres punktowy dla danych (a, a**2) z niebieskimi kwadratowymi markerami, oznaczony etykietą 'kwadratowa'
# plt.plot(a, a**3, 'g^', label='sześcienna')  # Wykres punktowy dla danych (a, a**3) z zielonymi markerami w kształcie trójkątów, oznaczony etykietą 'sześcienna'
#
# # Dodawanie legendy do wykresu
# plt.legend(loc='center left')  # Umieszczenie legendy w lewym centrum wykresu
# # plt.legend(loc='upper right', title='Legenda', fontsize='large')  # Ustawienie lokalizacji, tytułu i rozmiaru czcionki legendy
# # Wyświetlanie wykresu
# plt.show()
#---------------------------------------------------------------------------------------------------------------------------------------------------

                                            # # Macierze # #


# zera = np.zeros((3, 3), dtype='int')  # Tworzenie macierzy 3x3 wypełnionej zerami, typ danych ustawiony na 'int'
# jedynki = np.ones((4, 4))  # Tworzenie macierzy 4x4 wypełnionej jedynkami, domyślny typ danych
# print(zera)  # Wyświetlanie zawartości macierzy wypełnionej zerami
# print(jedynki)  # Wyświetlanie zawartości macierzy wypełnionej jedynkami
#
# print(zera.dtype)  # Wyświetlanie domyślnego typu danych macierzy wypełnionej zerami
# print(jedynki.dtype)  # Wyświetlanie domyślnego typu danych macierzy wypełnionej jedynkami
#
# pusta = np.empty((2, 2))  # Tworzenie "pustej" macierzy 2x2 (wartości losowe, niezainicjowane)
# print(pusta)  # Wyświetlanie zawartości "pustej" macierzy
#-----------------------------------------------------------------------------------------------------------------------------------------------

# macierz = np.array([[12, 11], [2, 1]])
# print(macierz)
#
# # Dostęp do elementów macierzy
# poz_1 = macierz[1, 1]  # Pobieranie elementu o indeksach (1, 1) - drugi wiersz, druga kolumna
# poz_2 = macierz[0][1]  # Pobieranie elementu o indeksach (0, 1) - pierwszy wiersz, druga kolumna
# print(poz_1)
# print(poz_2)
#---------------------------------------------------------------------------------------------------------------------------------------------------
# # Tworzenie tablicy liczb liniowych
# liczby_lin = np.linspace(1, 2, 5)  # Generowanie 5 równoodległych liczb między 1 a 2
# print(liczby_lin)
#-----------------------------------------------------------------------------------------------------------------------------------------------
# # Tworzenie tablicy indeksów
# z = np.indices([5, 3])  # Generowanie tablicy indeksów dla macierzy o wymiarach 5x3
# print(z)
# print(z[0][1][2])  # Pobieranie elementu o indeksach (0, 1, 2)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
# # Tworzenie macierzy diagonalnej
# mat_diag = np.diag([a for a in range(5)])  # Tworzenie macierzy diagonalnej o wartościach od 0 do 4
# print(mat_diag)
#
# # Tworzenie macierzy diagonalnej z przesunięciem
# mat_diag1 = np.diag([a for a in range(5)], k=1)  # Tworzenie macierzy diagonalnej o wartościach od 0 do 4, przesunięcie o 1 w górę
# mat_diag2 = np.diag([a for a in range(5)], k=-1)  # Tworzenie macierzy diagonalnej o wartościach od 0 do 4, przesunięcie o 1 w dół
# print(mat_diag1)
# print(mat_diag2)
#-------------------------------------------------------------------------------------------------------------------------------------------------------

# # Tworzenie macierzy
# mat = np.arange(25)
# mat = mat.reshape((5, 5))  # kształt macierzy
# print(mat)
#
# # Wyjmowanie wierszy od drugiego wiersza do końca
# print(mat[1:])
#
# # Wyjmowanie pierwszego wiersza jako wektora
# print(mat[:1])
#
# # Wyjmowanie wszystkich kolumn oprócz ostatniej
# print(mat[:, :-1])
#
# # Wyjmowanie 2 i 3 kolumny dla 3, 4, 5 wiersza
# print(mat[2:5, 1:3])
#
# # Wyjmowanie 3 i 5 kolumny dla wszystkich wierszy
# print(mat[:, [2, 4]])
#
# # Tworzenie nowej linii
# print('')
#------------------------------------------------------------------------------------------------------------------------------------------
# # Tworzenie macierzy
# x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
# print(x)
#
# # Tworzenie tablicy indeksów do wyjmowania elementów
# rows = np.array([[0, 0], [3, 3]])
# cols = np.array([[0, 2], [0, 2]])
#
# # Wyjmowanie elementów o indeksach zdefiniowanych w tablicach rows i cols
# y = x[rows, cols]
# print(y)

#------------------------------------------------------------------------------------------------------------------------------------------

                                                     # # # # Tablice # # # #


# a = np.array([[0, 1], [2, 3]])  # Tworzenie dwuwymiarowej tablicy (macierzy) a za pomocą list zagnieżdżonych
# # Pierwsza lista [0, 1] reprezentuje pierwszy wiersz macierzy a
# # Druga lista [2, 3] reprezentuje drugi wiersz macierzy a
# print(a)  # Wyświetlenie zawartości macierzy a
#------------------------------------------------------------------------------------------------------------------------------------------

# a = np.arange(2, 5, 0.5)  # (od ilu, do ilu, z jakim skokiem)
# print(a)  # Wyświetlenie zawartości tablicy a
# print(type(a))  # Wyświetlanie typu danych
#------------------------------------------------------------------------------------------------------------------------------------------
# # Tworzenie tablicy znakowej z bufora
# znaki = b'ogolna'
# z1 = np.frombuffer(znaki, dtype='S1')  # Tworzenie tablicy znakowej, gdzie każdy znak jest reprezentowany jako bajt
# print(z1)
#
# z2 = np.frombuffer(znaki, dtype='S2')  # Tworzenie tablicy znakowej, gdzie każdy znak jest reprezentowany jako dwa bajty
# print(z2)
#
# # Tworzenie tablicy znakowej z ciągu znaków
# znaki = 'ogolna'
# z3 = np.array(list(znaki))  # Tworzenie tablicy znakowej, gdzie każdy znak jest reprezentowany jako pojedynczy znak
# z4 = np.array(list(znaki), dtype='S1')  # Tworzenie tablicy znakowej, gdzie każdy znak jest reprezentowany jako bajt
# z5 = np.array(list(b'ogolna'))  # Tworzenie tablicy znakowej z bufora bajtowego
# z6 = np.fromiter(znaki, dtype='S1')  # Tworzenie tablicy znakowej, gdzie każdy znak jest reprezentowany jako bajt
# print(z3)
# print(z4)
# print(z5)
# print(z6)
#--------------------------------------------------------------------------------------------------------------------------------------------
# # Cięcia tablicy
# a = np.arange(10)
# print(a)
#
# s = slice(2, 7, 2)  # Definicja cięcia od indeksu 2 do 7 z krokiem 2
# print(a[s])
#
# # Inny sposób cięcia, jak w liście
# print(a[2:7:2])  # Cięcie od indeksu 2 do 7 z krokiem 2
#
# # Wyjmowanie konkretnych elementów
# print(a[1:])  # Wyjmowanie elementów od indeksu 1 do końca
# print(a[2:5])  # Wyjmowanie elementów od indeksu 2 do 4 (indeks 5 jest wykluczony)


#------------------------------------------------------------------------------------------------------------------
                               # # # # # # # # Odczyt pliku # # # # # # # # # # #


# # Wczytywanie danych z pliku CSV 'iris.data' do obiektu DataFrame (df)
# df = pd.read_csv('iris.data', header=0, sep=',', decimal='.')
#
# # Wyświetlanie zawartości DataFrame df
# print(df)
#
# # Tworzenie wykresu liniowego (lineplot) przy użyciu biblioteki Seaborn
# # Parametr data=df określa, że dane pochodzą z DataFrame df
# # Parametr x=df.index określa, że wartości na osi X będą indeksami DataFrame df
# # Parametr y='sepal length' określa, że wartości na osi Y będą pochodzić z kolumny 'sepal length'
# # Parametr hue='class' określa, że linie na wykresie będą różnionie w zależności od wartości w kolumnie 'class'
# # Parametr palette=['yellow', 'green', 'red'] określa paletę kolorów dla poszczególnych klas
# sns.lineplot(data=df, x=df.index, y='sepal length', hue='class', palette=['yellow', 'green', 'red'])
#
# # Dodawanie etykiety dla osi X
# plt.xlabel('indeksy')
#
# # Dodawanie etykiety dla osi Y
# plt.ylabel('Wykres liniowy danych z Iris dataset')
#
# # Wyświetlanie wykresu
# plt.show()

#-----------------------------------------------------------------------------------------------------------------------------------------

# # Wczytywanie danych z pliku CSV 'dane.csv' do obiektu DataFrame (df)
# df = pd.read_csv('dane.csv', header=0, sep=";", decimal=".")
#
# # Wyświetlanie zawartości DataFrame df
# print(df)
#
# # Grupowanie danych w kolumnie 'Wartość zamówienia' po wartościach w kolumnie 'Imię i nazwisko' i obliczanie sumy
# seria = df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()
#
# # Tworzenie wykresu kołowego (pie chart) przy użyciu funkcji plt.pie()
# # Parametr x=seria określa dane, które mają być przedstawione na wykresie kołowym
# # Parametr labels=seria.index określa etykiety dla poszczególnych części wykresu
# # Parametr autopct=lambda pct: "{:.1f}%".format(pct) określa formatowanie etykiet procentowych na wykresie
# # Parametr textprops=dict(color='black') określa, że etykiety tekstu będą miały czarny kolor
# # Parametr colors=['red', 'green'] określa kolory dla poszczególnych części wykresu kołowego
# wedges, texts, autotext = plt.pie(x=seria, labels=seria.index,
#                                   autopct=lambda pct: "{:.1f}%".format(pct),
#                                   textprops=dict(color='black'),
#                                   colors=['red', 'green'])
#
# # Dodawanie tytułu dla wykresu
# plt.title('Suma zamówień dla sprzedawców')
#
# # Dodawanie legendy do wykresu w dolnym prawym rogu
# plt.legend(loc='lower right')
#
# # Dodawanie etykiety dla osi Y
# plt.ylabel('Procentowy wynik wartości zamówień')
#
# # Wyświetlanie wykresu
# plt.show()
#------------------------------------------------------------------------------------------------------------------------------------