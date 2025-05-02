# print(r'''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
# |                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")

# direction = input('''
# You're at a cross road. Where do you want to go?
#     Type "left" or "right"
# \n''').lower()

# if direction == "left":
#     swim_or_wait = input('''
#     You've come to a lake, there is an island in the middle of the lake.                        
#     Do you want to swim or do you prefer to wait?
#         Insert "swim" for swim or "wait" for wait
#     \n''').lower()
#     if swim_or_wait == "wait":
#         door = input('''
#         You arrive at the island unharmed. There is a house with 3 doors.
#         You have to choose one door to enter:
#             Please select into: red, yellow or blue
#         \n''').lower()
#         if door == "red":
#             print('''
#             It's a room full of fire.
#             Burned by fire.
#             Game Over
#             \n''')
#         elif door == "blue":
#             print('''
#             You enter a room of beasts.
#             Game Over.
#             \n''')
#         elif door == "yellow":
#             print('''
#             Congratulations! You found the treasure.
#             You win the game
#             \n''')
#         else:
#             print('You choose a door that doesn\'t exist. Game over\n')

#     else:
#         print('''
#         You were attacked by an angry trout.
#         Game Over.
#         ''')
# else:
#     print('''
#     Fall into a hole.
#     Game Over.
#     ''')

# Mersenne Twister

# import sys
# sys.set_int_max_str_digits(10000)  # o más, según lo que necesites

# print(2**19937)

# import random
# import my_module

# # from a to B
# rand_num = random.randint(1,10)

# print(rand_num)

# # random not includes 1
# rand_num_0_to_1 = random.random() * 5

# print(rand_num_0_to_1)

# #uniform includes the b
# random_float = random.uniform(1, 10)

# print(random_float)

# #Importo el modulo creado y uso la variable creada en el modulo
# print(my_module.my_favourite_number)


import random
import my_module

# from a to B
# rand_num = random.randint(1,10)

# print(rand_num)

#  It generates a random number between 0 and 1, but 1 is not included
# rand_num_0_to_1 = random.random() * 5

# print(rand_num_0_to_1)

#uniform includes the b
# random_float = random.uniform(1, 10)

# print(random_float)
# print(my_module.my_favourite_number)

# Head or tails

# if random.random() * 10 > 5:
#     print("Heads")
# else:
#     print("Tails")

# Her solution

random_heads_or_tails = random.randint(0,1)

if(random_heads_or_tails == 0):
    print("Heads")
else:
    print("Tails")