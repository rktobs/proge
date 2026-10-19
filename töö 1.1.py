print("Tere, maailm!")
nimi = input ("Mis on sinu nimi? ")
print("Tere, maailm! Tervitan sind. "  ,nimi)
vanus = input ("Kui vana sa oled?")
print("Tere, maailm! Tervitan sind.",nimi, "Ma olen", vanus, "aastane,")

vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True

print(type(vanus))
print(type(eesnimi))
print(type(pikkus))
print(type(kas_käib_koolis))

import random

kommid = random.randint(5, 50)
print("Laual on komme:", kommid)
votta = int(input("Mitu kommi soovid võtta? "))
kommid = kommid - votta
print("Laual on nüüd komme:", kommid)

import math

ümbermoot = float(input("Sisesta puu ümbermõõt => "))
läbimõõt = ümbermoot/3.14
print("Puu läbimõõt on",läbimõõt)

from math import sqrt
N=float(input("Sisesta ristküliku esimene külg(N) => "))
M=float(input("Sisesta ristküliku teine külg(M) => "))

diagonaal=sqrt(N**2+M**2)
print("Ristküliku diagonaal on", diagonaal)

aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = round(teepikkus / aeg, 2)

print("Sinu kiirus oli " + str(kiirus) + " km/h")

arvud = []
for i in range(5):
    arvud.append(int(input("Sisesta täisarv: ")))

summa = sum(arvud)
print("Aritmeetiline keskmine:", summa / 5)

jagaja = int(input("Sisesta arv, millega summat jagada: "))
print("Täisarvuline osa:", summa // jagaja)
print("Jääk:", summa % jagaja)

print("   @..@")
print("  (----)")
print(" ( \\__/ )")
print('^^ "" ^^')

a = 3
b = 4
c = 5
P = a + b + c
print("Kolmnurga ümbermõõt on", P)

p = int(input("Mitu inimest? "))
hind = 12.90
kokku = hind * 1.10
print("Igaüks maksab", round(kokku / p, 2), "€")

vanus = 17
print("Järgmisel aastal oled " + str(vanus + 1) + " aastat vana")
try:
    vanus = int(input("Sisesta vanus: "))
    print("Järgmisel aastal oled", vanus + 1)
except ValueError:
    print("See ei olnud täisarv!")

     