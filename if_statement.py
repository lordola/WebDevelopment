# number= int(input("Insert a random number"))
# # % will print the remainder of a number. 5/2 is 1, 8/2 is 0
# if number % 2 ==0:
#     print("This is an even number")
# else:
#     print("This is an old number")

bill = 0
height = int(input("What is your height?"))
if height>120:
    print("You can ride!")

    age = int(input("What is your age?"))
    if age <12:
        bill = 5
        print("child ticket is $5!")
    elif age <=18:
        bill = 7
        print("Youth ticket is $7")
    else:
        bill = 12
        print("Adult ticket is $12")
    photo= input("Did you want photo? Y or N")
    if photo =="Y":
        bill+=3 # same way as bill = bill + 3
    print(f"Your final bill is ${bill}")


else:
    print("You cant ride")




# year = int(input("Which year do you want to check? "))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
#
# else:
#     print("Not leap year.")