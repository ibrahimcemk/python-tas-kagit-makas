import random

tas = '''stone:
    _______
---' ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''paper:
    _______
---' ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''scissors:
    _______
---' ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

human_selection = int(
  input(
    '''Rock, paper, scissors? Press "0" to select "rock", "1" to select "paper" and "2" to select "scissors"...\n'''''
  ))

if (human_selection > 2 or human_selection < 0):
  print("You entered an invalid value...")
else:
  print("Your selection...")
  print(game_images[human_selection])

  computer_selection = random.randint(0, 2)
  print("The computer is selecting...")
  print(game_images[computer_selection])

  if human_selection == 0 and computer_selection == 2:
    print("You won!")
  elif computer_selection == 0 and human_selection == 2:
    print("You lost!")
  elif computer_selection > human_selection:
    print("You lost")
  elif human_choice > computer_choice:
    print("You won!")
  elif computer_choice == human_choice:
    print("You tied!")