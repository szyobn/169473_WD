# a = 'a'
# print(a)
#
# #dodanie elementu na pozycje
# zad1 = ['ala','basia','ula']
# zad1.append('ewa')
# print(zad1)
# #dodanie kilku elementów na koniec listy
# zad2 = [1,2,3]
# test = [4,5,6]
# zad2.insert(3,test)
# print(zad2)
# #usuwanie elemenntu po indeksie
# zad3 = [1,2,3]
# zad3.pop(1)
# print(zad3)
# #usuwanie elementu po wartości elementu
# zad4 = [1,2,3]
# zad4.remove(1)
# print(zad4)
# #odwórcenie listy
# zad5 = ['ala','elwelina','basia','lili']
# zad5.reverse()
# print(zad5)
# #sortowanie
# zad6 = ['ala','elwelina','basia','lili']
# zad6.sort()
# print(zad6)
#
# slownik = {'a':1,3:1,5:'b','a':5}
# print(slownik)
# print(slownik['a'])
# print(slownik.keys())
# print(slownik.values())
#
# print('a =%(zm)d'%{'zm':12})
# print('a = {}'.format(1))


#instrukcja warunkowa if :
#   instrukcja 1
#   instrukcja 2
# elif warunek 2:
#   instrukcja 1
#   instrukcja 2
#else:
#   instrukcja 1
#   instrukcja 2
# a = input('podaj a: ')
# b = input('podaj b: ')
# print(a)
# print(b)
# print(type(a))

#if a>b:
 #   print('a= '+str(a))
#elif a < b:
 #       print('b= ' + str(b))
#else:
 #   print("a i b sa rowne")

#for element in sekwencja:
#   instrukcja 1
#   instrukcja 2
#else:
#   instrukcja 1
#   instrukcja 2
#for x in range(1,6,1):
#    print(x)
 #   print("")

#range(start,stop,step) for(int i =0, i < lista.count(), i++)

#while element in sekwencja:
#   instrukcja 1
#   instrukcja 2
#else:
#   instrukcja 1
#   instrukcja 2
#

# liczby = [3,45,3,2,1]
# licznik = 0
# a = int(input('podaj a: '))
# while licznik != len(liczby):
#     if a - liczby[licznik] == 0:
#         print('{} - {} = 0'.format(a, liczby[licznik]))
#         break
#         licznik +=1


liczby = [1,2,2,2,2,3]
licznik = 0;

while licznik != len(liczby):
     if liczby[licznik] == 2:
         liczby.remove(liczby[licznik])

     else:
         licznik +=1

print(liczby)