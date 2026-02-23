import random

def main():
    words = ["developer","hardware","software","algorithm","coding"]
    selected_word = random.choice(words)
    total_guesses = 6
    letters = set()
    
    print("Welcome to Hangman Game")
    
    while total_guesses > 0:
        guessed_word = ""
        for char in selected_word:
            if char in letters:
                guessed_word += char
            else:
                guessed_word += "_"
        print(f"\nWord: {guessed_word}")
        print(f"Attempts left: {total_guesses}")
        
        if guessed_word == selected_word:
            print("\nCongratulations, you won!")
            return
            
        guess = input("Guess a single letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
        if guess in letters:
            print("You already guessed that letter. Try again.")
            continue
        
        letters.add(guess)
        
        if guess in selected_word:
            print("Correct attempt")
        else:
            total_guesses -= 1
            print("Incorrect guess")        
        
    print(f"\nGame over! You ran out of attempts. The word was: {selected_word}")
    
    
main()
