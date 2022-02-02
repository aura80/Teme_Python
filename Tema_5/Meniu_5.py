import sys

def numarare():
    l = list(input("Dati lista (9 de mai multe ori): ").split())
    print(l)
    s = 0
    for i in l:
        if i == '9':
            s += 1
    print(f'Cifra --  9  -- se regaseste de --  {s}  -- ori in lista {l}\n')

#numarare()

def a():
    for i in range(0,7):
        if i != 3 and i != 6:
            print(i)
#a()

def multi():
    m = int(input("Input a number: "))
    p = 1
    for i in range(1,11):
        p = m * i
        print(f' {m} X {i} = {p}')
#multi()

# def menu3():
#     #print("************MAIN MENU**************")
#     n = int(input("""************MAIN MENU**************
#         1: numarare()
#         2: a()
#         3: multi()
#         10: exit
# Please enter your choice: """))
#
#     if n == 1 :
#         numarare()
#         menu3()
#     elif n == 2 :
#         a()
#         menu3()
#     elif n == 3 :
#         multi()
#         menu3()
#     elif n == 10 :
#         sys.exit()
#
#     else:
#         print("You must only select either 1,2, or 3.")
#         print("Please try again")
#         menu3()
#
#menu3()

def menu():

    print("---------MENU---------")
    key = int(input("Dati nr: "))

    if key == 1:
        numarare()
    elif key == 2:
        a()
    elif key == 3:
        multi()
    elif key == 4:
        exit()

menu()


