# # Question 1

# r = int(input("Enter the radius:"))
# area = 3.14 * r * r
# print("Area of the circle:", area)


# # Question 2

# f = float(input("Enter temperature in Fahrenheit:"))
# c= (f-32)*5/9
# print("Temperature in Celsius:", c)


# # Question 3

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operation = input("Enter operation (+, -, *, /): ")

# if operation == "+":
#     result = num1 + num25
# elif operation == "-":
#     result = num1 - num2
# elif operation == "*":
#     result = num1 * num2
# elif operation == "/":
#     result = num1 / num2
# else:
#     result = "Invalid operation"

# print("Result:", result)


# # Question 4

# import math
# num = int(input("Enter a number: "))
# sqt = math.sqrt(num)
# print("Square root of", num, "is", sqt)


# # Question 5

# import cmath
# a = int(input("Enter a number:"))
# b = int(input("Enter a number:"))
# c = int(input("Enter a number:"))

# d = (b**2) - (4*a*c)

# sol1 = (-b - cmath.sqrt(d)) / (2*a)
# sol2 = (-b + cmath.sqrt(d)) / (2*a)

# print("Solutions:", sol1, sol2)


# # Question 6

# import math
# a = float(input("Enter the value of a: "))
# b = float(input("Enter the value of b: "))
# c = float(input("Enter the value of c: "))

# s = (a + b + c) / 2  
# area = math.sqrt(s*(s-a)*(s-b)*(s-c))

# print("Area of the triangle:", area)


# # Question 7

# num = int(input("Enter a 5 digit number:"))

# sum = 0
# r = num % 10
# sum = sum + r

# num = num // 10
# r = num % 10
# sum = sum + r

# num = num // 10
# r = num % 10
# sum = sum + r

# num = num // 10
# r = num % 10
# sum = sum + r

# num = num // 10
# r = num % 10
# sum = sum + r

# print("Sum of digits:", sum)


# # Question 8

# s = "Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are"

# print(s)


# # Question 9

# Name = "Pranav Baghare"
# Age = 23
# Address = "Pune"

# print("Name:", Name)
# print("Age:", Age)
# print("Address:", Address)


# # Question 10

# str = "Hello, My name is 'Pranav Baghare'"
# print(str)


# #Question 11

# str = '''Hello, My name is "Pranav Baghare" and i live in 'bhopal'.'''
# print(str)


# # Question 12

# char = input("Enter the character:")
# int_rep = ord(char)

# print(int_rep)


# # Question 13

# s = "abc"
# s1 = s*5

# print(s1)


# #Question 14

# s = "-"

# print(s*50)

# #Question 15

# s = "hey hello how are you"

# s2=str.upper(s)

# print(s2)


# # Question 16 

# s = input("Enter the string:")
# if len(s) >= 2:
#     result = s[:2] + s[-2:]
# else:
#     result = "string is short"

# print(result)

# # Question 17 

# s = input("Enter the string:")
# first_char = s[0]
# modified_string = first_char + s[1:].replace(first_char, '$')
# print(modified_string)

# # Question 18

# s = input("Enter first string:")
# s1 = input("Enter second string:")
# new_s = s1[:2] + s[2:] + ' ' + s[:2] + s1[2:]
# print(new_s)


