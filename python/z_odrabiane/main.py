# import numpy as np
# # inicjalizacja tablicy
# a = np.array([90,1])
# print(a)
# # lub drugi sposób
# # a = np.array(2,5,0.1)
# print(a)
# # wypisywanie typu zmiennej tablicy
# print(type(a))
# # sprawdza typ danych tablicy
# print(a.dtype)
# # inicjalizacja tablicy z konkretnym typem danych
# a = np.arange(2, dtype='int64')
# print(a.dtype)
# b = a.astype('float')
# print(b)
# print(b.dtype)
# # wpisywanie rozmiaru tablicy
# print(b.shape)
# #  można też sprawdzić ilość wymiarów tablicy
# print(a.ndim)
# # stworzenie tablicy wielowymiarowej może wyglądać tak
# # parametrem przekazywanym do funkcji array jest obiekt,
# # może to być pythonowa lista
# m = np.array([np.arange(2), np.arange(2)])
# print(m.shape)
# # ponownie typem jest ,darray
# print(type(m))
#
# zera =np.zeros((5, 5))
# jedynki = np.ones((4, 4))
# print(zera)
# print(jedynki)
# # warto sprawdzić jaki jest domyślny typ danych takich
# print(zera.dtype)
# print(jedynki.dtype)
# # stworzenie pustej macierzy i podanych wymiarach
# # wartości umieszczane są losowo,najpierw podawana jest
# pusta = np.empty((2,2))
# print(pusta)
# #
# macierz = np.array([[12, 11], [2,1]])
# print(macierz)
# # do elementów tablicy możemy odwołać sie tak jak do elementu
# poz_1 = macierz[1, 1]
# poz_2 = macierz[0][1]
# print(poz_1)
# print(poz_2)
# # stworzenie macierzy 2x2 wraz z uzupełnieniem
#
#
# # funkcja linspace
#
# liczby_lin = np.linspace(1,2,5, endpoint=False)
# print(liczby_lin)
# # a teraz morzemy utworzyć dwie macierze
# z =np.indices((5, 3))
# print(z)
# print(z[0][1][2])
#
# # macierz diagonalna
# mat_diag = np.diag([a for a in range(5)])
# print(mat_diag)
# znaki = 'ogolna'
# z3 = np.array(list(znaki))
# z4 = np.array(list(znaki), dtype='S1')
# z5 = np.array(list(b'ogolna'))
# z6 = np.fromiter(znaki, dtype='S1')
#
# print(z3)
# print(z4)
# print(z5)
# print(z6)
#
#
# # zad1
#
# zad1 = np.arange(4, 81, 4)
# print(zad1)
#
# # zad2
# lista = [1.1, 2.2, 3.3, 4.4, 5.5]
#
#
# zad2 = np.array(lista)
# zad2_int32 = zad2.astype(np.int32)
#
# print("Tablica int32:", zad2_int32)
#
# # zad3
# def n2(n):
#
#     zad3 = np.zeros((n, n), dtype=int)
#     for i in range(n):
#         for j in range(n):
#             zad3[i][j] = 2**(i+j)
#
#
#     return zad3
#
#
#     test = n2(4)
#     print(test)
#
#
# #zad4
#
# def zad4(a,b)

import numpy as np
# Zad1
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
#
# wynik = np.sum(a * b)
#
# print(wynik)
# zad2
# macierz = np.array([[12, 11,1,2], [2,1,3,4], [2,1,3,4], [2,1,3,4]])
# macierz2 = np.array([[2,1,3,4], [2,1,3,4], [2,1,3,4]])
# print(macierz)
# print(macierz2)
# print("Najniższe wartości rzędu:")
# print(np.min(macierz2, axis=1))
# print("Najniższe wartości kolumny:")
# print(np.min(macierz2, axis=0))
# print("Najniższe wartości rzędu:")
# print(np.min(macierz, axis=1))
# print("Najniższe wartości kolumny:")
# print(np.min(macierz, axis=0))

# Zad3
# wynik = np.dot(a , b)
# print(wynik)

# Zad4
# a = np.array([1, 2, 3], dtype=int)
#
#
# b= np.array([2.5, 3.5, 4.5], dtype=float)
#
#
# wynik= np.dot(a, b)
#
# print(wynik)
# Zad5
# b = np.array([[1, 2, 3], [4, 5, 6]])
#a = np.sin(b)
#
# print(a)
# Zad6
# b= np.array([[1, 2, 3], [4, 5, 6]])
#
# a = np.cos(b)
#
# print(a)
# Zad7
# a = np.array([[1, 2, 3], [4, 5, 6]])
# a = np.sin(a)
#
# b = np.array([[4.5, 1.5, 2.5], [3.4, 4.5, 5.5]])
# b = np.cos(b)
# c = a + b
# print(c)
# Zad8
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# for i in a:
#  print(i)
 # Zad9
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# for i in a.flat:
#  print(i)
# Zad10
# a = np.arange(81).reshape(9, 9)
# b = a.reshape(3, 27)
# c = a.reshape(27, 3)
# d = a.reshape(81, 1)
# print(b)
# print(c)
# print(d)

# Zad11
flat_a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

b = flat_a.reshape((3, 4))

c = flat_a.reshape((4, 3))

d = flat_a.reshape((2, 6))

flat_b = b.flatten()
flat_c = c.flatten()
flat_d = d.flatten()

print("Macierz 3x4:")
print(b)
print(flat_b)

print("Macierz 4x3:")
print(c)
print(flat_c)

print("Macierz 2x6:")
print(d)
print(flat_d)



