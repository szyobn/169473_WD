#                                                               LAB1:

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


# liczby = [1,2,2,2,2,3]
# licznik = 0;
#
# while licznik != len(liczby):
#      if liczby[licznik] == 2:
#          liczby.remove(liczby[licznik])
#
#      else:
#          licznik +=1
#
# print(liczby)

#                                                           LAB2:
import math
# Zad.1
# x=math.exp(10)
# print(x)

# y = math.pow(math.log(5+math.pow(math.sin(8),2)),1/6)
# print(y)

# z = math.floor(3.55)
# print(z)
# q = math.ceil(4.80)
# print(q)


# Zad.2
# imie="SZYMON"
# nazwisko = "OBNISKI"
# print(imie.capitalize(),nazwisko.capitalize())

# Zad.3
# fragment = "Tequila Tequila Tequila"
# # Tekst pochodzi z https://www.tekstowo.pl/piosenka,the_champs,tequila.html"
# print(fragment.count('Tequila'))

# Zad.4
# imie="szymon"
# print(imie[0],imie[len(imie)-1])

#Zad.5

# print(fragment.split())

# Zad.6

#
# a = "mniej niż zero"
# b = 2.342
# c = 0xFF1E
#
#
# print(a)
# print(b)
# print("{:X}".format(c))


# Zad.7
# sport = ["nożna","ręczna","siatkówka","siłka"]
# odwr = list(reversed(sport))
# odwr.append("boks")
# print(odwr)

# Zad.8
# skrot= {'jj':'juz jetsem','z/w':'zaraz wracam'}
# print(skrot)

# Zad.9
# skrot= {'minecraft':'klocek','call_of_duty':'RPG'}
# dlugosc = len(skrot)
# print(skrot,dlugosc)
# Zad.10
# x = input()
# y = 0
# for i in x:
#     if i =="a" or i=="A":
#         y+=1
# print(x , y)

# Zad.11
# a = input()
# b = input()
# c = input()
# if a > b and a>c:
#     print("A jest najwieksze")
# elif b > a and b>c:
#     print("b jest najwieksze")
# else :
#     print("C jest najwieksze")

#Zad.12

# a = [2, 2.5, 3, 3.5, 5, 6.2]
# for i in range(len(a)):
#     a[i] = a[i] ** 2
# print(a)

# Zad.13
# b = []
# i = 0
# while i < 10:
#     a = int(input())
#     if a % 2 == 0:
#         b.append(a)
#     i += 1
#
# print("Parzyste liczby: ", b)
# Zad.15
# a = {1-x for x in range(1,11)}
# b = {i**2 for i in range(1, 7)}
# c = {x for x in b if x % 2 == 0}
# print("A: ", a)
# print("B:", b)
# print("C:", c)
# Zad.16
# import random
# l1 = [random.randint(1, 100) for i in range(10)]
# print("Pierwsza: ", l1)
# Zad.17
#
#                                 LAB4
#Zad.1
# plik=open("zad.1.txt","a")
#
# lista=[]
#
# for i in range (0,31):
#     lista+=[i]
#
# for i in lista:
#     lista[i]*=2
# print(lista)
# plik.writelines(str(lista))
#
# plik.close()
#Zad.2
# plik=open("Zad.1.txt","r")
#
# linia=plik.readlines()
# print(linia)
# plik.close()
# Zad.3
# with open("Zad.3.txt","w+") as plik:
#     for i in range(4):
#         plik.write("Mamy w sobie moc,\n")
#
#
# zad3=open("Zad.3.txt","r")
# linia=zad3.readlines()
# print(linia)
# zad3.close()
#Zad.4
class NaZakupy:
    nazwaproduktu=''
    ilosc=''
    jednostkamiary=''
    cenajed='zl'
    def __init__(self,nazwaproduktu,ilosc,jednostkamiary,cenajed):
        self.nazwa = nazwaproduktu
        self.ilosc = ilosc
        self.jednostka = jednostkamiary
        self.cena = cenajed

    def wyswietlprodukt(self):
        return nazwa+' '+ilosc+' '+jednostka+' '+cena+' zl'

    def ileproduktow(self):
        return ilosc+' '+jednostka
    def ilekosztuje(self):
        wynik=int(ilosc) * int(cena)
        return str(wynik)


nazwa=input("Nazwa: ")
ilosc=input("Ilosc: ")
jednostka=input("Jednostka miary: ")
cena=input("Cena: ")

nowy=NaZakupy(nazwaproduktu=str(nazwa),
              ilosc=int(ilosc),jednostkamiary=str(jednostka),
              cenajed=int(cena))

print(nowy.wyswietlprodukt())

print("Ilosc : "+nowy.ileproduktow())

print("Koszt: "+nowy.ilekosztuje()+" zl")

