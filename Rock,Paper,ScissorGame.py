import random

options=['Rock','Paper','Scissor']
ComputerScore=0 
PlayerScore=0
NumberOfRounds=0
gameOn=True

while NumberOfRounds<5:
  ComputerOption=random.choice(options)
  PlayerOption=input("Enter Rock/ Paper/ Scissor :").title()
  print(f"Computer option :{ComputerOption}")
  print(f" Player :{PlayerOption}")
  NumberOfRounds += 1
  if ComputerOption==PlayerOption:
    print('Tie')
  elif (ComputerOption=='Rock' and PlayerOption == 'Scissor') or (ComputerOption=='Scissor' and PlayerOption=='Paper') or (ComputerOption=='Paper' and ComputerOption=='Rock'):
    print("Computer wins")
    ComputerScore += 1
  elif (PlayerOption=='Rock' and ComputerOption == 'Scissor') or (PlayerOption=='Scissor' and ComputerOption=='Paper') or (PlayerOption=='Paper' and ComputerOption=='Rock'):
    print(f"Player wins")
    PlayerScore += 1
  else:
    print("Choose a valid option to play this game.") 
  print(f"Round No: {NumberOfRounds}")
  print("------ Score Board ------")
  print("")
  print(f" Player {PlayerScore} | Computer: {ComputerScore}")
  print("")
  if NumberOfRounds==5:
    gameOn=False
    break
if PlayerScore==ComputerScore:
  print("Draw!!")
elif PlayerScore>ComputerScore:
  print(f"Congrats , You won the game!!")
else:
  print(f"Oops Computer won the game!! Better luck next time !")
  
Player = int(input('''Game Start....
                   1 Yes
                   2 NO| Exit''')) 
