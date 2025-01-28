import sys

print()  # wypisz/wydrukuj
# Process finished with exit code 0 - program zakończył działanie bez błędu

# ctrl d - powielanie linijek
print("Nazywam się Marzena")
print("Nazywam się Marzena")
print("Nazywam się Marzena")

# mozna stosować cudzysłowy ", ' ale jednolicie na początku i końcu
print('Nazywam się Marzena')

# Process finished with exit code 1 - zakończone błędem
# interpretowany wykoinuje się od góry do dołu
# bład zatrzymuje działanie programu

# ctrl / - automatyczne komentowanie
print("Nazywam się 'Marzena'") # mozna łączyć, ale musi się zgadzac liczba cudzysłowów

# type() - sprawdzenie typu danych
print(type("Marzena")) # <class 'str'>, string, dane typu tekstowego

print("39"+"39") # 3939, konkatenacja - łączenie tekstów


print(39+39) # 78 operacja na liczbach
print(type(39)) # <class 'int'>, integer -liczba całkowita
print(sys.int_info) # zadania systemowe; zakres liczb int
# sys.int_info(bits_per_digit=30,
#               sizeof_digit=4,
#               default_max_str_digits=4300, maksymalna liczba cyfr 4300 znaków
#               str_digits_check_threshold=640)

# operacja niedozwolona, nie zamienia typów na inne w trakcie wykonywania operacji
# silne typowanie
# print("39"+39) # Type Error: can only concatenate str (not "int") to str

# musimy jawnie wskazać odpwoiednie typy
print(int("39")) # rzutownie, zamiana na liczbę int
print(int("39")+39)
# print(int("A")) # ValueError: invalid literal for int() with base 10: 'A'

print("39"+ str(39)) # 3939, str( rzutowanie, zamiana na str

# print(5*"4") # 44444

# 168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168
print(168* 50) #8400
print(int(168)*int(50))

# zmienna - pudełko na dane, przechowuje jeden element
# snake_case - z małej litery, drugi wyraz po podkreslniku _
# nazwa zmienej powinna sugerować co przechowuje

# typowanie dynamiczne
# typ zmiennej jest określany na podstawie jakie dane zwiera
# w kadej chwili, mozemy do zmiennej wrzucić dowolną inną wartość innego typu
# zmieni się typ zmiennej

liczba = 39
print(liczba) # nazwa zmiennej bez cudzysłowia
print(type(liczba)) # <class 'int'>

name = "Radek"
print(name+"Kowalski") # RadekKowalski
name = 90
# print(name+"Kowalski") # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# podpowiedź dla programisty i pycharma
name: str = "Radek"
print(name)
name = 90
print(name) # 90

age = 56
print(age)
print(type(age)) # 56 <class 'int'>
