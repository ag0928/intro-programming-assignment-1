import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  f=1
  return choices

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    f=0
    return "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You win!"
    else:
      return "Paper covers rock! You lose."
  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock! You win!"
    else:
      return "scissors cut paper! You lose."
  elif player == "scissors":
    if computer == "paper":
      return "Scissors cut paper! You win!"
    else:
      return "Rock smashes scissors! You lose."
  
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
if f= 0:
  print()
print(result)
