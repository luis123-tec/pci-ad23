import random
from hangman_words import word_list
from hangman_art import logo, stages

def start_game():
#Definir funciones para el inicio del juego (Sacar las palabras, determinar estado, vidas y score)
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
  #Mandar llamar la funcion para que se ejecute el incio del juego
    chosen_word, word_length, end_of_game, lives, max_score, display = start_game()

    while not end_of_game:
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

if __name__ == "__main__":
    play_hangman()

#Como hay tres modulos, cuando se este en main se va a ejectuar el juego
