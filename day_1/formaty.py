user = "Tomek" # str
wiek = 39 # int
wersja=3.90001 #
print(type(wersja)) # <class 'float'> - liczby zmiennoprzecinkowe
liczba=456789 # int

print("Witaj %s, masz teraz %d lat." %(user,wiek))
# sprawdza typy
# print("Witaj %d, masz teraz %s lat." %(user,wiek))

print("Witaj %(user)s, jesteś %(user)s" %{"user": user})
print("Witaj %(user)a, jesteś %(user)a" %{"user": user}) # a powoduje ze tekst jest w apostrofach Witaj 'Tomek', jesteś 'Tomek'

print(f"Witaj {user}, masz teraz {wiek} lat.")

print("Uzywamy wersji pythona %i" % 3)
print("Uzywamy wersji pythona %f" % 3) # zera się pojawią
print("Uzywamy wersji pythona %.0f" % 3.9) # lub %.f
x = 3.8796
print(x)
print("%.2f" %x)

y = round(x)
print(y)

z=round(x,2)
print(z)

print(f"Uzywamy wersji pythona {wersja}") # Uzywamy wersji pythona 3.90001
print(f"Uzywamy wersji pythona {wersja: .2f}")

print(f"{user: <10}") # formatuje kolumne to długości 10 (wyrównanie do lewej)
print(f"{user: >20}") # wyrównanie do prawej
print(f"{user: ^20}") # wyśrodkowanie

print(liczba)
print(f"nasz duza liczba {liczba: _}".replace("_", "."))

liczba = 15_000_000_000_000
print(liczba)
print(type(liczba)) # int
