import random

def hangman():
    word_list = ['python', 'java', 'ruby', 'javascript']
    random_word = random.choice(word_list)
    guessed_letters = []
    attempts = 10

    print("Let's play Hangman!")
    
    while attempts > 0:
        failed = 0
        for char in random_word:
            if char in guessed_letters:
                print(char, end="")
            else:
                print("_", end="")
                failed += 1
                
        if failed == 0:
            print("\nYou win!")
            print("The word was:", random_word)
            break

        guess = input("\n\nGuess a letter: ")
        guessed_letters.append(guess)

        if guess not in random_word:
            attempts -= 1
            print("\nIncorrect!")
            
            if attempts == 0:
                print("You lose! The word was:", random_word)

hangman()
