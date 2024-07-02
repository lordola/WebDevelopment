# student_heights = [180, 124, 165, 173, 189, 169, 146]
#
# number = 0
# for heights in student_heights:
#     number+=heights
# print(number)
#
# lenght = len(student_heights)
# print(lenght)
#
# average = number/lenght
# print(average)

student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

heights_score = 0
for score in student_scores:
    if score > heights_score:
        heights_score=score
print(heights_score)

