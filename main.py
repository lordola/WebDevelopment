# print("Welcome to the Band Name Generator")
#
# name = input("What is your name\n")
# city = input("What is your city\n")
# print(len(name))
# print("Your brand name is " + name + " " + city)
# print("Hello world\nHello World\nHello world")
#
#
# # input will be executed first, followed by print statement
# print("Hello " + input("Whats is your name"))
print("Thank you for choosing Python Pizza Deliveries")
size = input("What size did you want? S , M, or L\n")
add_pepperoni= input("Did you want pepperoni? Y or N\n")
extra_cheese= input("Did you want extra cheese? Y or N\n")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size =="S":
        bill +=2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is {bill}")
