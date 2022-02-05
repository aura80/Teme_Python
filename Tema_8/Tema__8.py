#Check for anagram
def anagram1():
    a = "Desperation"
    b = "A Rope Ends It"
    a = a.lower()
    b = b.lower()
    bb = b.split()
    print("\na =  ",a)
    print("b =  ",b)
    print("b.split() =  ",bb)
    tt = []
    ll = []

    s = 0
    t = 0
    for i in a:
        for j in range(len(bb)):
            for k in bb[j]:
                if i == k:
                    s += 1
                    #print("Anagram",i,s)
                    tt.append(i)
                    ll.append(k)
            t += len(bb[j])
        if len(a) == t:
            z = t
    print(f'The number of letters which are the same is:   {z}')
    print("tt =    ",tt)
    print("ll =    ",ll)
    if tt == ll:
        print("              tt == ll       --->         We have anagrams!\n")
#anagram1()

def anagram2():
    a = "Desperation"
    b = "A Rope Ends It"
    a = a.lower()
    b = b.lower()
    l, t = [],[]
    for i in a:
        for j in b:
            if i == j and j != ' ':
                c = "Anagrams: "
                l.append(i)
                t.append(j)
    print("\n", c)
    print("l =  ", l)
    print("t =  ", t)
    print()
#anagram2()


def anagram3(a, b):
    a = a.lower()
    b = b.lower()
    x = sorted(a)
    y = sorted(b)
    print("\n     Lower case strings:")
    print("  - ", a)
    print("  - ", b)
    print("     Sorted strings:")
    print("x =  ",x)
    print("y =  ",y)
    l = []
    for i in y:
        y.remove(' ')
        print("***  ",y)
        if i != ' ':
            print("y =  ",y)
            break

    if x == y :
        print("             x == y      --->     Strigs are anagrams!\n")
    else:
        print("Strigs are not anagrams!")

a = "Desperation"
b = "A Rope Ends It"

#anagram3(a,b)
from collections import Counter
def anagram4():
    a = "armura"
    b = ["murara", "macara", "ramura", "uraram", "aur", "urmara", "tei"]
    l = list()
    m = list()

    x = sorted(a)
    print(f'\nSorted "{a}" is: {x}')
    y = Counter(a)
    for i in range(len(b)):
        s = sorted(b[i])
        if x == s and y == Counter(s):
            l.append(s)
            m.append(b[i])
            z = Counter(s)
    print(f'Sorted anagrams are: {l}')
    print(f'Anagrams for \'{a}\' are: {m}\n')
    print(f'Counter for "{a}" is:   {y}')
    print(f'Counter for anagrams is:   {z}\n')

def min_array1():
    l = [4,8,6,1,2,9,4]
    m = []
    for i in range(0, len(l)-1):
        d = l[i+1] - l[i]
        m.append(abs(d))
        minim = None
        for j in range(len(m)):
            if minim is None:
                minim = m[j]
            elif m[j] < minim:
                minim = m[j]
                idx = j
        mini = m[0]
        for j in range(len(m)):
            if m[j] < mini:
                mini = m[j]
                idex = j

    print("Minim: {}  Index: {}".format(minim,idx))
    print(f'Minim: {mini}  Index: {idex}')

def min_array2():
    l = [4,8,6,1,2,9,4]
    m = min(l)
    index = l.index(m)
    print(f'Minim: {m}  Index: {index}')

def min_array():
    l = [4,8,6,1,2,9,4]
    m = []
    print("\nLista: ")
    print(l)
    for i in range(0, len(l)-1):
        d = l[i+1] - l[i]
        m.append(abs(d))
        if min(m) == m[i]:
            index = i
    print("Differences: ")
    print(m)
    print(f'\nThe minimum difference between the elements of the array is: {min(m)} with index {index}\n')
    min_array1()
    min_array2()
#min_array()

def menu():
    print("-----------------------------------------------------MENU----------------------------------------------------\
    \n 1 - anagram1();    2 - anagram2();     3 - anagram3();     4 - anagram4();     5 - min_array()     6 - Exit")
    print()
    i = int(input("Alegeti optiunea: "))
    while True:
        if i == 1:
            anagram1()
            menu()
        elif i == 2:
            anagram2()
            menu()
        elif i == 3:
            anagram3(a,b)
            menu()
        elif i == 4:
            anagram4()
            menu()
        elif i == 5:
            min_array()
            menu()
        elif i == 6:
            print("exit")
            exit()
        else:
            print("Option does not exist!")
            menu()

menu()

















