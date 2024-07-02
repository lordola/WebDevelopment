# greetings = "Good Morning"
# a = 4
#
# if a > 5:
#     print("the condition is met")
#     print("second line")
# else:
#     print("condition is not met")
# print("End of quotes")
#
# number = 23
# #guess = int(input(50))
# guess = 22
#
# if guess == number:
#     print('Congratulations, you guessed it')
#     print('(But you do not win any price!)')
# elif guess < number:
#     print('No, it is a little higher than that')
# else:
#     print('No, it is a little lower than that')
# print('Done')
#
# print(".....FOR LOOP.........")
# obj = [1, 2, 6, 8, 9]
# for i in obj:
#     print(i)
#     print(i*2)
# print('..................................')
#
# #sum of natural number
#
# # range(i, j)= i to j-1
# summation = 0
# for j in range(1, 6):
#     summation = summation + j
# print(summation)
#
# print('.................................')
# # multiple of i+2
# for m in range(1, 10, 2):
#     print(m)
#
# print("......WHILE LOOP...........")
# it = 4
# while it > 1:
#     print(it)
#     it = it-1
# print("While loop execution is done")
# it = 4
# while it > 1:
#     if it != 3:
#         print(it)
#     it = it-1
# print("......BREAK...........")
# it = 10
# while it > 1:
#     if it == 3:
#         break
#     print(it)
#     it = it-1
#
# print("......CONTINUE...........")
#
# it = 10
# while it > 1:
#     if it == 9:
#         it = it-1
#         continue
#     if it == 3:
#         break
#     print(it)
#     it = it-1
import random

# student_heights = input("Insert number of students\n").split()
#
# for n in range (0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
#
#
# total_student = sum(student_heights)
# total_height = len(student_heights)
# average = round(total_student/ total_height)
# print(average)
#
#
# # USING FOR LOOP INSTEAD OF SUM
# total_height = 0
# for height in student_heights:
#     total_height+=height
# print(total_height)
#
#
# #USING FOR LOOP INSTEAD OF LEN
#
# total_number= 0
# for number in student_heights:
#     total_number+=1
# print(total_number)
#
# average= round(total_height/total_number)
# print(average)


# PRINT OUT HIGHEST AND LOWEST NUMBER IN A STRING
#
# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
#
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
#
# print(f"The highest score in the class is: {highest_score}")
#
# total = 0
# for number in range(1, 101):
#     total+=number
# print(total)
#
#
# #For Loop with Lists
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#   print(fruit)
#   print(fruit + " Pie")
#
# # For-Loop with Range
#
# for number in range(1, 100):
#   print(number)
#
# for number in range(1, 101):
#   print(number)
#
# for number in range(1, 11, 3):
#   print(number)

# Calculating the sum of all the numbers from 1 to 100.
# total = 0
# for number in range(1, 101):
#   total += number
# print(total)
#
#
# # Calculating sum of even numbers
# total = 0
# for number in range(2, 101, 2):
#     total += number
# print(total)
#
#
# # or
# total2 = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total2 += number
# print(total2)

# IN RANGE(1,5)  sequence of integers from start (inclusive) to stop (exclusive) by step
# IN RANDINT(1,5) Return random integer in range [a, b], including both end points.

# print multiple of 3/5 and 3, 5
target = 100
for number in range(1, target+1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

random.randint()