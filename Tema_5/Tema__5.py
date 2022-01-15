import array
print("-------Problema 1-------")
# ****** return the number of 9's in a list
# [1, 2, 9] → 1
# [1, 9, 9 ]→ 2
# [1, 9, 9, 3, 9] → 3

def numarare():
    l = list(input("Dati lista (9 de mai multe ori): ").split())
    print(l)
    s = 0
    for i in l:
        if i == '9':
            s += 1
    print(f'Cifra --  9  -- se regaseste de --  {s}  -- ori in lista {l}\n')

numarare()

def numarare(li):
    # li = list()
    s = 0
    for i in li:
        if i == 9:
            s += 1
    print(f'" 9 " de -- {s} -- ori in lista {li}')
numarare([1, 2, 9])
numarare([1, 9, 9])
numarare([1, 9, 9, 3, 9])

print("\n-------Problema 2-------")
#****** Write a Python program that prints all the numbers from 0 to 6 except 3 and 6
def a():
    for i in range(0,7):
        if i != 3 and i != 6:
            print(i)
print("Varianta 1 ")
a()

def b():
    l = [0,1,2,3,4,5,6]
    for i in l:
        if i != 3 and i != 6:
            print(i)
print("Varianta 2 ")
b()

def c(lista):
    l = []
    for i in lista:
        if i != 3 and i != 6:
            l.append(i)
    print(l)
print("Varianta 3 ")
c([0,1,2,3,4,5,6])

def d():
    l = []
    lista = input("\nDati orice numere (mai multe, 3 6 inclusiv), preferabil intre 0 si 6: ").split()
    for i in lista:
        if (i == '0' or i == '1' or i == '2' or i == '4' or i == '5') and (i != '3' and i != '6'):
            l.append(i)
        else:
            print(f'Numarul {i} este invalid!')
    print("Lista este:     ", l)
d()

print("\n-------Problema 3-------")
#****** Print sum of the numbers between 20 and 100
s = 0
for i in range(20,101):
    s += i
print("Suma numerelor de la 20 la 100: ", s)

print("\n-------Problema 4-------")
#****** Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
l = []
for i in range(1,51):
    if i % 3 == 0:
        if i % 5 == 0:
            #print("FizzBuzz")
            l.append("FizzBuzz")
        else:
            #print("Fizz")
            l.append("Fizz")
    elif i % 5 == 0:
            #print("Buzz")
            l.append("Buzz")
    else:
        #print(i)
        l.append(i)
print(l)

print("-------Problema 5-------")
#******Write a Python program to create the multiplication table (from 1 to 10) of a number.
def multi():
    m = int(input("Input a number: "))
    p = 1
    for i in range(1,11):
        p = m * i
        print(f' {m} X {i} = {p}')
multi()

def multiplu():
    m = int(input("Input a number: "))
    l = [1,2,3,4,5,6,7,8,9,10]
    p = 1
    for i in l:
        p = m * i
        print(f' {m} X {i} = {p}')
multiplu()

print("-------Problema 6-------")
#****** Write a Python program to construct the following pattern
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999
#
# print("---Varianta 0 obtin altceva ")
# l = []
# p = 1
# for i in range(1,10):
#     for j in range(1,10):
#         if i <= j:
#             z = i * p
#     l.append(z)
#     print("*",l)

# print("---Varianta 0 obtin altceva ")
# l = []
# sample_array = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
# for i in range(1,10):
#     l.append(sample_array[i-1])
#     print(l)

# print("---Varianta 0 obtin altceva ")
# l = []
# p = 1
# for i in range(1,10):
#     for j in range(1,10):
#         if i <= j:
#             z = i * p
#         elif i > j:
#             z = i
#     l.append(z)
#     z += 1
#     print("*", l)
#
# print("---Varianta 0 obtin altceva ")
# A = [1,2,3,4,5,6,7,8,9]
# print(A[0])
# print(A[1],A[1])
# print(A[2],A[2],A[2])
# print(A[3],A[3],A[3],A[3])
# print(A[4],A[4],A[4],A[4],A[4])
# print(A[5],A[5],A[5],A[5],A[5],A[5])
# print(A[6],A[6],A[6],A[6],A[6],A[6],A[6])
# print(A[7],A[7],A[7],A[7],A[7],A[7],A[7],A[7])
# print(A[8],A[8],A[8],A[8],A[8],A[8],A[8],A[8],A[8])

print("---Varianta 2 ")

sample_array = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

for i in sample_array:
    for j in sample_array:
        if sample_array[i-1] >= sample_array[j-1]:
            print(" ",end = f'{i}')
    p = i * '-'
    print(" -",p)

print("---Varianta 3 ")

n=10
for i in range(1,n):
    for j in range(i):
        print (end = f'{i}')
    print('')

print("\n-------Problema 7-------")
# ******Write a program to print n natural number in descending order
# *****print max and minim from the list
# lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
print("---Varianta 1 ")
lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
maxim = max(lst)
print("Maximul din lista este: ", maxim)
minim = min(lst)
print("Minimul din lista este: ", minim)

print("---Varianta 2 ")
def max_min(lst):
    maxim = lst[0]
    minim = lst[0]
    for i in lst:
        if i >= maxim:
            maxim = i
        elif i <= minim:
            minim = i
    print("Maxim este: ", maxim)
    print("Minim este: ", minim)

max_min([55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6])

print("\n-------Problema 8-------")
# *****count how many times 6 occur in the list.
# lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
print("---Varianta 1 ")
lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
s = lst.count(6)
print(f' * 6 * se regaseste de -- {s} -- ori in lst =', lst)

print("---Varianta 2 ")
def sase(lsst):
    nr = int(input(f'Dati un numar din lista {lsst} : '))
    s = 0
    for i in lsst:
        if nr == i:
            s += 1
    print(f'Numarul - {nr} - apare de -- {s} -- ori in lista -- {lsst}')
sase([55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6])
sase([2,3,8,2,9,5,4,7,3,9,2,1,8,8,9,9,7,7,7,5])

print("\n-------Problema 9-------")
# *****Using .remove() method, clear the last element of the list.
print("---Varianta 1   - remove last element")
lista=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6, 7]

def ultim_0():
    lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
    print("Lista initiala:", lst)
    lst.reverse()
    lst.remove(lst[0])
    lst.reverse()
    print("Cu remove():   ", lst)
ultim_0()

print("\n---Varianta 2   - remove last element")
def ultim(lista):
    ultim = lista[-1]
    for i in lista:
        if i == ultim:
            if lista.index(i) == lista.index(ultim):
                lista.remove(ultim)
            else:
                lista
    print(lista)

print(f'Lista este: \n{[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6, 7]}')
print(f'Ramane: ')
ultim([55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6, 7])
print(f'\nLista este: \n{[55, 6, 777, 54, 22222, 76, 101, 1, 22222, 2, 22222]}')
print(f'Ramane: ')
ultim([55, 6, 777, 54, 22222, 76, 101, 1, 22222, 2, 22222])

print("\n---Varianta 3 ")
def fructe(x):
    l = ["mere", "pere", "kiwi", "mango", "portocale", "caise"]
    print(l)
    l.remove(x)
    print(l)
    print(f'Removed:  ---  "{x}"')
fructe("caise")
fructe("pere")

print("\n-------Problema 10-------")
# # *****Concatenate two lists in the following order
# # list1 = ["Hello ", "take "]
# # list2 = ["Dear", "Sir"]

print("---Varianta 0 ")

def conc2():
    list1 = ["Hello ", "take "]
    list2 = ["Dear", "Sir"]
    l = []
    for i in list1:
        for j in list2:
            l.append(i + j)
    print("Lista:      ", l)

    res = [x + y for x in list1 for y in list2]
    print("Pe scurt:   ", res)
conc2()

print("---Varianta 1 ")
l = []
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
l = list1 + list2
print("Concatenare simpla: ",l)
#print(str(list1) + '\n' + str(list2))

print("---Varianta 2 ")

res = [i + j for i, j in zip(list1, list2)]
print("The concatenated lists: ", res)

print("---Varianta 3 ")

lista_goala = []
for (i,j) in zip(list1, list2):
    lista_goala.append(i + j)
print("Lista concatenata:      ", lista_goala)


print("\n-------Problema 11-------")
# *****add the sub-list: ["socks", "tshirt", "pajamas"] to the end of the gift_list
#  gift_list=['socks', '4K drone', 'wine', 'jam']

def adaugare1():
    gift_list=['socks', '4K drone', 'wine', 'jam']
    l = ["socks", "tshirt", "pajamas"]
    gift_list.extend(l)
    print(gift_list)
adaugare1()

def adaugare2():
    gift_list=['socks', '4K drone', 'wine', 'jam']
    l = ["socks", "tshirt", "pajamas"]
    gift_list.append(l)
    print(gift_list)
adaugare2()

def adaugare3():
    gift_list=['socks', '4K drone', 'wine', 'jam']
    l = ["socks", "tshirt", "pajamas"]
    gift_list += l
    print(gift_list)
adaugare3()

def adaugare4():
    gift_list=['socks', '4K drone', 'wine', 'jam']
    gift_list += ["socks", "tshirt", "pajamas"]
    print(gift_list)
adaugare4()

def adaugare5():
    gift_list=['socks', '4K drone', 'wine', 'jam']
    gift_list[:] =gift_list + ["socks", "tshirt", "pajamas"]
    print(gift_list)
    print(gift_list[:])
adaugare5()

def adaugare6():
    gift_list=['socks', '4K drone', 'wine', 'jam']
    l = ["socks", "tshirt", "pajamas"]
    gift_list.insert(4, l)
    print(gift_list)
adaugare6()

def adaugare7():
    gift_list=['socks', '4K drone', 'wine', 'jam']
    gift_list.insert(4, "socks")
    gift_list.insert(5, "tshirt")
    gift_list.insert(6, "pajamas")
    print(gift_list)
adaugare7()


def adaugare8():
    gift_list=['socks', '4K drone', 'wine', 'jam']
    for i in gift_list:
        if i != 4 and i > 'w':
            gift_list += ["socks", "tshirt", "pajamas"]
    print(gift_list)
adaugare8()

# def diferenta_liste():
#     list1 = [10, 15, 20, 25, 30, 35, 40]
#     list2 = [25, 40, 35]
#     list = list1 - list2
#     print(list)
# diferenta_liste()
#
# def diferenta_liste2(list1, list2):
#     list = list1 - list2
#     return list
#
# list1 = [10, 15, 20, 25, 30, 35, 40]
# list2 = [25, 40, 35]
# dif = diferenta_liste2(list1, list2)
# print(dif)

print("\n-------Problema 12-------")
# *****Given 2D array calculate the sum of diagonal elements.
# Ex: [[1,3,5],[1,4,6],[7,6,9]]
print("----Printare matrice 1:----")
A = [[1,3,5],[1,4,6],[7,6,9]]
print(A[0])
print(A[1])
print(A[2])

print("----Printare matrice 2:----")
for a in A:
    print(a)

print("----Suma diagonala 1:----")
s = A[0][0] + A[1][1] + A[2][2]
print(f'Suma elementelor de pe diagonala este: \n {A[0][0]} + {A[1][1]} + {A[2][2]} = {s}')

print("----Suma diagonala 2:----")
def matrice(A):
    #A = [[1,3,5],[1,4,6],[7,6,9]]
    sum = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end=" ")
        print("      ",A[i][i])
        sum += A[i][i]
    print(f'-------------- ')
    print(f'Suma este:  {sum}')

matrice([[1,3,5],[1,4,6],[7,6,9]])

print("---- numpy - Suma diagonala 3: ----")
import numpy as nmp
A = [[1,3,5],[1,4,6],[7,6,9]]

X = nmp.array(A)

a = X[0][0]
b = X[1][1]
c = X[2][2]

print("Suma lor este: ",a + b + c)

print("Linie 0: ", X[0])
print("Coloana 0: ", X[:,0])
print("Linie 1: ", X[1])
print("Coloana 1: ", X[:,1])
print("Linie 2: ", X[2])
print("Coloana 2: ", X[:,2])

print('\nElementele diagonalei sunt: ')
print(X[0][0],X[1][1],X[2][2])
print(X[0][0])
print(X[1][1])
print(X[2][2])


print("\n-------Problema 13-------")
# *****Add item 7000 after 6000 in the following Python List
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

def liste_imbricate1(lista3):
    for i in range(len(lista3)):
        if isinstance(lista3[i], list):
            for j in range(len(lista3[i])):
                if isinstance(lista3[i][j], list):
                        l3 = lista3[i][j]
                        # l4 = lista3[i][j]
                        # l5 = lista3[i][j]
                        l3.extend([7000])
                        # l4.append([7000])
                        # l5.append(7000)
                        #
                        # print("---", l3)
                        # print("---", l4)
                        # print("---", l5)
    print("***** ", lista3)

liste_imbricate1([10, 20, [300, 400, [5000, 6000], 500], 30, 40])

def liste_imbricate2():
    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    list1[2][2].append(7000)
    print("***** ", list1)

liste_imbricate2()

def liste_imbricate3():
    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    list2 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

    for i in list1:                     # i in toata lista
        if list1.index(i) == 2:         # index 2 in toata lista
            for j in list1[2:3]:        # j in lista 2 [300, 400, [5000, 6000], 500]
                    li = []
                    li = j[2:3]
                    # print("1 --- ", li)
                    li.append([7000])
                    j[2:3] =  li
                    # print("2 --- ", li)
                    # print("3 --- ", j)
                    list1[2:3] = j
                    # print("4 --- ", list1)
                    break
        else:
            pass
    print("***** ", list1)

    for i in list2:                     # i in toata lista [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
        if list2.index(i) == 2:         # index 2 in toata lista
            for j in list2[2:3]:        # j in lista 2 [300, 400, [5000, 6000], 500]
                        ki = []
                        j[2:3] = [5000, 6000, 7000]
                        list2[2:3] = j
    print("***** ", list2)

liste_imbricate3()

print("\n-------Problema 14-------")
# *****Given a Python list, find value 20 in the list, and if it is present, replace it with 200.
#  Only update the first occurrence of a value
#  list1 = [5, 10, 15, 20, 25, 50, 20]

def find_20():
    list1 = [5, 10, 15, 20, 25, 50, 20]
    print("///", list1)
    for i in list1:
        if i == 20 :
            j = list1.index(i)
            list1[j] = 200
            print("___", list1)
            break
find_20()

print("\n-------Problema 15-------")
# *****Remove empty strings from the list of strings
#  ["Mike", "", "Emma", "Kelly", "", "Brad"]

l = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print("   ", l)

def sterge_gol1():
    for i in l:
        if i == "":
            j = l.index(i)
            del l[j]
    print("   ", l)
sterge_gol1()

def sterge_gol2():
    ll = ["Mike", "", "Emma", "Kelly", "", "Brad"]
    for i in ll:
        if i == "":
            ll.remove("")
    print("   ", ll)
sterge_gol2()

def sterge_gol3(lll):
    for i in lll:
        if i == "":
            j = lll.index(i)
            lll.pop(j)
    print("   ", lll)
sterge_gol3(["Mike", "", "Emma", "Kelly", "", "Brad"])

print("\n-------Problema 16-------")
# ******Write a program that appends the square of each number to a new list. (o noua lista cu patratul fiecarui element)

def patrat(l):
    print(f'Lista1 = {l}')
    lll = []
    for i in l:
        lll.append(i*i)
    print(f'Lista2 = {lll}')

    ll = []
    for i in range(1,len(l)+1):
        ll.append(i*i)
    print(f'Lista3 = {ll}')

    llll = []
    for i in range(1,11):
        llll.append(i*i)
    print(f'Lista4 = {llll}')

patrat([3,2,10,1,8,6,7,0,9,5])

print("\n-------Problema 17-------")
#******Write a function that takes a list as a parameter and returns the reversed list. Do NOT use the built-in reverse() function.

z = [4, 7, 2, 3, 5, 22, 1, 0]
print("* direct", z)
m = z[::-1]
print("* invers", m)

def lista_inversa(l):
    print("* direct")
    for k in z:
        print(" ", k, end=" ")

    print("\n* invers")
    for i in range(len(l),0,-1):
        print(" ", l[i-1], end=" ")

    print("\n* invers")
    q = []
    for p in range(len(l))[::-1]:
        print(" ", l[p], end=" ")
        q.append(l[p])
    print("\n ", q)

    print("* invers")
    for j in m:
        print(" ", j, end=" ")

lista_inversa([4,7,2,3,5,22,1,0])

print("\n-------Problema 18-------")
#****** Write a python program to print the first 10 numbers Fibonacci series

a = 0
b = 1

for j in range(0,9): # iteratia Fibonnaci merge tot timpul de la 1 la n-1
    c = a + b
    a = b
    b = c
    print("-- ", b)
print("Fibonnaci de 10  -->", b)

def fibonacci(nr):
    a = 0
    b = 1
    if nr > 0 :
        for j in range(1, nr):
            c = a + b
            a = b
            b = c
        print(f'Fibonnaci de {nr} este', b)
    elif nr == 0:
        return 0
    else:
        print("Numar invalid")
fibonacci(10)


print("\n-------Problema 19-------")
# ****** Write a python program to read a number and print a right triangle using "*"

def brad1():
    n = int(input("Input : "))
    for i in range(1,n+1):
        brad = i * '* '
        print("",brad)
brad1()

def brad2():
    n = int(input("Input : "))
    for i in range(n+1)[:0:-1]:
        brad = i * '* '
        print("",brad)
brad2()

def brad3():
    n = int(input("Input : "))
    for i in range(n+1)[::-1] :
        brad = i * ' ' + '* ' + abs(i-n) * '* '
        print(brad)
brad3()

def prime1():

    n = int(input("Dati un numar: "))
    k = 0
    for i in range(1, n + 1) :
        if n % i == 0 :
            k += 1

    if k == 2:
        print(f'Numarul  -  {n}  -  este numar prim')
    else:
        print(f'Numarul  -  {n}  -  nu este numar prim')

prime1()

def prime2():
    l = []
    x = 0
    for j in range(2, 101):
        k = False
        for i in range(2, round(j/2)+1) :
            if j % i == 0 :
                k = True
        if k == False:
            print(f'Numarul  -  {j}  -  este numar prim')
            l.append(j)
            x += 1
    print(f'Lista numerelor prime intre 1 si 100 este: \n * {l}')
    print(f'Intre 1 si 100 avem  - {x} -  numere prime')

prime2()

def prim101():
    l = []
    k = 0
    for num in range(1, 101):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                l.append(num)
                k += 1
    print("Lista numerelor prime intre 1 si 100 este: ")
    print(" *",l)
    print(f'Intre 1 si 100 avem  - {k} -  numere prime')
prim101()
