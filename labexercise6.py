# Question 1
# from datetime import datetime, timedelta
# date = datetime.now()
# new_date = date - timedelta(days=7)
# print(new_date)

# Question 2
# from datetime import datetime, timedelta
# date = datetime(2024, 3, 22, 10, 0, 0)
# new_date = date + timedelta(days=7, hours=12)
# print(new_date)

# Question 3
# from datetime import datetime, timedelta
# date = datetime.now()
# for i in range(10):
#     date = date + timedelta(weeks=2)
#     print(date.strftime("%Y-%m-%d"))

# Question 4
# from datetime import datetime
# date_1 = datetime(2020, 2, 25)
# date_2 = datetime(2020, 9, 17)
# delta = date_2 - date_1
# print(abs(delta.days, "days"))

# Question 5
# from datetime import datetime
# date = datetime.now()
# print(date.strftime("%Y-%m-%d %H:%M:%S"))
# print(date.year)
# print(date.strftime("%B"))
# print(date.strftime("%a"))
# print(date.strftime("%d"))
# print(date.strftime("%A"))


# Question 6
# class Triangle():
#     n = 3
#     def __init__(self, angle1, angle2, angle3):
#         self.a = angle1
#         self.b = angle2
#         self.c = angle3

#     def check_angles(self):
#         if self.a + self.b + self.c == 180:
#             return True
#         else:
#             return False
        
# my_triangle = Triangle(90,30,60)
# print(my_triangle.n)
# print(my_triangle.check_angles())

# Question 7
# class Songs():
#     def __init__ (self, lyrics):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for line in range(0, len(self.lyrics)):
#             print(self.lyrics[line])
# happy_bday = Songs(["May god bless you,",
# "Have a sunshine on you,",
# "Happy Birthday to you !"])
# happy_bday.sing_me_a_song()

# Question 8
# class Lunch():
#     def __init__(self, menu):
#         self.menu = menu

#     def menu_price(self):
#         if self.menu == "menu 1":
#             return "your choice:, self.menu, Price: 12.00"
#         elif self.menu == "menu 2":
#             return "your choice:, self.menu, Price: 13.40"
#         else:
#             return "Error in menu"

# paul=Lunch("menu 1")
# print(paul.menu_price())

# Question 9
# class string():
#     def get_string(self, s):
#         self.s = s
#     def print_string(self):
#         print(self.s.upper())

# my_string = string()
# my_string.get_string("hello")
# my_string.print_string()

# Question 10
# class rectangle():
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    
#     def area(self):
#         return self.length * self.width
    
#     def perimeter(self):
#         return 2 * (self.length + self.width)
    
#     def exit(self):
#         print("Exit")
#         exit()
    
# length = int(input("Enter length of a Rectangle: "))
# width = int(input("Enter width of a Rectangle: "))
# print("1. Area")
# print("2. Perimeter")
# print("3. Exit")
# choice = int(input("Enter choice: "))
# rect = rectangle(length, width)


# while True:
#     if choice == 1:
#         print("Area of Rectangle is: ", rect.area())
#         choice = int(input("Enter choice: "))
#     elif choice == 2:
#         print("Perimeter of Rectangle is: ", rect.perimeter())
#         choice = int(input("Enter choice: "))
#     elif choice == 3:
#         rect.exit()
#     else:
#         print("Invalid Choice")
#         choice = int(input("Enter choice: "))
