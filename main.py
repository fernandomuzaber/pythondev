import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

values = [rock, paper, scissors]
computer_election = random.randint(0, 2)
election = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if election == "0":
    print(values[0])
    print(values[computer_election])
    if computer_election == 0:
        print("It's a draw!")
    elif computer_election == 1:
        print("You lose!")
    else:
        print("You win!")
elif election == "1":
    print(values[1])
    print(values[computer_election])
    if computer_election == 0:
        print("You win!")
    elif computer_election == 1:
        print("It's a draw!")
    else:
        print("You lose!")
elif election == "2":
    print(scissors)
    print(values[computer_election])
    if computer_election == 0:
        print("You lose!")
    elif computer_election == 1:
        print("You win!")
    else:
        print("It's a draw!")
else:
    print("You typed an invalid number, you lose!")
