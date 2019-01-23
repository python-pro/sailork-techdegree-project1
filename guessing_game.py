import random


def start_game(scores):
    print(f"""
Hello and welcome to my Number Guessing Game! You will be prompted to guess
a number between 1 and 10. I'll let you know if you need to go higher or
lower, and then when you guess correctly you can play again!
""")
    number = random.randint(1,10)
    guess_count = 1

    try:
        print(f"The current high score is {min(scores)} guesses, try to beat it!")
    except ValueError:
        print("No current high score, try to get the best!")

    while True:
        try:
            guess = input("So, whats your guess?  ")
            if not guess.isdigit():
                raise ValueError("Please enter an integer between 1 and 10.")
            guess = int(guess)
            if guess < 1 or guess > 10:
                raise ValueError("Please enter an intgeer between 1 and 10.")
        except ValueError as err:
            print(f"Whoops! {err}")
        else:
            if guess < number:
                print(f"It's higher! You've guessed {guess_count} times.")
                guess_count += 1
                continue
            elif int(guess) > number:
                print(f"It's lower! You've guessed {guess_count} times.")
                guess_count += 1
                continue
            elif int(guess) == number:
                print("Nice job! You got it!")
                scores.append(guess_count)
                print(f"""
Your score was {guess_count}. The high score is {min(scores)}.""")
                play_again = input("Want to play again? (Y/N)  ")
                if play_again.lower() == 'y':
                    start_game(scores)
                else:
                    print("Thanks for playing!")
                    exit()

if __name__ == '__main__':
    scores = []
    start_game(scores)
