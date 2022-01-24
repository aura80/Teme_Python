'''1. Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.
Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another Volume() method to calculate
the volume of the Parallelepiped'''

def Pr1():
    print("--- Problem 1 - class Rectangle ---")
    print()

    class Rectangle:
        def __init__(self, lungime, latime):  # constructorul clasei
            self.lungime = lungime
            self.latime = latime

        def Perimeter(self):  # metodele clasei - arata behaviour
            p = 2 * (self.lungime + self.latime)
            print("1 - Perimetrul este 2*({}+{}) = {} ".format(self.lungime, self.latime, p))

        def Area(self):
            a = self.lungime * self.latime
            print("2 - Aria este {}*{} = {} ".format(self.lungime, self.latime, a))
            return a

    perimetru = Rectangle(8, 2)  # instanta = apelarea clasei
    perimetru.Perimeter()  # apelarea metodei
    aria = Rectangle(8, 2)
    aria.Area()

    # print(perimetru.lungime)

    def Display():
        l = Rectangle(12, 3)
        print(f' *** Lungimea este: {l.lungime}')
        print(f' *** Latimea este: {l.latime}')
        l.Perimeter()
        l.Area()

    Display()
    print("---------------------------------------")

    class Parallelepipede1(Rectangle):
        high = 35
        ari = Rectangle(30, 20)
        ar = ari.Area()

        def Volume(self):
            V = self.ar * self.high
            print("3 - Volumul este {} * {} = {} ".format(self.ar, self.high, V))

    vol = Parallelepipede1(30, 20)
    # print(vol.ar)
    vol.Volume()

    class Parallelepipede2(Rectangle):
        def __init__(self, high, lungime, latime):
            super().__init__(lungime, latime)
            self.high = high

        def Volume(self):
            V = self.lungime * self.latime * self.high
            print("3' - Volumul este {} * {} * {} = {} ".format(self.lungime, self.latime, self.high, V))

    vol = Parallelepipede2(35, 30, 20)
    vol.Volume()
    print()


Pr1()

'''2. Define a Book class with the following attributes: Title, Author (Full name), Price.
Set the View() method to display information for the current book.'''


def Pr2():
    print("--- Problem 2 - class Book ---")
    print()

    class Book:
        Title = "Amintiri din copilarie"
        Author = "Ion Creanga"
        Price = 35

        def View(self):
            print("Lucrarea '{}' este scrisa de {} si costa {} lei. ".format(self.Title, self.Author, self.Price))

    b = Book()
    b.View()
    print()


Pr2()

'''3. Create a Python class Person with attributes: name and age of type string.
Create a display() method that displays the name and age of an object created via the Person class.
Create a child class Student  which inherits from the Person class and which also has a section attribute.
Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
Create a student object via an instantiation on the Student class and then test the displayStudent method.'''


def Pr3():
    class Person:
        print("--- Problem 3 - class Person ---")
        print()

        def __init__(self, name, age):  # constructorul clasei
            self.name = name
            self.age = age

        def display(self):
            print(f'*** {self.name} is {self.age} years old. ')

    p = Person("Mariana", "32")
    p.display()

    class Student(Person):
        def __init__(self, year, course, mark, name, age):
            super().__init__(name, age)
            self.year = year
            self.course = course
            self.mark = mark

        def displayStudent(self):
            pers1 = Person("Ana", "22")
            pers1.display()
            print("*\tPerson: ", pers1.name, "\n\tAge:\t", pers1.age, "\n\tYear:\t", self.year, "\n\tCourse: ",
                  self.course, "\n\tMark:\t", self.mark)
            print(
                f'* \t{self.name} is {self.age} years old\n\tYear of study:\t\t{self.year}\n\tCourse followed:\t{self.course}\n\tMark obtained: \t\t{self.mark}')

    s = Student(2, "Math", "10", "Ioana", "20")
    s.displayStudent()
    print()


Pr3()

'''4.Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
Create a constructor with parameters: accountNumber, name, balance.
Create a Deposit() method which manages the deposit actions.
Create a Withdrawal() method  which manages withdrawals actions.
Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
Create a display() method to display account details.'''

def Pr4():
    class BankAccount:
        print("----------------------------------------- Problem 4 - class BankAccount ------------------------------------------")
        print()

        def __init__(self, accountNumber, name, balance):
            self.accountNumber = accountNumber
            self.name = name
            self.balance = balance

        def Deposit(self):
            print("\n---------------------------------DEPOSIT-------------------------------")
            print("Choose between the two accounts no. and names:   123 - Mark Twain / 124 - Tom Sawyer")
            c = int(input("Add account no.: "))
            n = input("Add account owner: ")
            print("-------------------------")
            print(f'Account no. : {self.accountNumber}\nOwner\'s name: {self.name}\nBalance:      {self.balance} $')
            d = {c: n, n: 0}
            l = []
            while True:
                if c == self.accountNumber and n == self.name:
                    bani = float(input("Add money(0 out): "))
                    self.balance += bani
                    print(f'New balance: {round(self.balance, 2)} $ ')
                    if bani == 0:
                        d.update({c: n, n: self.balance})
                        l.append(self.balance)
                        print(d)
                        print(f'\n *    Cont no.: {self.accountNumber} -> {round(d[self.name],2)} $ cash')
                        for i in range(len(l)):
                            pass
                        print(f' *    {self.name} has in his account {round(l[i],2)} $\n')
                        ret = l[i]
                        return ret
                        exit()
                    # print()
                else:
                    print("Account no. or name do not match! ")
                    exit()

        def Withdrawal(self):
            print("-------------------------------WITHDRAWAL------------------------------")
            wd = float(input("Withdrawal amount: "))
            self.balance -= wd
            print(f'The amount left in {self.name}\'s account is: {round(self.balance, 2)} $\n')

        def bankFees(self, per):
            print("----------------------------------FEES---------------------------------")
            self.per = per
            percent = float(self.per / 100) * self.balance
            percentage = self.balance - percent
            print(f'Taxes {self.per}% ')
            print(f'{self.name} pays {round(percent, 2)} $ in taxes')
            print(f'{self.name} still has {round(percentage, 2)} $ in his account after paying his taxes\n')

        def display(self):
            print("--------------------------------DISPLAY--------------------------------")
            print(f'--> Owner: {self.name}; ' + ' ---' + " Account no. " + f'{self.accountNumber}; ' + ' --' + " Amount: " + f'{round(self.balance, 2)} $; ' + ' --' + " Taxes: " + f'{round(float(self.per / 100) * self.balance,2)} $  representing {self.per}% fees')
            print()
        def displ(self):
            print(f' ---->  Owner: {self.name}; ' + ' ---' + " Account no. " + f'{self.accountNumber}; ' + ' --' + " Amount: " + f'{round(self.balance, 2)} $; ' + ' --' + " Taxes: " + f'{round(float(5 / 100) * self.balance,2)} $  representing 5% fees')

    d = BankAccount(123, "Mark Twain", 8000)
    da = BankAccount(124, "Tom Sawyer", 500)
    d.displ()
    da.displ()

    for i in range(1,4):
        i = int(input("\nChoose 1 (first client), 2 (second client), 3 (quit) : \n"))
        if i == 1:
            b = BankAccount(123, "Mark Twain", 8000)
            b.Deposit()
            b.Withdrawal()
            b.bankFees(5)
            b.display()
        elif i == 2:
            ba = BankAccount(124, "Tom Sawyer", 500)
            ba.Deposit()
            ba.Withdrawal()
            ba.bankFees(5)
            ba.display()
        elif i == 3:
            exit()

Pr()

'''5
1 - Create a Coputation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.
2 - Create a method called Factorial() which allows to calculate the factorial of an integer. Test the method by instantiating the class.
3 - Create a method called Sum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Test this method.
4 - Create a method called testPrim() in  the Calculation class to test the primality of a given integer. Test this method.
5 - Create  a method called testPrims() allowing to test if two numbers are prime between them.
6 - Create a tableMult() method which creates and displays the multiplication table of a given integer. 
7. Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.
6 - Create a static listDiv() method that gets all the divisors of a given integer on new list called  Ldiv. 
8. Create another listDivPrim() method that gets all the prime divisors of a given integer.'''

class Computation:
    print("\n--- Problem 5 - class Integers ---")
    print()
    def __init__(self):
        self.n1 = 100
        self.n2 = 300
    def Suma(self):
        sum = self.n1 + self.n2
        print("Suma: ", sum)
    def Dif(self):
        dif = self.n2 - self.n1
        print("Diferenta: ", dif)
    def testPrim(self):
        pass

class Multi(Computation):
    def Mul(self):
        mul = self.n1 * self.n2
        print("Multiplicare: ", mul)
    def Div(self):
        div = self.n2 / self.n1
        print("Impartire: ", div)
    def Factorial(self, n):
        self.n = n
        p = 1
        for i in range(1,n+1):
            p = p * i
        print(f'Factorialul lui {self.n} este: {p}')
    def Sum(self, n):
        self.n = n
        s = 0
        for i in range(1,n+1):
            s = s + i
        print(f'Suma primelor {self.n} numere este: {s}')


s = Multi()
s.Suma()
s.Dif()
s.Mul()
s.Div()
s.Factorial(5)
s.Sum(5)


