# track lives
# compare guess
# reprint hangman status after each guess, so we can print the correct icon

def charposition(string, char):
    pos = []
    for n in range(len(string)):
        if string[n] == char:
            pos.append(n)
    return pos

lives = 6
win = False

print("\033[H\033[J", end="")
print("Hangman Game:")
print("*****************")
word = input("Type a word to hang the man: ")
hiddenWord = list('_'*len(word))
print("\033[H\033[J", end="")

print("__________________________")
print("!Game Begin!")

while lives != 0:
    print(f"Lives remaining {lives}:")
    
    if lives == 6:
        print("  ------")
        print("  |    |")
        print("       |")
        print("       |")
        print("       |")
        print(" -------")
    
    elif lives == 5:
        print("  ------")
        print("  |    |")
        print("  O    |")
        print("       |")
        print("       |")
        print(" -------")
        
    elif lives == 4:
        print("  ------")
        print("  |    |")
        print("  O    |")
        print("  |    |")
        print("       |")
        print(" -------")
        
    elif lives == 3:
        print("  ------")
        print("  |    |")
        print("  O    |")
        print(" /|    |")
        print("       |")
        print(" -------")
    
    elif lives == 2:
        print("  ------")
        print("  |    |")
        print("  O    |")
        print(" /|\   |")
        print("       |")
        print(" -------")
        
    elif lives == 1:
        print("  ------")
        print("  |    |")
        print("  O    |")
        print(" /|\   |")
        print(" /     |")
        print(" -------")

    print(*hiddenWord)
    print("\n--------------------")
    
    guess = input("Guess a letter: ")
    
    if guess in word:
        print("Good Guess!")
        for i in range(len(hiddenWord)):
            if word[i] == guess:
                hiddenWord[i] = guess
                
        if ''.join(hiddenWord) == word:
            win = True
            print(f"win {win}")
            break
    else:
        print("Oof Wrong Guess!")
        lives = lives - 1
    
if win != True:
    print("\033[H\033[J", end="")
    print("*****************")
    print("  ------")
    print("  |    |")
    print("  O    |")
    print(" /|\   |")
    print(" / \   |")
    print(" -------")
    print(f"You loose, the word was: {word}")   
    print("*****************")
else:
    print("\033[H\033[J", end="")
    print("*****************")
    print("YOU WON, No man was hanged today!")
    print("*****************")
    
