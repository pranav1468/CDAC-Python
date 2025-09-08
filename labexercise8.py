# #Question 1
# from abc import ABC, abstractmethod
# class Appliance(ABC):
#     @abstractmethod
#     def turn_on(self):
#         pass

#     @abstractmethod
#     def turn_off(self):
#         pass

# class fan(Appliance):
#     def turn_on(self):
#         print("Fan is now ON.")

#     def turn_off(self):
#         print("Fan is now OFF.")   

# class light(Appliance):
#     def turn_on(self):
#         print("Light is now ON.")

#     def turn_off(self):
#         print("Light is now OFF.")

# f = fan()
# f.turn_on()
# f.turn_off()

# L = light()
# L.turn_on()
# L.turn_off()

# Question 2

# from abc import ABC, abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     def display_shape(self):
#         print("the shape is displayed")

# class circle(shape):
#     def area(self):
#         r = int(input("Enter the radius"))
#         area = 3.14*r*r
#         print(area)

#     def display_shape(self):
#         super().display_shape()
    
# class rectangle(shape):
#     def area(self):
#         w = int(input("Enter the width:"))
#         l = int(input("Enter the length:"))
#         area = w*l
#         print(area)

#     def display_shape(self):
#         super().display_shape()
    
# c = circle()
# c.area()
# c.display_shape()

# r = rectangle()
# r.area()
# r.display_shape()

# #Question 3

# def greed():
#     print("how are you")

# greed()

# def decor(func):
#     def wrapper():
#         print("hello")
#         func()
#     return wrapper
    
# @decor
# def greed():
#     print("how are you")

# greed()

# Question 4

# def log_argument(func):
#     def wrapper(*args, **kwargs):
#         print("Argument are:", args, kwargs)
#         func(*args, **kwargs)
#     return wrapper

# @log_argument
# def greed(num, name):
#     print(f"the name is {num} and the number is {name}")

# greed(2,"pranav")

# Question 5

# def log_method_call(func):
#     def wrapper(*args, **kwargs):
#         print("Calling method:",func.__name__)
#         func(*args, **kwargs)
#     return wrapper

# class myclass():
#     @log_method_call
#     def greet(self):
#         print("hello, you have entered the room")

# d= myclass()
# d.greet()

# [EXCEPTION HANDLING]

# Question 1

# try:
#     def div():
#        a= 5/0
#     div()
# except ZeroDivisionError as ex:
#     print("Error: cannot be divided by zero")

# Question 2
# try:
#     list = [0,1,3,5]
#     list[6]
# except IndexError as ex:
#     print(ex)

# Question 3
# file_path = input("Enter the file name")
# try:
#     f = open(file_path, 'r')
#     content = f.read()
#     print("content:", content)
#     f.close()

#     n = int(input("Enter the input"))
#     f = open(file_path, 'w')
#     f.write(str(n))
#     f.close()

# except FileNotFoundError:
#     print("Error: File not found")
# except ValueError:
#     print("Error this is not a value")

# Question 4

# class InvalidageError(Exception):
#     pass

# try:
#     age = int(input("Enter the aage:"))
#     if age < 0 or age > 150:
#         raise InvalidageError("Age is not in the range")
    
# except InvalidageError:
#     print("Age is not in the range")

# Question 5 

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# try:
#     c = a/b
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")

# else:
#     print(c)

# finally:
#     print("Operation completed")

# Question 6

# str1 = input("Enter the string:")
# try:
#     if str1 == "":
#         raise TypeError("Error: The empty string is not allowed")
    
#     num = int(str1)
#     print(num)

# except ValueError:
#     print("Error the value is invalid")

# except TypeError:
#     print("Error: The empty string is not allowed")

# Question 7

# def func1():
#     a = 5
#     b = 0
#     if b == 0:
#         raise ZeroDivisionError("this is not divisible by 0")
#     print(a/b)
        
# def func2():
#     try:
#         func1()
#     except ZeroDivisionError as ex:
#         print("error occured: error", ex)
#         raise ValueError("Error occured")
# try:
#     func2()
# except ValueError as err:
#     print("Caught ValueError in main block:", err)



# Question 8

# List1 = [0, 'a', 5, 68]
# dic1 = {'name': 'PRANAV', 'age': 23, 'city': 'bhopal'}
# try:
#     List1[6]
# except (IndexError, KeyError) as ex:
#     print(ex)

# try:
#     dic1['last_name']
# except (KeyError, IndexError) as ex:
#     print("Error Occoured:",ex)

# Question 9

# file_path = input("enter the file name")
# try:
#     f = open(file_path, 'r')
#     for line in f:
#         try:
#             num = int(line.strip())
#             print("number:", num)
#         except ValueError as ex:
#             print("Error Occured:", ex)
# except FileNotFoundError as ex:
#     print("Error Occured", ex)
        

# Question 10
# file_path = input("Enter the fine name: ")
# try:
#     f = open(file_path, 'r')
#     f.write("abc")

# except IOError as ex:
#     print("Error Occoured:",ex)

# Question 11
# import sys
# x = int(input("Enter a number: "))

# try:
#     if x < 0:
#         raise ValueError("The value is less then 0")
#     print("the value is valid", x)
# except ValueError:
#     print("The value is less then 0")
#     sys.exit()

# Question 12
# try:
#     x = input("Enter a number:")
#     if not x.isdigit():
#         raise TypeError
#     x = int(x)
#     print(x)
# except TypeError as ex:
#     print("error occured", ex)

