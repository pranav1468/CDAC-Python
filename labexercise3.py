#question1

sum = 0
for i in range(0,20):
    if i % 2 != 0:
        sum = sum + i

print("Sum of odd numbers from 1 to 20 is:", sum)

#question2

sum = 0
for i in range(101,200):
    sum = sum + i

print("Sum of numbers from 100 to 200 is:", sum)

#question3
sum = 0

for i in range(21):
    if i % 2 == 0:
        sum = sum + i**2

print("Sum of even numbers from 1 to 20 is:", sum)

#question4

print("list of operations")
print("1. Append a number")
print("2. Insert a number at a position")
print("3. Append multiple numbers")
print("4. Update a number at a position")
print("5. Delete a number at a position")
print("6. Remove a number")
print("7. Sort the list")
print("8. Sort the list in descending order")
print("9. Print the list")
print("10. Exit")

my_list = [int(i) for i in input("Enter numbers: ").split(",")]

while True:
    choice = int(input("Enter your choice(1-10):"))

    if choice == 1:
        num = int(input("Enter a number: "))
        my_list.append(num)
        print("Updated list:", my_list)
        
    elif choice == 2:
        num = int(input("Enter a number: "))
        position = int(input("Enter position: "))
        my_list.insert(position, num)
        print("Updated list:", my_list)

    elif choice == 3:
        nums = [int(i) for i in input("Enter numbers: ").split(",")]
        my_list.append(nums)
        print("Updated list:", my_list)

    elif choice == 4:
        num = int(input("Enter a number: "))
        position = int(input("Enter position: "))
        my_list[position] = num
        print("Updated list:", my_list)

    elif choice == 5:
        position = int(input("Enter position: "))
        del my_list[position]
        print("Updated list:", my_list)

    elif choice == 6:
        num = int(input("Enter a number: "))
        my_list.remove(num)
        print("Updated list:", my_list)
        
    elif choice == 7:
        my_list.sort()
        print("Sorted list:", my_list)

    elif choice == 8:
        my_list.sort(reverse=True)
        print("Sorted list in descending order:", my_list)

    elif choice == 9:
        print(my_list)

    elif choice == 10:
        exit()


#question 5

for i in range(65, 91):
    p = chr(i)
    print(i, "=", p,)

#question 6

for i in range(48, 58):
    p = chr(i)
    print(i, "=", p,)

#question7

for i in range(97, 123):
    p = chr(i)
    print(i, "=", p,)

#question8

L1 = [100, 200, 300, 400, 500]
L1.reverse()
print(L1)

#question9

List1 = [1, 2, 3, 4, 5, 6, 7]
l1 = [i**2 for i in List1]
print(l1)

#question10
string = input("enter a string: ")

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

for i in string:
    if i in "a" :
        count1 += 1
    if i in "e" :
        count2 += 1
    if i in "i" :
        count3 += 1
    if i in "o" :
        count4 += 1
    if i in "u" :
        count5 += 1

print("a =", count1)
print("e =", count2)
print("i =", count3)
print("o =", count4)
print("u =", count5)

#or

string = input("Enter a string: ")

a_count = string.count("a")
e_count = string.count("e")
i_count = string.count("i")
o_count = string.count("o")
u_count = string.count("u")

print("a =", a_count)
print("e =", e_count)
print("i =", i_count)
print("o =", o_count)
print("u =", u_count)

#question11
string = input("Enter a string: ")
string1 = string.replace(" ","")

string2 = sorted(string1)
print("Sorted words:", ''.join(string2)) 

#question 12

import string

str1 = input("Enter a string:")
str2 = ""
punctuations = string.punctuation

for i in str1:
    if i not in punctuations:
        str2 += i

print(str2)

#question 13

for i in range(1,4):  
    for j in range(i, 0, -1):  
        print(j, end="")
    print()  

#question 14

for i in range (1,7):
    for j in range(0,i):
        print("*", end=" ")
    print()


#question 15

for i in range(0,6):
    for j in range(0,i):
        print("*", end=" ")
    print()
for i in range(0,6):
    for j in range(i,4):
        print("*", end=" ")
    print()

#question 16

for row in range(1, 11):
    if row < 10:
        print(end=" ")
    print(row, end=" |  ")
    for col in range(1, 11):
        product = row * col
        if (product) < 10:
            print(end=" ")
        print(product, end="  ")
    print() 
