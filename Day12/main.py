# Imports
import random

# Global Variables
RANDOM_NUMBER = random.randint(1, 100)

# Functions


def set_player_lives():
    """Lets user decided difficulty and adjust amount of lives the player has for the game."""
    difficulty = input("Select your difficulty: Easy or Hard: ").lower()
    if difficulty == "easy":
        player_lives = 10
    elif difficulty == "hard":
        player_lives = 5

    return player_lives


def check_guess(player_guess):
    """Checks the players guess against the winning number."""
    if player_guess == RANDOM_NUMBER:
        print(f"You win! The number was {RANDOM_NUMBER}")
        return False
    elif player_guess > RANDOM_NUMBER:
        print("Too high\n")
        return True
    elif player_guess < RANDOM_NUMBER:
        print("Too low\n")
        return True


def play_game():
    """Starts the game logic."""
    print("Welcome to the number guessing game!\n ")
    game_active = True
    player_lives = set_player_lives()
    while game_active:
        if player_lives > 0:
            print(f"Lives left: {player_lives}")
        elif player_lives == 0:
            print(f"LAST GUESS")
        guess = int(input("Guess the number between 0 & 100: "))
        game_active = check_guess(player_guess=guess)
        if game_active and player_lives == 0:
            print(f"You lose. The number was {RANDOM_NUMBER}")
            game_active = False
        elif game_active and player_lives > 0:
            player_lives -= 1


play_game()
