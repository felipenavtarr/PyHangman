from random import choice


LIVES_INITIAL = 8
words = ('python', 'java', 'kotlin', 'javascript')


def check_input(txt):
    if len(txt) != 1:
        print("You should input a single letter")
        return False
    if not txt.isalpha() or txt.isupper():
        print("Please enter a lowercase English letter")
        return False
    return True


def game():
    solution = choice(words)
    lives = LIVES_INITIAL
    tried = set()
    while lives > 0:
        print("\n" + "".join([letter if letter in tried else '-' for letter in solution]))
        guess = input("Input a letter: ")
        if not check_input(guess):
            continue

        if guess in tried:
            print("You've already guessed this letter")
        else:
            tried.add(guess)
            if set(solution).issubset(tried):  # victory condition
                break
            if guess not in solution:
                lives -= 1
                print("That letter doesn't appear in the word")

    if lives:
        print('You guessed the word!\nYou survived!''')
    else:
        print("You lost!")
    print()


print(*"HANGMAN")
while True:
    option = input('Type "play" to play the game, "exit" to quit: ')
    if option == 'play':
        game()
    elif option == 'exit':
        break
    else:
        continue
