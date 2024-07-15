student_heights = input("Insert number of students\n").split()

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
# USING FOR LOOP INSTEAD OF SUM
total_height = 0
for height in student_heights:
    total_height+=height
print(total_height)


#USING FOR LOOP INSTEAD OF LEN

total_number = 0
for number in student_heights:
    total_number += 1
print(total_number)

average= round(total_height/total_number)
print(average)


#PRINT OUT HIGHEST AND LOWEST NUMBER IN A STRING
