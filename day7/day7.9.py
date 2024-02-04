import random
import hangmanArt
import hangmanWords

endgame = False
chosen_word = random.choice(hangmanWords.word_list)
lives = 6
print(chosen_word)
print(hangmanArt.logo)


display = []


for letter in chosen_word:
    display.append("_")


while not endgame:
    guess = input("guess a letter ").lower()
    if guess in display:
        print(f"you already guessed {guess} letter")
    for position in range(len(chosen_word)):
        char = chosen_word[position]
        if char == guess:
            display[position] = char

    if guess not in chosen_word:
        lives -= 1 
        if lives == 0:
            endgame = True
            print("you lose")

    print(f"your lives is {lives} left")
    print(f"{' '.join(display)}")

    if "_" not in display:
        endgame = True
        print("you win")

    print(hangmanArt.stages[lives])
