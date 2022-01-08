print("-----Problema 1-----")

m = "Maximul dintre doua numere"
print(m.upper())
a = int(input("Dati-l pe a: "))
b = int(input("Dati-l pe b: "))

def maxim(a,b):
    if a < b :
        max = b
        print("a < b max = ", max)
    elif a > b:
        max = a
        c = format(max)
        print(f'a > b max = {c}')
    else:
        print("numerele sunt egale")
maxim(a,b)

print("\n-----Problema 2-----")

m = "   Grading system"
print(m.upper())
mark = int(input("Enter mark: "))
if 0 < mark < 25:
    print("Grade is F")
elif 25 <= mark < 45:
    print("Grade is E")
elif 45 <= mark < 50:
    print("Grade is D")
elif 50 <= mark < 60:
    print("Grade is C")
elif 60 <= mark < 80:
    print("Grade is B")
elif 80 <= mark <= 100:
    print("Grade is A")
else:
    print("Mark does not exist!")

print("\n-----Problema 3-----")

m = "Discount application for "
print(m.upper() + "50+ kg")
quantity = float(input("* Introdu cantitate: "))
cost = quantity * 20.3
discount = 0.1 * cost
cost_final = cost - discount
pret = "{:.3f}".format(cost)
if cost > 1000:
    print(f'** La un pret de 20.3 lei/kg si \n** un discount de 10% din {pret} avem:')
    print(f'*** Pret final: {"{:.2f}".format(cost_final)} lei')
else:
    print(f'** La un pret de 20.3 lei/kg fara discount de 10% din {pret} avem:')
    print("*** Pret final fara discount: ", pret)

print("\n-----Problema 4-----")

m = "Welcome "
print(m.upper() + "Bond! JAMES Bond")
i = str(input("Numele agentului: "))
if i == "Bond":
    print(" * Welcome on board 007")
else:
    print(f' * Good morning {i}')
    l = "-- Hello {}!"
    print(l.format(i))
    print(" * Hello {}".format(i))

print("\n-----Problema 5-----")

m = "  password validity"
print(m.upper())
print("$#@")
c = input("Introduceti parola: ")
car = 0
spec = 0
if 6 <= len(c) and len(c) <=16:
    for i in c:
        if (i.islower() or i.isupper() or i.isdigit()):
            car += 1
        if (i == '$') or (i == '#') or (i == '@'):
            spec += 1
if (car > 1 and spec >= 1 and car + spec == len(c)):
    print("Parola valida")
else:
    print("Parola invalida")

print("\n-----Problema 6-----")

m = "       5 or 6"
print(m.upper())
n = int(input("Introduceti un numar: "))
l = str(n)
def numar():
    if n == 5 :
        print("Numarul introdus este {} nu {}".format(n, n + 1))
    elif n == 6 :
        print("Numarul introdus este {} nu {}".format(n, n - 1))
    elif (n != 5 or n != 6):
            print("Numarul introdus este diferit de 5 sau 6 !")
    else:
        if l == str(n):
            print("Ati introdus o litera!")
numar()

print("\n-----Problema 7-----")

m = "      sortare"
print(m.upper())
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

def sort(a,b,c):
    if a < b and b < c :
        print("Sortare: ", a,b,c)
    elif a > b and b < c and a > c:
        print("Sortare: ", b,c,a)
    elif a > b and b < c and a < c:
        print("Sortare: ", b,a,c)
    elif a < b and b > c and a < c:
        print("Sortare: ", a,c,b)
    elif a < b and b > c and a > c:
        print("Sortare: ", c,a,b)
    else:
        print("Sortare: ", c, b, a)
sort(a,b,c)

# print("\nMetoda a 2-a cu numere pana la 10 !!!")
# list = [input("a= "), input("b= "), input("c= ")]
# #list = ["5", "8" , "7"]
# print("Lista de numere este: ", list)
# list.sort()
# print("Lista 1 sortata este: ", list)
# sorted(list)
# print("Lista 2 sortata este: ", list)
# list.sort(reverse=True)
# print("Lista 3 reverse sortata este: ", list)
# sorted(list, reverse = True)
# print("Lista 4 reverse sortata este: ", list)
# sorted(list)
# print("Lista 5 sortata este: ", list)
# print("Lista 6 sortata este: ", sorted(list))


print("\n-----Problema 8-----")

m = "   Parrot trouble"
print(m.upper())
hour = int(input("Ore liniste: "))

if ((hour >= 0) and (hour <= 7)):
    print("Papagalul deranjeaza: ", bool(hour))
elif (hour >= 20) and (hour <= 23):
    print("Papagalul deranjeaza: ", bool(hour))
else:
    if hour in range(24):
        print("Nu deranjeaza!")
    else:
        print("Orele nu apartin intervalului dat!")

import datetime
now = datetime.datetime.now()
der = ""
def ora(now):
    print("An - {}, Luna - {}, Zi - {}, ___ Ora - {} ___ , Minut - {}, Secunda - {} ".format(now.year, now.month, now.day, now.hour, now.minute, now.second))
    if now.hour >= 0 and now.hour <= 7:
        return True
    elif (now.hour >= 20) and (now.hour <= 23):
        return True
    else:
        if now.hour in range(24):
            print("Nu deranjeaza!")
        else:
            print("Orele nu apartin intervalului dat!")
print("Papagalul deranjeaza: ",ora(now))

print("\n-----Problema 9-----")

m = "        not   "
print(m.upper())
sir = str(input("Dati sirul: "))
if sir[0:3] == "not":
    print("Sirul este: " + sir)
else:
    print("Noul sir este: " + "not" + " " + sir)

print("\n-----Problema 10-----")

m = "        Hi    "
print(m.upper())
strg = str(input("Dati sirul: "))
def fct():
    if strg[0:2] == "hi":
        return True
    else:
        return False

print(" ", fct())

print("\n-----Problema 11-----")

m = " Forbidden sum returns '20'  "
print(m.upper())
print("Forbidden sum { 10 and 19 }")
a, b = int(input("a= ")), int(input("b= "))
c = a + b
if c >= 10 and c <= 19:
    print("20")
else:
    print("Suma: ", c)

print("\n-----Problema 12-----")

m = " *11/*11 + 1 == special  "
print(m.upper())
print("Obtine un multiplu de 11")
mul = int(input("Dati un numar: "))
multiplu = 11 * mul
print(multiplu)

no = int(input("Introduceti un numar "))
if no == multiplu or no == multiplu + 1:
    print("Special  ---   ", bool(no))
else:
    print("Special  ---   ", bool(0))

n = int(input("numarul este: "))
if n % 11 == 0 or (n-1) % 11 == 0:   #  sau if n%11 == 0 or n%11 == 1:
    print("este numar special")
else:
    print("nu este numar special")

    