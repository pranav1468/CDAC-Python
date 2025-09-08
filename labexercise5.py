# #Question 1
# f= open(r"C:\Users\prana\OneDrive\Desktop\tut python\modules\text.txt","r")
# print(f.read())
# f.close()

# #Question 2
# import mymod
# file = input("Enter the filename with path: ")
# print("Number of lines in the file:", mymod.count_lines(file))
# print("Number of characters in the file:", mymod.count_characters(file))
# print("Lines and characters:", mymod.test(file))

# #Question 3
# import mymod 
# file = input("Enter the filename with path: ")
# print("Number of lines in the file:", mymod.count_lines(file))
# print("Number of characters in the file:", mymod.count_characters(file))
# print("Lines and characters:", mymod.test(file))

# import mymod as mm
# file = input("Enter the filename with path: ")
# print("Number of lines in the file:", mm.count_lines(file))
# print("Number of characters in the file:", mm.count_characters(file))
# print("Lines and characters:", mm.test(file))

# from mymod import count_lines, count_characters, test
# file = input("Enter the filename with path: ")
# print("Number of lines in the file:", count_lines(file))
# print("Number of characters in the file:", count_characters(file))
# print("Lines and characters:", test(file))

# from mymod import *
# file = input("Enter the filename with path: ")
# print("Number of lines in the file:", count_lines(file))
# print("Number of characters in the file:", count_characters(file))  
# print("Lines and characters:", test(file))


# Question 4

# import mymod
# if __name__ == "__main__":
#     file = input("Enter the filename with path: ")
#     print("Number of lines in the file:", mymod.count_lines(file))
#     print("Number of characters in the file:", mymod.count_characters(file))
#     print("Lines and characters:", mymod.test(file))
# else:
#     print("mymod module has been imported.")

# Question 5

# import mymod
# file = input("Enter the filename with path: ")
# print("Number of lines in the file:", mymod.count_lines(file))
# print("Number of characters in the file:", mymod.count_characters(file))
# print("Lines and characters:", mymod.test(file))

# from mymod import count_lines, count_characters, test
# file = input("Enter the filename with path: ")
# print("Number of lines in the file:", count_lines(file))
# print("Number of characters in the file:", count_characters(file))
# print("Lines and characters:", test(file))


# Question 6
# import mypkg.mymod 
# file = input("Enter the filename with path: ")
# print("Number of lines in the file:", mypkg.mymod.count_lines(file))
# print("Number of characters in the file:", mypkg.mymod.count_characters(file))
# print("Lines and characters:", mypkg.mymod.test(file))



# Question 7
# file_path = input("Enter the filename with path: ")
# n = int(input("Enter the number of lines to read: "))
# f= open(file_path, 'r')
# for i in range(n):
#     line = f.readline()
#     print(line, end='')

# f.close()

# Question 8 Python program to append text to a file and display the text.
# file_path = input("Enter the filename with path: ") 
# text_to_append = input("Enter the text to append: ")
# f = open(file_path, 'a')
# f.write(text_to_append + '\n')
# f.close()

# f = open(file_path, 'r')
# content = f.read()
# f.close()
# print("Content of the file after appending:")
# print(content)

# Question 9 Python program to read a file line by line and store it into a list.
# file_path = input("Enter the filename with path: ")
# f = open(file_path, 'r')
# lines = f.readlines()
# f.close()

# print(lines)

# Question 10 file_path = input("Enter the filename with path: ")
# file_path = input("Enter the filename with path: ")
# f = open(file_path, 'r')
# lines = f.readlines()
# lines=lines[::-1]
# f.close()

# lines = ''.join(lines)
# print(lines)

# Question 11 Python program to write a list content to a file.
# list_to_write = input("Enter the list elements separated by commas: ").split(',')
# file_path = input("Enter the filename with path: ")

# list_to_write = ' '.join(list_to_write)

# f = open(file_path, 'w')
# f.write(list_to_write)
# f.close()

# f = open(file_path, 'r')
# content = f.read()
# f.close()

# print("List has been written to the file.",content)

# Question 12 
# from mymod import *

# file_path = input("Enter the filename with path: ")
# print("Number of lines in the file:", count_lines(file_path))
# print("Number of characters in the file:", count_characters(file_path))
# print("Number of words in the file:", count_word(file_path))
# print(f"lines: {count_lines(file_path)}, characters: {count_characters(file_path)}, words: {count_word(file_path)}")

# question 13
# file_path = input("Enter the filename with path: ")

# f = open(file_path, 'a')
# while True:
#     line = input("Enter a line (or 'End' to stop): ")
#     if line == 'End':  
#         break
#     f.write(line + '\n')  
# f.close() 


# f = open(file_path, 'r')
# lines = f.readlines()  
# f.close()  

# for line in lines:
#     if line.strip() and line[0].isupper(): 
#         print(line, end='') 

# Questin 14
# import pickle

# k = open("data.pkl", "wb")
# n = int(input("Enter the number of records: "))
# for i in range(n):
#     data = []
#     Item_No = int(input("Item No: "))
#     Item_Name = input("Item Name: ")
#     Qty = int(input("Quantity: "))
#     Price = float(input("Price per item: "))
#     amount = Qty * Price
#     data = [Item_No, Item_Name, Qty, Price, amount]
#     pickle.dump(data, k)
# k.close()

# k = open("data.pkl", "rb")

# while True:
#         try:
#             item = pickle.load(k)
#             print(f"Item No: {data[0]}")
#             print(f"Item Name: {data[1]}")
#             print(f"Quantity: {data[2]}")
#             print(f"Price per item: {data[3]}")
#             print(f"Amount: {data[4]}")
#         except EOFError:
#             break
# k.close()









