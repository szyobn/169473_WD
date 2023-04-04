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
