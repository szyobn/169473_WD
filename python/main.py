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

#ZAD1
arr = np.arange(20) * 4
print(arr)
#ZAD2
lst_float = [1.2, 2.3, 3.4, 4.5, 5.6]
lst_int32 = np.array(lst_float, dtype='int32')
print(lst_int32)
#ZAD3
def podwa(n):
    return np.array([2 ** i for i in range(n*n)]).reshape((n, n))
print(podwa(3))
#ZAD4

def generuj(base, n):
    return np.logspace(0, n-1, n, base=base)
print(generuj(2, 4))
#ZAD5

def macierz(n):
    reversed_vector = np.arange(n)[::-1]
    diagonal_vector = np.diag(reversed_vector, k=2)
    return diagonal_vector
print(macierz(5))
#ZAD6

words = ['PYTHON', 'NUMPY', 'ARRAY', 'MATRIX']

n_rows = len(words)
n_cols = max(len(word) for word in words)

matrix = np.zeros((n_rows, n_cols), dtype='U1')

for i, word in enumerate(words):
    matrix[i, :len(word)] = list(word)

for i in range(n_rows):
    for j in range(n_cols):
        if matrix[i, j] != '':
            print(matrix[i, j], end=' ')
        else:
            print(' ', end=' ')
    print()

diagonal_word = 'NUM'
for i in range(len(diagonal_word)):
    matrix[i, n_cols-len(diagonal_word)+i] = diagonal_word[i]

print()
for i in range(n_rows):
    for j in range(n_cols):
        if matrix[i, j] != '':
            print(matrix[i, j], end=' ')
        else:
            print(' ', end=' ')
    print()
#ZAD7

def genmacierz(n):
    
    matrix = np.zeros((n, n), dtype=int)

    
    for i in range(n):
        matrix[i, i] = 2 * (i + 1)
        if i < n - 1:
            matrix[i, i + 1] = 2 * (i + 1)
            matrix[i + 1, i] = 2 * (i + 1)

    return matrix
#ZAD8

def array(arr, direction):
    if direction == 'vertical':
        if arr.shape[0] % 2 != 0:
            print('Ilość wierszy nie pozwala na operację.')
            return arr
        else:
            half = arr.shape[0] // 2
            return arr[:half], arr[half:]
    elif direction == 'horizontal':
        if arr.shape[1] % 2 != 0:
            print('Ilość kolumn nie pozwala na operację.')
            return arr
        else:
            half = arr.shape[1] // 2
            return arr[:, :half], arr[:, half:]
    else:
        print('Nieprawidłowy kierunek podziału.')
        return arr
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(arr)

  
    arr1, arr2 = divide_array(arr, 'vertical')
    print(arr1)
    print(arr2)

 
    arr3, arr4 = divide_array(arr, 'horizontal')
    print(arr3)
    print(arr4)

    
    arr5 = divide_array(arr, 'wrong')
    print(arr5)

    #ZAD9

    arr = np.arange(1, 26)

    arr = arr.reshape((5, 5))

    print(arr)
