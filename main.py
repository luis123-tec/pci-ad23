import random
from hangman_words import word_list
from hangman_art import logo, stages
#Import all the necesarry modules for the game to start

def start_game():
    #Define the functions for the start of the game (word, len, lives, display)
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6
    max_score = 0

    display = ["_" for _ in range(word_length)]

    print(logo)
    print(f'Pssst, the solution is {chosen_word}.')
    return chosen_word, word_length, end_of_game, lives, max_score, display

def play_hangman():
    #Call in the function and the variables to start the game
    chosen_word, word_length, end_of_game, lives, max_score, display = start_game()
    #This while true, and not end of game, make it so you can restart the game if you so chose, and make it so that if you lose all lives, then game is false losing automatically
    while True:
        while not end_of_game:
            #Game logic
            guess = input("Guess a letter: ").lower()

            if guess in display:
                print(f"You've already guessed {guess}")

            for position in range(word_length):
                letter = chosen_word[position]

                if letter == guess:
                    display[position] = letter

            if guess not in chosen_word:
                print(f"You guessed {guess}, that's not in the word. You lose a life.")
                lives -= 1
                if lives == 0:
                    end_of_game = True
                    print("You lose.")

            print(" ".join(display))

            if "_" not in display:
                end_of_game = True
                print("You win.")
                score = max_score + lives * 100  # Incrementa el score
                print(f"Your score is {score}")

            print(stages[lives])

        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
      #Input to see if you want to play again or not

        if restart == "no":
            print("Goodbye")
            break
        elif restart == "yes":
            print("Let's play again!")
            chosen_word, word_length, end_of_game, lives, max_score, display = start_game()
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

if __name__ == "__main__":
    play_hangman()

#Since there are 3 modules, by being in main the game starts.
