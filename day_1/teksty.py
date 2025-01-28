tekst = ("Witaj Świecie")
print(tekst)
print(type(tekst)) # Witaj Swiecie <class 'str'>


tekst.upper()
print(tekst)

tekst_upper=(tekst.upper())
print(tekst_upper)

# małe litery, capitalize
print(tekst.lower()) # witaj swiecie
print(tekst.capitalize()) #Witaj swiecie
print(tekst.swapcase()) # wITAJ sWIECIE

# Witaj Świecie
# 01234567890... - indeksy numerowane od 0

print(tekst[6]) # "S" liczy ze spacjami, ale od 0

print(tekst.index("Ś")) # 6
print(tekst.index("i")) # 1
print(tekst.count("i")) # i wystpępuje 3 razy
print(tekst.count("j",0,4)) # j wystepuje 0 razy, bo z prawej storny zbiór otwarty
print(tekst[4]) # j

print(tekst.removeprefix("Witaj")) # Swiecie
print(tekst.removesuffix("Swiecie")) # Witaj

# usunięcie białych znaków, spacji..-> strip()
print(tekst.removesuffix("Swiecie").strip())

tekst_zamiana = "Witaj Dobry Świecie"
print(tekst_zamiana.replace("Dobry", ""))

# kodowanie znaków

encode_s = tekst.encode('utf-8')
print(encode_s) # b'Witaj Swiecie \xc5\x9awiecie''
print(type(encode_s)) # <class 'bytes'> dane bajtowe
# \xc5\x9awiecie' zapis szesnastkowy dla literki Ś
print(encode_s.decode('utf-8')) # Witaj Świecie

# f string, tekst sformatowany
imie = "Radek"
# tekst_format = f"Mam na imię {imie} i lubię pythona"
# print(tekst_format)

tekst_format = f"\tMam na imię {imie}\n i lubię pythona.\b"
print(tekst_format)
# Mam na imię Radek
# i lubię pythona
# \t - tabulator
# \n nowa linia
# \b - backspace

starszy="Witaj %s!" # %s w to miejsce podstawi string (starszy sposób)
print(starszy % imie) # Witaj Radek!

print("Witaj {}!".format(imie)) # format zapomniany

print("Witaj", imie)

print("""Teskt 
    wielolinijkowy""")

# traktowany jako dokumentacja
"""Komentarz
    wielolinijkowy"""
