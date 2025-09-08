# # first = "pranav"
# # last = "baghare"
# # age = 23

# # print("my first name is {} my last name is {} and my age is {}".format(first, last, age))


# number1 = int(input("Number1:"))
# number2 = int(input("number2:"))
# n = number1 * number2
# s = number1 + number2

# if n <= 1000:
#     print(f"The result is {n}")
# else:
#     print(f"The result is {s}")

# s = 0
# for i in range(1, 11):
#     s += i
#     print(f"Current Number {i} Previous Number {i-1} Sum: {s}")

# str1 = input("Enter a string")

# for i in range(0, len(str1)-1, 2):
#     print(str1[i])

# str1 = input("Enter a string:")
# n = int(input("Enter a number:"))

# str2 = str1[n:] 

# print(str2)


# def genrator():
#     i = 0
#     for i in range(1, 550):
#         yield i

# g = genrator()
# print(genrator())
# print(next(g))


# def decor(funct):
#     def wrapper():
#         gen = funct()
#         print("decorated: first value:", next(gen))
#         return gen
#     return wrapper

# @decor
# def genrator():
#     i = 0
#     for i in range(1, 550):
#         yield i

# g = genrator()
# print(genrator())
# print(next(g))

# import sys
# try:
#     a = 10
#     b = 2
#     print(a/b)
#     l1 = [1, 2, 3]
#     print(l1[4])
#     print(cdac)
# except (ZeroDivisionError, IndexError, NameError):
#     print("Error: ", sys.exc_info()[1])

                                    ##PRACTICE######
#question1
# def greet():
#     name = input("enter your name: ")
#     print("Hello", name)

# greet()

#question2
# def square():
#     num = int(input("enter your num:"))
#     print(num*num)

# square()

#question3
# def is_even():
#     num = int(input("enter a number: "))
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("false")

# is_even()

#question4
# def sum():
#     num1 = int(input("enter a number:"))
#     num2 = int(input("enter a number"))
#     print(num1+num2)

# sum()

# question5
# def area_of_circle():
#     r = int(input("enter a radius"))
#     print(3.14 * r*r)
# area_of_circle()

#question6
# def factorial():
#     n = int(input("enter a number:"))
#     x = 1
#     for i in range(1, n+1):
#         x = x*i
#         print(x)
# factorial()