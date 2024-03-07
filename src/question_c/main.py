from question_c import get_random_number

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thanks for playing! Goodbye.")
            break

def play_game():
    print("Welcome to the Guessing Game!")
    random_number = get_random_number()

    while True:
        guess = int(input("Guess the number between 1 and 5: "))

        if guess == random_number:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            print("Sorry, that's not the correct number. Try again.")

if __name__ == "__main__":
    main()
