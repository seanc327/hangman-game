#word input
while True:
    secret_word = str(input('Please enter a word to be guessed\nthat does not contain ? or white space: ')).lower()
    if " " in secret_word:
        str(input('Please enter a word to be guessed\nthat does not contain ? or white space: ')).lower()
    elif "?" in secret_word:
        str(input('Please enter a word to be guessed\nthat does not contain ? or white space: ')).lower()
    else:
        break


letter_guessed = []
chance = 7
print(secret_word)
print('?' * len(secret_word))

while chance > 0:
# input
    print('\nSo far you have guessed:', ','.join(sorted(map(str, letter_guessed))))
    while True:
        try:
            guess = input('Please enter your next guess: ')
        except EOFError:
            continue
        if len(guess) > 1: # whole word guess error
            print("You can only guess a single character.")
            continue
        if len(guess) == 0 or len(guess) == " ": # empty word guess error
            print("You must enter a guess.")
            continue
        if guess in letter_guessed: # words already been guessed before
            print('You already guessed the character:', guess)
            continue
        else:
            break


# guesses
    if guess in secret_word:
        print('')
    else:
        chance -= 1

#display
    if chance == 6:
        print(' |')
    if chance == 5:
        print(' |')
        print(' 0')
    if chance == 4:
        print(' |')
        print(' 0')
        print(' |')
    if chance == 3:
        print(' |')
        print(' 0')
        print('/|')
    if chance == 2:
        print(' |')
        print(' 0')
        print('/|\\')
    if chance == 1:
        print(' |')
        print(' 0')
        print('/|\\')
        print('/')

    letter_guessed += guess
    wrong_letter = 0
    for letter in secret_word:
        if letter in letter_guessed:
            print(f'{letter}', end='')
        else:
            print('?', end='')
            wrong_letter += 1

    if wrong_letter == 0:
        print('\nYou correctly guessed the secret word:', secret_word)
        break

else:
    print(' |')
    print(' 0')
    print('/|\\')
    print('/ \\')
    print('\nYou failed to guess the secret word:', secret_word)