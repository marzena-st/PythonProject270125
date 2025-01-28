# kolekcje - przecowują wiele elementów

# lista - przechowuje dowolną ilość danych, rónego typu na raz
# zachowuje kolejność przy dodawaniu danych

# pusta lista
lista = []
print(lista)
print(type(lista))

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))

# append() - dodawanie elementów do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Bogdan")
lista.append("Anna")
lista.append("Maciek")

print(lista)
# lista ma indeksy

print(len(lista))
print(lista[0])

# print(lista[10]) # błąd index poza zakresem

print(lista[-3])

# wyświetlanie fragmentu listy (slicowanie)
print(lista[0:3])  # czyli pierwsze 3 elementy, bo oznaczy jakby nawias otwarty z prawej
print(lista[:3])
print(lista[2:])  # włącznie 2345
print(lista[2:5])  # 234

print(lista[2:16])  # 2345
print(lista[:])
print(lista[2:2])  # pusta lista
print(lista[10:27])

print(lista[-2:0])  # pusta lista [4:0]
print(lista[0:-2])

lista_15 = list(range(15))  # zakres od 0-14
print(lista_15)
print(lista_15[0:15:2])  # start, stop, krok

print(list(range(0, 15, 2)))
print(lista[::2])

print(lista[::-1])  # odwrócona lista

# nadpisanie elementu w liscie na wskazanym indeksie
# zmiana na oryginalnej liście
lista[3] = "Asia"
print(lista)

# dopisanie elementu do listy we wskazanym miejscu
# insert
lista.insert(1, "Krzysztof")
print(lista)

lista.insert(15, "Mateusz")
print(lista)

# sprawdzenie indeksu dla wskazanego elementu
print(lista.index("Asia"))
lista.append("Asia")
print(lista)
print(lista.index("Asia"))

# usunięcie elementu po indeksie, pierwszy napotkany
lista.remove("Asia")
print(lista)

# usunięcie elementu po indeksie
lista.pop(5)
print(lista.pop(5))
print(lista)
print(lista.pop())  # usunie ostatni element

a = 1
b = 3
a = b
print(f"{a=}, {b=}")
b = 9
print(f"{a=}, {b=}")

lista_2 = lista  # odpwoiednik a = b, kopia adresu listy, kopia referencji
lista_copy = lista.copy()
print(lista_2)
print(lista)

lista.clear()  # usunięcie wszystkich elementów z listy
print(lista_2)
print(lista)
print(id(lista_2))
print(id(lista))
print(id(lista_copy))

liczby = [54, 999, 34, 22, 12.34, 567]
print(liczby)
print(type(liczby))
liczby.sort()
print(liczby)

liczby = [54, 999, 34, 22, 12.34, 567, "A"]
print(liczby)
print(type(liczby))


print(lista_copy)
lista_copy.sort()
print(lista_copy)

lista_copy.sort(reverse=True)
print(lista_copy)

liczby[3] = 666
print(liczby[0:3])
print(liczby[-2])
print(liczby)

# rozpakowanie sekwencji
tekst = 'Pyth on.'
lista1 = list(tekst)
print(lista1)

lista2 = [tekst]
print(lista2)

krotka = tuple()
print(type(krotka))
print(krotka)
