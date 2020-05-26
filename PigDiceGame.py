#Pig Dice Game
#Version as of 02/21/2020 by Brad Campbell

import random
import time

dice = 0
current = 0
compTotal = 0
humanTotal = 0
compContinue = 1
humanContinue = 1
status = "y"

print("Welcome to Pig!\nYou will be playing against a computer.")

while(compTotal < 100 and humanTotal < 100):
  
  print("\033[1;32;40m\n") #sets text to Green
  print("############# USER TURN #############")
  print("\033[0;40;0m") #back to white
  while ((humanContinue > 0) and (current + humanTotal < 100) and (status == "y")):
    status = input("\nDo you want to roll? (input \"y\" or \"n\")")
    dice = random.randint(1, 6)
    if (dice == 1):
      current = 0
      humanContinue = 0
      print("You rolled a " + str(dice))
      print("\tSince you rolled a 1, your turn's total has been reset and it is the computer's turn.")
    else: 
      current += dice
      print("You rolled a " + str(dice) + ", so your current turn total is " + str(current))
  humanTotal += current
  print("Your game total is " + str(humanTotal))
  
  
  if (humanTotal > 100):
    compContinue = 0
  else:
    compContinue = 1
  current = 0

  print("\033[1;31;40m") #sets text to Red
  print("\n########### COMPUTER TURN ###########")
  print("\033[0;40;0m") #back to white
  while ((compContinue > 0) and ((current + compTotal) < 100)):
    time.sleep(3) #so user can follow computer moves
    dice = random.randint(1, 6)
    if (dice == 1):
      current = 0
      print("\nThe computer rolled a " + str(dice))
      print("\tSince it rolled a 1, its turn's total has been reset.")
    else:
      current += dice
      print("\nThe computer rolled a " + str(dice) + ", so its current turn totals " + str(current))
    if (dice != 1 and current < random.randint(12, 19)):
      print("\tThe computer will continue its turn.")
    else:
      print("The computer will stop its turn. It is your turn now.")
      compContinue = 0
      humanContinue = 1
  
  compTotal += current
  print("The computer's game total is " + str(compTotal))

  if (compTotal > 100):
    humanContinue = 0
  else:
    humanContinue = 1
  current = 0


#ran at the end of game
if (compTotal > 100):
  print("Unfortunately, the computer has won the game.")
  print("Better luck next time!")
else: 
  print("\033[1;43;40m\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
  print("Congratulations! You are victorious!")
#end here