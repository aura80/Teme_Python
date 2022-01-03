print("-----Problema 1 varianta 1-----")
#Write a Python program to find the number of days in a month.
def months():
    m = int(input("Luna in cifre: "))
    an = int(input("An: "))
    l = [1,3,5,7,8,10,12]
    ll = ["January","March","May","July","August","October","December"]
    p = [4,6,9,11]
    pp = ["April","June","September","November"]
    if m == 2:
        if (an >= 0 and an % 4 == 0 and an % 100 != 0) or (an >= 0 and an % 4 == 0 and an % 400 == 0):
            print("February {} has 29 days".format(an))
        # elif an % 400 == 0:
        #     print("February {} has 29 days".format(an))
        else:
            print("February {} has 28 days".format(an))
    elif m!=2 and m in l and an >= 0:
        if m == l[0]:
            print("{} {} has 31 days".format(ll[0], an))
        if m == l[1]:
            print("{} {} has 31 days".format(ll[1], an))
        if m == l[2]:
            print("{} {} has 31 days".format(ll[2], an))
        if m == l[3]:
            print("{} {} has 31 days".format(ll[3], an))
        if m == l[4]:
            print("{} {} has 31 days".format(ll[4], an))
        if m == l[5]:
            print("{} {} has 31 days".format(ll[5], an))
        if m == l[6]:
            print("{} {} has 31 days".format(ll[6], an))
    elif m in p and an >= 0:
        if m == p[0]:
            print("{} {} has 30 days".format(pp[0], an))
        if m == p[1]:
            print("{} {} has 30 days".format(pp[1], an))
        if m == p[2]:
            print("{} {} has 30 days".format(pp[2], an))
        if m == p[3]:
            print("{} {} has 30 days".format(pp[3], an))
    else:
        if an < 0:
            print("An invalid")
        if m <= 0:
            print("Luna invalida")
months()

print("\n-----Problema 1 varianta 2-----")
m = int(input("Input a month using numbers: "))
y = input('Input a year: ')

if m == 1:
    print("January {} has 31 days".format(y))
elif m == 2:
    print("February {} has 28 days".format(y))
elif m == 3:
    print("March {} has 31 days".format(y))
elif m == 4:
    print("April {} has 30 days".format(y))
elif m == 5:
    print("May {} has 31 days".format(y))
elif m == 6:
    print("June {} has 30 days".format(y))
elif m == 7:
    print("July {} has 31 days".format(y))
elif m == 8:
    print("August {} has 31 days".format(y))
elif m == 9:
    print("September {} has 30 days".format(y))
elif m == 10:
    print("October {} has 31 days".format(y))
elif m == 11:
    print("November {} has 30 days".format(y))
elif m == 12:
    print("December {} has 31 days".format(y))
else:
    print("Luna invalida")

print("\n-----Problema 2-----")
#   Write a Python program to find the zodiacal sign when you have the day and  the month of birth
def zodiacal():
    m = input("Input a month in letters: ")
    d = int(input("Input a day: "))
    l = ("January","February","March","April","May","June","July","August","September","October","November","December")
    z = ["Berbec","Taur","Gemeni","Rac","Leu","Fecioara","Balanta","Scorpion","Sagetator","Capricorn","Varsator","Pesti"]
    m = m.capitalize()
    if m in l:
        if ((m == "March" and (d >= 21 and d <= 31)) or (m == "April" and (d >= 1 and d <= 20))):
            print("Your zodiac sign is: ",z[0])
        elif ((m == "April" and (d >= 21 and d <= 30)) or (m == "May" and (d >= 1 and d <= 20))):
            print("Your zodiac sign is: ",z[1])
        elif ((m == "May" and (d >= 21 and d <= 31)) or (m == "June" and (d >= 1 and d <= 21))):
            print("Your zodiac sign is: ",z[2])
        elif ((m == "June" and (d >= 22 and d <= 30)) or (m == "July" and (d >= 1 and d <= 22))):
            print("Your zodiac sign is: ",z[3])
        elif ((m == "July" and (d >= 23 and d <= 31)) or (m == "August" and (d >= 1 and d <= 22))):
            print("Your zodiac sign is: ",z[4])
        elif ((m == "August" and (d >= 23 and d <= 31)) or (m == "September" and (d >= 1 and d <= 22))):
            print("Your zodiac sign is: ",z[5])
        elif ((m == "September" and (d >= 23 and d <= 30)) or (m == "October" and (d >= 1 and d <= 22))):
            print("Your zodiac sign is: ",z[6])
        elif ((m == "October" and (d >= 23 and d <= 31)) or (m == "November" and (d >= 1 and d <= 21))):
            print("Your zodiac sign is: ",z[7])
        elif ((m == "November" and (d >= 22 and d <= 30)) or (m == "December" and (d >= 1 and d <= 20))):
            print("Your zodiac sign is: ",z[8])
        elif ((m == "December" and (d >= 21 and d <= 31)) or (m == "January" and (d >= 1 and d <= 19))):
            print("Your zodiac sign is: ",z[9])
        elif ((m == "January" and (d >= 20 and d <= 31)) or (m == "February" and (d >= 1 and d <= 18))):
            print("Your zodiac sign is: ",z[10])
        elif ((m == "February" and (d >= 19 and d <= 29)) or (m == "March" and (d >= 1 and d <= 20))):
            print("Your zodiac sign is: ",z[11])
zodiacal()

print("\n-----Problema 3-----")
#   Write a program in Python to display the first 10 natural numbers
def primele_numere():
    for i in range(1,11,1):
        print(i)
primele_numere()

print("-----Problema 3-----")
#   Write a program in Python to display the first the sum and the average of numbers from 200 to 450
def suma_medie():
    sum = 0
    for i in range(200,451,1):
        sum = sum + i
        average = sum / len(range(200,451,1))
    print("Suma = ", sum)
    print("Average = ", average)
suma_medie()

