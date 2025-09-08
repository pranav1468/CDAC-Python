# # question1
# l1 = [1, 2, 3, 4, 5]
# print(sum(l1))

# # question2
# l1 = [1, 2, 3, 4, 5]
# s = max(l1)
# print(s)

# # question3
# l1 = [1, 2, 3, 4, 5]
# s = min(l1)
# print(s)

# #question 4
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0], color_list[-1])

# #question 5
# str1 = input("Enter a string: ")
# if str1.endswith("ing"):
#     str2 = str1 + ("ly")
#     print(str2)
# else:
#     str2 = str1 + ("ing")
#     print(str2)

# #question6
# marks = input("Enter marks: ")
# if int(marks) >= 60:
#      print("First Division")
# elif int(marks) >= 50 and int(marks) <= 5956:
#     print("Second Division")
# elif int(marks) >= 40 and int(marks) <= 49:
#     print("Third Division")
# elif int(marks) < 40:
#     print("Fail")


# #question 7
# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
# num3 = input("Enter third number: ")

# num4 = max(int(num1), int(num2), int(num3))
# print("The largest number is:", num4)

# #question8
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

# #question9
# str1 = input("Enter a string: ")
# if str1 == str1[::-1]:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# # #question10
# l1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sl = ["h", "i", "j"]

# l1[2][1][2].extend(sl)
# print(l1)

#question 11
list1 = [5, 10, 15, 20, 25, 50, 20]

list1[list1.index(20)] = 200
print(list1)

#question 12
list1 = [1, 2, 3, 4, 5]

str1 = list1[3:5]
str2 = list1[0:3]

list2 = str1 + str2
print(list2)