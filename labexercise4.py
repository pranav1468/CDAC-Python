#question1
# Define the functions for each operation
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Cannot divide by zero"

# Main program loop
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

while True:
    choice = int(input("Enter choice (1/2/3/4/5): "))

    if choice == 1 or choice == 2 or choice == 3 or choice == 4:
        # Get the numbers after choosing the operation
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            result = add(num1, num2)
            print(num1, "+", num2, "=", result)

        elif choice == 2:
            result = subtract(num1, num2)
            print(num1, "-", num2, "=", result)

        elif choice == 3:
            result = multiply(num1, num2)
            print(num1, "*", num2, "=", result)

        elif choice == 4:
            result = divide(num1, num2)
            print(num1, "/", num2, "=", result)

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice.")


#Question 2

num = int(input("Enter a number: "))

a , b = 0 , 1
for i in range(num):
    a =b
    b=a+b
    print(a)

#question3
x=int(input("Enter a number: "))

double = list(map(lambda x: 2 ** x, range(x)))

print(double)

#question4
my_list = [int(i) for i in input("Enter numbers: ").split(",")]
x = my_list
div = lambda x: x % 13 == 0
print(list(filter(div, x)))

question 5
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Enter a number: "))
for i in range(n):
    print(fibonacci(i))

question6
def fac(n):
    if n <= 1:
        return n
    else:
        return n + fac(n-1)
n = int(input("Enter a number: "))
for i in range(n):
    print(fac(i))

#question7

import string

my_list = [i for i in input("Enter phrase: ").split(" ")]

list2 = "".join(my_list)

punch = string.punctuation

for i in punch:
    list2 = list2.replace(i, "")


list2 = list2.lower()

list3 = "".join(reversed(list2))

print(list3)
print(list2)

if list2 == list3:
    print("Palindrome")
else:
    print("Not a palindrome")

#question8
import string
def panagram(str1):
    alphabet = set(string.ascii_lowercase)
    return set(str1.lower()).issuperset(alphabet)

str1 = input("Enter a string: ")

if panagram(str1):
    print("Panagram")
else:
    print("Not a panagram")

#or

str1 = input("Enter a string: ")
alphabet = set("abcdefghijklmnopqrstuvwxyz")
if all(letter in str1.lower() for letter in alphabet):
    print("Panagram")
else:
    print("Not a panagram")

question9
list1 = list(input("Enter phrase: "))
list2 = list(input("Enter phrase: "))

def overlap(list1, list2):
    for i in list1:
        if i in list2:
            return True
    return False
print(overlap(list1, list2))

#question10
lis1 = [i for i in input("Enter first list: ").split(" ")]

def longest(lis1):
    longest = ""
    for i in lis1:
        if len(i) > len(longest):
            longest = i
    return longest, len(longest)

longest, len = longest(lis1)
print("Longest word:", longest, "with length", len)

# #0r
word = input("Enter first list: ").split(" ")
def longest(lis1):
    m = 0 
    for word in lis1:
        m= max(m, len(word))
    return m

print(longest(word))


question11

def filter_long_words(lis1, n):
    result = []
    for i in lis1:
        if len(i) > n:
            result.append(i)
    return result

list1 = [i for i in input("Enter first list: ").split(" ")]
n = int(input("Enter the minimum length: "))

print("words longer than", n, "are:", filter_long_words(list1, n))




