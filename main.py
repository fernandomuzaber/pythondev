# import random
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# values = [rock, paper, scissors]
# computer_election = random.randint(0, 2)
# election = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
# if election == "0":
#     print(values[0])
#     print(values[computer_election])
#     if computer_election == 0:
#         print("It's a draw!")
#     elif computer_election == 1:
#         print("You lose!")
#     else:
#         print("You win!")
# elif election == "1":
#     print(values[1])
#     print(values[computer_election])
#     if computer_election == 0:
#         print("You win!")
#     elif computer_election == 1:
#         print("It's a draw!")
#     else:
#         print("You lose!")
# elif election == "2":
#     print(scissors)
#     print(values[computer_election])
#     if computer_election == 0:
#         print("You lose!")
#     elif computer_election == 1:
#         print("You win!")
#     else:
#         print("It's a draw!")
# else:
#     print("You typed an invalid number, you lose!")

# Her solution

# import random
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# game_images = [rock, paper, scissors]
# #0 : rock
# #1 : paper
# #2 : scissors

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# if user_choice >= 0 and user_choice <= 2:
#     print(game_images[user_choice])
# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])

# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number, you lose!")
# elif user_choice == 0 and computer_choice == 2:
#     print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#     print("You lose!")
# elif computer_choice > user_choice:
#     print("You lose!")
# elif user_choice > computer_choice:
#     print("You win!")
# elif computer_choice == user_choice:
#     print("It's a draw!")


# Python loops

# List
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))

# total_exam_score = sum(student_scores)
# print(total_exam_score)

# Without python method
# sum = 0
# for score in student_scores:
#     sum += score
# print(sum)

# max_score = max(student_scores)
# print(max_score)

# Without max method

max = 0
for score in student_scores:
    if score > max:
        max = score

print(max)

min = min(student_scores)
print(min)

min = 100
for score in student_scores:
    if score < min:
        min = score
print(min)
