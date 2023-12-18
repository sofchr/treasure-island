print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

move_1 = input("You arrive at a fork in the road. Would you like to start by going left or right? Type 'left' or 'right'\n").lower()
if move_1 == "left":
		move_2 = input("You come upon a lake. Do you decide to swim across to the island, or wait for a boat? Type 'swim' or 'wait'\n")

		if move_2 == "wait":
			move_3 = input("On the island, you find a strange wall with three doors. One is red, one is blue, and one is yellow. Which door do you decide to open? Type 'red', 'blue', or 'yellow'\n")
			if move_3 == "yellow": 
				print("You win the game! The treasure was behind the yellow door.")
			else:
				print("GAME OVER. The treasure was behind the yellow door. You are eaten by a dragon.")
		else:
			print("GAME OVER. A vengeful mermaid drags you to your watery tomb at the bottom of the lake.")		
else:
	print("GAME OVER. You walk directly into a ravine and perish.")