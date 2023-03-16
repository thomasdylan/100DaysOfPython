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

opp_choice = random.randint(0, 2)
player_choice = int(input("0 for Rock, 1 for Paper, 2 for Scissors "))

choice_list = [rock, paper, scissors]

if player_choice == opp_choice:
    print(choice_list[player_choice])
    print(f"Computer chose:\n {choice_list[opp_choice]}")
    print("It\'s a tie!")
elif player_choice == 0 and opp_choice == 1:
    print(choice_list[player_choice])
    print(f"Computer chose:\n {choice_list[opp_choice]}")
    print("You lose")
elif player_choice == 0 and opp_choice == 2:
    print(choice_list[player_choice])
    print(f"Computer chose:\n {choice_list[opp_choice]}")
    print("You Win!")
elif player_choice == 1 and opp_choice == 0:
    print(choice_list[player_choice])
    print(f"Computer chose:\n {choice_list[opp_choice]}")
    print("You Win!")
elif player_choice == 1 and opp_choice == 2:
    print(choice_list[player_choice])
    print(f"Computer chose:\n {choice_list[opp_choice]}")
    print("You lose")
elif player_choice == 2 and opp_choice == 0:
    print(choice_list[player_choice])
    print(f"Computer chose:\n {choice_list[opp_choice]}")
    print("You lose")
elif player_choice == 2 and opp_choice == 1:
    print(choice_list[player_choice])
    print(f"Computer chose:\n {choice_list[opp_choice]}")
    print("You Win!")
else:
    print("Did you make a valid selection?")
