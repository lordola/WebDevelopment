score = 0
height = 1.8
winning = True

# f-String is used to concatenate diff data types
print(f"your score is {score}, your height is {height}, you are winning is {winning}")

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
year_left = 90 - int(age)
# print(f"you have {year_left} years left")

month = 12 * int(age)
month2 = 90*12
month_left = (month2-month)

week = 52 * int(age)
week2 = 90*52
week_left = (week2-week)


day = 365*int(age)
day2 = 90*365
days_left = (day2 - day)
print(f"You have {days_left} days, {week_left} weeks, and {month_left} months left.")