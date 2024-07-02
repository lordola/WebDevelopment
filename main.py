import random

# random_integer = random.randint(2, 20)
# print(random_integer)
#
# random_float = random.random() * 5  # we multiply by 5 to get random 0-5
# print(random_float)
#
# number = random.randint(0, 1)
# if number == 0:
#   print("Tails")
# else:
#   print("Heads")

names = ["Ola", "Yemi", "Bola", "Lekan"]
#person_pay = input("Who will pay the bills?")
pay_by = random.choice(names)
print(f"{pay_by} will pay the bill.")
