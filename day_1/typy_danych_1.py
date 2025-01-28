import sys

wiek = 47  # int
rok = 2025  # int
temp = 36.6  # float

print(wiek + rok)  # 2072
print(wiek - rok)  # -1978
print(wiek * rok)  # 95175
print(wiek / rok)  # 0.023209876543209877

print(rok // wiek)  # część całkowita z dzielenia
print(rok % wiek)  # reszta z dzielenia
print(5 % 2)  # r1

print(wiek ** rok)  # potęga

# len() sprawdzenie długości
print(len(str(wiek ** rok)))  # 3386 znaków

print(54 - 5 * 43 + 4 / 2 + 4 / 2)
print(54 - 5 * 43 + (4 / 2 + 4) / 2)

# liczby float
# ma błąd zaokrąglenia
print(0.2 + 0.7)  # 0.8999999999999999

# decimal - pozwala ominąć błąd zaokrąglenia
print(sys.float_info)

print(f"Sprawdzenie zmiennej {temp} {wiek}")

# typ logiczny
# prawda fałsz
# True False
# 1 True, 0 False
czy_znasz_pythona = True  # <class 'bool'>, boolean, logiczny
print(czy_znasz_pythona)  # True
print(type(czy_znasz_pythona))

print(int(czy_znasz_pythona))
print(int(False))

print(bool(1))  # bool() - rzutowanie na typ boolean, True
print(bool(0))
# wszystko co nie 0 jest True
print(bool(100))  # True
print(bool(-100))  # True

print(bool("Radek"))

print(bool(""))  # False
print(bool(0.01))
print(bool("0"))

print(bool(None))  # False, odpowiednik null, nic, stan nieokreślony


# and - i
print(True and True)
print(True and False)

# or - lub
print(True or True)
print(True or False)
print(False or False)

# NOT - negacja
print(not True)
print(not False)

a = 8
b = 6

print(f"Porównanie {a} > {b} = {a > b}")
print(f"Porównanie {a} < {b} = {a < b}")

print(f"Porównanie {a >= b = }")


