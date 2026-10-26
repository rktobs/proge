
from datetime import date
from calendar import monthrange
from math import pi

# Ülesanne 1
tana = date.today()
print("Tere! Täna on", tana)
print(tana.strftime("%d/%m/%Y"))
print(tana.strftime("%B %d, %Y"))
print(tana.strftime("%m/%d/%y"))
print(tana.strftime("%b-%d-%Y"))

kuu_paevi = monthrange(tana.year, tana.month)[1]
print("Kuu lõpuni:", kuu_paevi - tana.day, "päeva")
print("Aasta lõpuni:", (date(tana.year, 12, 31) - tana).days, "päeva")

synnipaev = date(2008, 5, 17)  # pane oma kuupäev
paevi = (tana - synnipaev).days
print("Vanus:", paevi // 365, "aastat,", paevi % 365 // 30, "kuud,", paevi % 365 % 30, "päeva")

# Ülesanne 2
print("3 + 8 / (4 - 2) * 4 =", 3 + 8 / (4 - 2) * 4)
print("3 + 8 / 4 - 2 * 4 =", 3 + 8 / 4 - 2 * 4)
print("(3 + 8) / (4 - 2) * 4 =", (3 + 8) / (4 - 2) * 4)
print("3 + 8 / ((4 - 2) * 4) =", 3 + 8 / ((4 - 2) * 4))

# Ülesanne 3
R = float(input("Ringi raadius: "))
print("Ruudu pindala:", (2 * R) ** 2)
print("Ruudu ümbermõõt:", 4 * 2 * R)
print("Ringi pindala:", pi * R ** 2)
print("Ringi ümbermõõt:", 2 * pi * R)

# Ülesanne 4
raadius_mm = 6378 * 1000000
mündi_labimoot_mm = 25.75
print("Münte on vaja:", 2 * pi * raadius_mm / mündi_labimoot_mm)

# Ülesanne 5
a = "kill-koll"
b = "killadi-koll"
print(f"{a} {a} {b} {a} {a} {b} {a} {a} {a}".title())
print(a.title())

# Ülesanne 6
print("""Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.""".upper())

# Ülesanne 7
a = float(input("Külg a: "))
b = float(input("Külg b: "))
print("Ümbermõõt:", 2 * (a + b))
print("Pindala:", a * b)

# Ülesanne 8
try:
    liitrid = float(input("Liitrid: "))
    km = float(input("Kilomeetrid: "))
    print("Kütusekulu:", liitrid / km * 100, "l/100km")
except:
    print("Midagi läks valesti")

# Ülesanne 9
M = float(input("Minutid: "))
print("Jõuab", 29.9 * M / 60, "km")

# Ülesanne 10
min = int(input("Minutid: "))
print(f"{min // 60}:{min % 60:02d}")