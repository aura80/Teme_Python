from getpass import getpass

x = 5
y = 10
print("1. x + y = ", x + y)

print("---")
#integer
x = 20
#float
y = 10.5
#string
x = "Acesta este "
y = 'un sir de caractere'
print("2. x + y: ", x + y)

print("---")
restanta = 0
notaFinala = 10.0
laborator = "Introducere in informatica"
print("3. Tipul lui restanta este: ", type(restanta))
print("   Tipul lui notaFinala este: ", type(notaFinala))
print("   Tipul lui laborator este: ", type(laborator))

print("---")
x = 15
y = 2
print("4. 15 * 2 = ", x * y)

print("---")
sir = "Afara ninge"
print("5. Primul element al sirului nu este egal cu primul - ", sir[0]!=sir[10])

print("---")
str_x = "Emma is good developer. Emma is a writer"
sub = "Emma"
print("6. First string is: " + str_x)
print("   Substring is: " + sub)
rez = str_x.count(sub)
print(f'   Frecventa lui sub in str_x este de --- {rez} --- ori')

print("---")
str = "eu merg la mare"
l = len(str)
print(f'7,8. Lungime sir "eu merg la mare" = {l},  ', '"', str[0:2] + str[-2:] ,'"')

print("---")
string = "restart"
r = string[0:1]
d = "$"
newOrder = "resta{}t"
print("9. r --> $ : ", newOrder.format(d))

print("---")
print("10. I have 1000 dollars so I can buy 3 football for 450.00 dollars.")
print(f'    I have 1000 dollars so I can buy 3 football for 450.00 dollars.')
fir = '    I have {} dollars so I can buy {} football for {} dollars.'
totalMoney  = 1000
quantity  = 3
price  = 450.00

print(fir.format(totalMoney,quantity,price))

format_float = "{:.2f}".format(price)
print(fir.format(totalMoney,quantity,format_float))

firU = "    I have 1000 dollars so I can buy 3 football for 450.00 dollars."
print(firU.upper())
print(firU.lower())
print(len(firU))
print(firU[0:])
print(firU[0:-1])

print("---")
a = input("11. Latura mare a dreptunghiului este: ")
b = input("    Latura mica a dreptunghiului este: ")
r = input("    Raza cercului este:                ")
PI = 3.14
print("  * Aria dreptunghiului este:      -> ", int(a)*int(b))
print("    Perimetrul dreptunghiului este:   ", 2*(int(a) + int(b)))
print("    Aria cercului este:               ", PI*int(r)**2)

print("---")
print('foo\'bar')
print("""foo'bar""")
print("foo'bar")
#print('foo"bar')   # nu este ce se cere
#print('foo'bar')  -  nu este corect

print("---")
username = input("13. Define username: ")
password = input("    Define password: ")
s = 'The password for user {} is {} with {} characters long'

print(s.format(username, password, len(password)))
password = "*********".encode("utf-8")
print(s.format(username, password, len(password)))



