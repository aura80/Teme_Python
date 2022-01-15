def noua():
    f = [1, 2, 9, 9, 9, 9, 9]
    i = 0
    s = 0
    while i in range(len(f)):
        if f[i] == 9:
            s += 1
        i = i + 1
    print(f'Cifra 9 se regaseste in {f} de {s} ori')
# noua()

def omite():
    l = []
    z = []
    i = 0
    while i in range(7):
        z.append(i)
        if i != 3 and i != 6:
            l.append(i)
        else:
            pass
        i += 1
    print(f'Lista {z} fara 3 si 6 este l = {l}')
# omite()

def sum20_100():
    i = 20
    sum = 0
    while i in range(20,101):
        sum = sum + i
        i = i + 1
    print("Sum = ", sum)
# sum20_100()

def Fizz_Buzz():
    i = 1
    while i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        i += 1
# Fizz_Buzz()

def multi(n):
    i = 1
    while i in range(1,11):
        p = n * i
        i += 1
        print(f' {n} x {i - 1} = ', p)
# multi(3)

def pattern():
    i, j = 1, 0
    while i in range(1, 10):
        while j in range(i):
            print(f' {i}' * i )
            j += 1
        i += 1
# pattern()

def desc1(n):
    l = []
    i = 0
    while i in range(n):
        l.append(n - i - 1)
        i += 1
    print(f'Primele \' {n} \' numere in ordina descrescatoare:', l)

# desc1(10)
# desc1(15)
# desc1(12)

def desc3():
    l = [5,7,3,1,3,2,4,8]
    print("Lista:  ",l)
    l.reverse()
    print("Invers: ", l)
    l.sort()
    l.reverse()
    print("Descrescator: ", l)

# desc3()

def min_max():
    lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
    minim = min(lst)
    maxim = max(lst)
    print(f' -- * ---  {lst}  --- * -- ')
    print(f'Minimul este: {minim}\nMaximul este: {maxim}')

    lsst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
    i = 0
    minimum = lsst[0]
    maximum = lsst[0]
    while i in range(len(lsst)):
        if lsst[i] >= maximum:
            maximum = lsst[i]
        elif lsst[i] <= minimum:
            minimum = lsst[i]
        i += 1

    print(f' --- Minimul este {minimum}, iar maximul este {maximum} ')

# min_max()

def how_many_times():
    lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
    l = [5, 2, 7, 8, 5, 7, 9, 2, 3, 3, 3, 2, 8]
    s = lst.count(6)
    print(f' Cifra 6 se gaseste de --- {s} --- ori in lista {lst}')

    i = 0
    s = 0
    while i in range(len(l)):
        if l[i] == 8:
            s += 1
        i += 1
    print(f' Cifra 8 se gaseste de --- {s} --- ori in lista {l} ')

# how_many_times()

def sterge0():
    lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
    print("Lista initiala:", lst)
    lst.reverse()
    lst.remove(lst[0])
    lst.reverse()
    print("Cu remove():   ", lst)
# sterge0()

def sterge1():
    lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
    l = []
    i = 0
    while i in range(0, len(lst)):
        if i == len(lst) - 1:
            #lst.remove(lst[i])
             pass
        else:
            l.append(lst[i])
        i += 1
    print("Cu WHILE:      ", l)
# sterge1()

def concatenare():
    list1 = ["Hello ", "take ", "tv "]
    list2 = ["Dear", "Sir", "antena "]

    l = []
    m = []

    for i in range(len(list1)):
        for j in range(len(list2)):
                l.append(list1[i] + list2[j])
    print("Cu FOR:               ", l)

    i = 0
    while i in range(len(list1)):
        for j in range(len(list2)):
            t = list1[i] + list2[j]
            m.append(t)
        i += 1
    print("Cu WHILE si FOR:      ", m)

    res = [x + y for x in list1 for y in list2]
    print("Pe scurt:             ", res)

# concatenare()

def sub_list1():
    gift_list = ['socks', '4K drone', 'wine', 'jam']
    gift_list.extend(["socks", "tshirt", "pajamas"])
    print("Cu extend():  ", gift_list)
# sub_list1()

def sub_list2():

    gift_list=['socks', '4K drone', 'wine', 'jam']
    l = []

    i = 0
    while i in range(len(gift_list)+1):
        if i == 3:
            gift_list += ["socks", "tshirt", "pajamas"]
            l.append(gift_list)
        i += 1
    print("Cu While:     ", gift_list)
    print("Cu lista noua:", l)

# sub_list2()

def diag():
    l = [[1, 3, 5], [1, 4, 6], [7, 6, 9]]
    #print(l[0:][0:])

    a = 0
    while a in range(len(l)):
        print(l[a])
        a += 1

    b = '-'
    i = 0
    s = 0
    while i in range(len(l)):
        #print(f'Indexul liniei este:  {i} ')
        for j in l[i][i:i+1]:
            print(f'Elementul  l[{i}][{i}]  pe diagonala este:  {j}')
            s = s + j
        i += 1

    print(f'{41*b} \nSuma elementelor de pe diagonala este: ', s)
# diag()

def add_list1():
    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    #print(list1[2][2])
    list1[2][2].append(7000)
    print(list1)
# add_list1()

def add_list2():
    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

    i = 0
    while i in range(len(list1)):
        for j in range(len(list1[2:])):
            if i == 2 and j == 2:
                t = list1[i][j]
                t.append(7000)
        i += 1
    print(list1)

# add_list2()

def twenty():
    list1 = [5, 10, 15, 20, 25, 50, 20]
    i = 0
    while i in range(len(list1)):
        if list1[i] == 20:
            list1[i] = 200
            break
        i += 1
    print(list1)

# twenty()

def empty1():
    s = ["Mike", "", "Emma", "Kelly", "", "Brad"]
    print("Lista initiala1: ", s)
    i = 0
    while i in range(len(s)):
        if s[i] == "":
            t = s.index(s[i])
            s.pop(t)        # echivalent cu     del s[t]
        i += 1
    print("Lista finala1:   ", s)

# empty1()

def empty2():
    s = ["Mike", "", "Emma", "Kelly", "", "Brad"]
    print("Lista initiala2: ", s)
    i = 0
    while i in range(len(s)):
        if s[i] == "":
            s.remove(s[i])
        i += 1
    print("Lista finala2:   ", s)

# empty2()

def square1(n):
    #.split()
    #print(n)
    #l = []
    #l.extend(n)
    print("Lista:            ", n)
    new_l = []
    i = 0
    while i in range(len(n)):
        # n = int(input("Dati lista: "))
        new_l.append(n[i] * n[i])
        i += 1
    print("Lista patratelor: ", new_l)

# square1([5, 3, 1, 2, 4, 7])

def square2(l):
    print(f'Lista:             {l}')
    g = []
    i = 0
    while i in range(len(l)):
        z = l[i]
        g.append(z * z)
        i += 1
    print(f'Lista patratelor:  {g}')

# square2([2,7,8,9,1,2,5,4,3])

def square3():
    new_l = []
    l = []
    i = 0
    while i in range(5):
        n = int(input("Dati numarul: "))
        l.append(n)
        new_l.append(n * n)
        i += 1
    print(f'Lista:             {l}')
    print("Lista patratelor: ", new_l)

# square3()

def square4():            # de pe net
      l = [5,8,3,1,2,4,8,7,6,9]
      print("           ", l)
      i = 0
      while i in range(len(l)):
          print("Elementul cu index {} care initial era {} este acum:  {} ".format(i,l[i],l[i]*2))
          i += 1
# square4()

def inversa1(l):
    m = []
    m.append(l[::-1])
    return m

# print("Inversa:\t\t\t", inversa1([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))

def inversa2(l):
    i = 1
    m = []
    while i in range(1,len(l)+1):
        #m.append(abs(i - len(l) - 1))
        z = len(l) - i + 1
        m.append(z)
        i += 1

    return m

# print(f'Inversa cu WHILE: \t {inversa2([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])} ')

def Fibonacci(n):
    a = 0
    b = 1
    i = 0

    while i in range(0, n-1):  # iteratia Fibonnaci merge tot timpul de la 1 la n-1
        c = a + b
        a = b
        b = c
        print("-- ", b)
        i += 1
    print(f'Fibonnaci de {n}  --> ', b)

# Fibonacci(10)
# Fibonacci(20)

def triunghi():

    n = int(input("Dati numarul: "))
    i = 1
    p = 1
    while i in range(1,n+1):
        p = i * '* '
        print(p)
        i += 1

# triunghi()

def nr_prim():

    n = int(input("Dati un numar: "))
    k = 0
    i = 1
    while i <= n:
        if n % i == 0 :
            k += 1
        i += 1
    if k == 2:
        print(f'Numarul  -  {n}  -  este numar prim')
    else:
        print(f'Numarul  -  {n}  -  nu este numar prim')

# nr_prim()

def prime100():
    l = [2]
    x = 0
    j, i = 1, 2

    while j in range(1, 101):
        k = True
        while i in range(2, round(j/2)+1) :
            if j % i == 0 :
                k = False
            if k:
                l.append(j)
                x += 1
            i += 1
        j += 1
    print(f'Lista numerelor prime intre 1 si 100 este: \n{l}')
    print(f'Intre 1 si 100 avem  - {x} -  numere prime')

# prime100()

def meniu():

    while True:
        print("\n-------MENIU-------")
        print("1. Problema 'de cate ori 9'              6. Problema 'pattern'        11. Problema 'concatenare'             16. Problema 'remove empty \"\" '   21. Problema 'nr prim'             \n"
              "2. Problema 'omite doua cifre'           7. Problema 'descrescator'   12. Problema 'sub_list'                17. Problema 'square'             22. Problema 'nr prime in interval'  \n"
              "3. Problema 'suma nr. intre 20 si 100'   8. Problema 'min-max'        13. Problema 'suma pe diagonala'       18. Problema 'inversa'            23. Exit                             \n"
              "4. Problema 'Fizz-Buzz'                  9. Problema 'how many times' 14. Problema 'add-list 7000'           19. Problema 'Fibonacci'                                               \n"
              "5. Problema 'multiplu de n'              10. Problema 'sterge'        15. Problema 'inlocuieste 20 cu 200'   20. Problema 'triunghi * '                                             \n"
              )
        n = int(input("Alege problema: "))
        if n == 1:
            noua()
            #meniu()
        elif n == 2:
            omite()
            #meniu()
        elif n == 3:
            sum20_100()
            #meniu()
        elif n == 4:
            Fizz_Buzz()
            #meniu()
        elif n == 5:
            multi(3)
            #meniu()
        elif n == 6:
            pattern()
           #meniu()
        elif n == 7:
            desc1(10)
            desc1(15)
            desc1(12)
            desc3()
            #meniu()
        elif n == 8:
            min_max()
            #meniu()
        elif n == 9:
            how_many_times()
            #meniu()
        elif n == 10:
            sterge0()
            sterge1()
            #meniu()
        elif n == 11:
            concatenare()
            #meniu()
        elif n == 12:
            sub_list1()
            sub_list2()
            #meniu()
        elif n == 13:
            diag()
            #meniu()
        elif n == 14:
            add_list1()
            add_list2()
            #meniu()
        elif n == 15:
            twenty()
            #meniu()
        elif n == 16:
            empty1()
            empty2()
            #meniu()
        elif n == 17:
            square1([5, 3, 1, 2, 4, 7])
            square2([2, 7, 8, 9, 1, 2, 5, 4, 3])
            square3()
            square4()
            #meniu()
        elif n == 18:
            print("Inversa:\t\t\t", inversa1([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
            print(f'Inversa cu WHILE: \t {inversa2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])} ')
            #meniu()
        elif n == 19:
            Fibonacci(10)
            Fibonacci(20)
            #meniu()
        elif n == 20:
            triunghi()
            #meniu()
        elif n == 21:
            nr_prim()
            #meniu()
        elif n == 22:
            prime100()
            #meniu()

        elif n == 23:
            exit()
        else:
            print("Problema inexistenta")


meniu()

def meniu2():
        print("\n-------MENIU-------")
        print("1. Problema 'de cate ori 9'              6. Problema 'pattern'        11. Problema 'concatenare'             16. Problema 'remove empty \"\" '   21. Problema 'nr prim'             \n"
              "2. Problema 'omite doua cifre'           7. Problema 'descrescator'   12. Problema 'sub_list'                17. Problema 'square'             22. Problema 'nr prime in interval'  \n"
              "3. Problema 'suma nr. intre 20 si 100'   8. Problema 'min-max'        13. Problema 'suma pe diagonala'       18. Problema 'inversa'            23. Exit                             \n"
              "4. Problema 'Fizz-Buzz'                  9. Problema 'how many times' 14. Problema 'add-list 7000'           19. Problema 'Fibonacci'                                               \n"
              "5. Problema 'multiplu de n'              10. Problema 'sterge'        15. Problema 'inlocuieste 20 cu 200'   20. Problema 'triunghi * '                                             \n"
              )
        n = int(input("Alege problema: "))
        a = noua()
        b = omite()
        c = sum20_100()
        d = Fizz_Buzz()
        e = multi(3)
        f = pattern()
        l = [a, b, c, d, e, f]
        l[3]
        # for i in range(0, 6):
        #     if n == i+1:
        #         l[i]
        #         break
        #     else:
        #         exit

meniu2()














