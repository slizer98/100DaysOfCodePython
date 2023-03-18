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

#Write your code below this line 👇
print("Welcome to the Rock Paper Scissors Game")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
game_images = [rock, paper, scissors]
pc_choice = random.randint(0,2)
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == pc_choice:
    print(f"User choice: \n {game_images[user_choice]} ")
    print(f"PC choice: n {game_images[pc_choice]}")
    print("It's a draw!")
elif user_choice == 0 and pc_choice == 2 or user_choice == 1 and pc_choice == 0 or user_choice == 2 and pc_choice == 1:
  print(f"User choice: \n {game_images[user_choice]} ")
  print(f"PC choice: n {game_images[pc_choice]}")
  print("You win!")
else:
    print(f"User choice: \n {game_images[user_choice]} ")
    print(f"PC choice: \n {game_images[pc_choice]}")
    print("You lose!")