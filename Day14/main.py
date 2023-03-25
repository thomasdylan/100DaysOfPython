# Imports
import random
import game_data

# Functions


def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


# Global Variables
SCORE = 0
GAME_SHOULD_CONTINUE = True

# Logic
while GAME_SHOULD_CONTINUE:
    account_a = random.choice(game_data.data)
    account_b = random.choice(game_data.data)
    if account_a == account_b:
        account_b = random.choice(game_data.data)

    print(f"Compare A: {format_data(account_a)}.")
    print("vs")
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more foloower? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        SCORE += 1
        print("Correct!")
    else:
        GAME_SHOULD_CONTINUE = False
        print(f"Wrong answer. Final Score: {SCORE}")
