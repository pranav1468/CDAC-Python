# Question 1

class bank_account():

    def inital_value(self):
        self.Depositer_name = input("Name of the Depositer:")
        self.Account_number = int(input("Account Number:"))
        self.Account_type = input("Type of Account:")
        self.Account_Balance_amount = float(input("Balance amount in the account:"))
    
    def deposit(self):
        self.amount =  float(input("Deposit Amount"))
        self.Account_Balance_amount = self.Account_Balance_amount + self.amount
    
    def withdraw(self):
        self.wd = float(input("Withdraw Amount:"))
        self.Account_Balance_amount = self.Account_Balance_amount - self.wd

    def display(self):
        print(self.Depositer_name)
        print(self.Account_Balance_amount)


m= bank_account()
while True:
    print("1. New Coustomer")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter Your choice:"))

    if choice == 1:
        m.inital_value()
    elif choice == 2:
        m.deposit()
    elif choice == 3:
        m.withdraw()
    elif choice == 4:
        m.display()
    elif choice == 5:
        exit()
    else:
        print("Invalid Choice")
        choice = int(input("Enter choice: "))


# Question 2

class staff():
    def __init__(self, code, name):
        self.code = code
        self.name = name
    def display(self):
        print(f"Code: {self.code}")
        print(f"Name: {self.name}")

class teacher(staff):
    def __init__(self, code, name, subject, publication):
        self.code = code
        self.name = name
        self.subject = subject
        self.publication = publication
    
    def display(self):
        super().display()
        print(f"Subject: {self.subject}")
        print(f"Publication: {self.publication}")

class typist(staff):
    def __init__(self,code, name, speed):
        self.code = code
        self.name = name
        self.speed = speed
    
    def display(self):
        super().display()
        print(f"Typing Speed: {self.speed}")


class officer(staff):
    def __init__(self,code, name, grade):
        self.code = code
        self.name = name
        self.grade = grade

    def display(self):
        super().display()
        print(f"Grade: {self.grade}")

class regular(typist):
    def __init__(self,code, name, speed, salary):
        self.code = code
        self.name = name
        self.speed = speed
        self.salary = salary
    
    def display(self):
        super().display()
        print(f"Salary: ₹{self.salary}")

class casual(typist):
    def __init__(self,code, name, speed, daily_wages):
        self.code = code
        self.name = name
        self.speed = speed
        self.daily_wages = daily_wages

    def display(self):
        super().display()
        print(f"Daily Wages: ₹{self.daily_wages}")

while True:
    print("1. Teacher")
    print("2. Officer,")
    print("3. Regular Typist")
    print("4. Casaul typist")
    print("5. Exit")
    choice = int(input("Enter Your choice:"))

    if choice == 1:
        a = teacher(1, "pratyush", "Math", "R.s.Agrawal")
        a.display()
    elif choice == 2:
        b = officer(1, "Navnesh", 1500)
        b.display()
    elif choice == 3:
        c = regular(1, "prashant", "15s", 50000)
        c.display()
    elif choice == 4:
        d = casual(1, "Vishal", "10s", 500)
        d.display()
    elif choice == 5:
        exit()
    else:
        print("Invalid Choice")
        choice = int(input("Enter choice: "))
