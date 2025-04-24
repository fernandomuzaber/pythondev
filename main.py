print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input('''
You're at a cross road. Where do you want to go?
    Type "left" or "right"
\n''').lower()

if direction == "left":
    swim_or_wait = input('''
    You've come to a lake, there is an island in the middle of the lake.                        
    Do you want to swim or do you prefer to wait?
        Insert "swim" for swim or "wait" for wait
    \n''').lower()
    if swim_or_wait == "wait":
        door = input('''
        You arrive at the island unharmed. There is a house with 3 doors.
        You have to choose one door to enter:
            Please select into: red, yellow or blue
        \n''').lower()
        if door == "red":
            print('''
            It's a room full of fire.
            Burned by fire.
            Game Over
            \n''')
        elif door == "blue":
            print('''
            You enter a room of beasts.
            Game Over.
            \n''')
        elif door == "yellow":
            print('''
            Congratulations! You found the treasure.
            You win the game
            \n''')
        else:
            print('You choose a door that doesn\'t exist. Game over\n')

    else:
        print('''
        You were attacked by an angry trout.
        Game Over.
        ''')
else:
    print('''
    Fall into a hole.
    Game Over.
    ''')



