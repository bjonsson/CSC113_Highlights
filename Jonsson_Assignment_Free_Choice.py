# A good website to play this game is : http://www.hangman.no/. Select English as the language, then
# “Play game” and finally choose a category in the list and get started. Here, the number of chances
# you get is 10 (i.e. k = 10), for your project it will be only 6.
#
# Your task is to implement the Hangman game in Python.
import string
# Program Specifications:
# 1)	Output a brief description of the game of hangman and how to play
# 2)	Ask the user to enter the word or phrase that will be guessed (have a friend enter the phrase
#       for you if you want to be surprised)
# 3)	Output the appropriate number of dashes and spaces to represent the phrase (make sure it’s clear
#       how many letters are in each word and how many words there are)
# 4)	Continuously read guesses of a letter from the user and fill in the corresponding blanks if the
#       letter is in the word, otherwise report that the user has made an incorrect guess.
# 5)	Each turn you will display the phrase as dashes but with any already guessed letters filled in,
#       as well as which letters have been incorrectly guessed so far and how many guesses the user has remaining.
# 6)	Your program should allow the user to make a total of k=6 guesses.
# 7)	You MUST use at least 3 string methods or operators in a useful manner (several examples that I used
#       are given in the notes below).  If you wish to use lists in your project that is fine, as long as you meet
#       this requirement.


#Greeting
flag = True
while flag == True:
    menu = input("Hey... this is hangman. Are you alone right now? y/n ")

    flag2 = True
    while flag2 == True:
        if menu == "y":
            menuy = input("Do you want the computer to play hangman with you? ")

            if menuy == "y":
                # Start AI version of program
                AI_word = input("What word do you want our AI to guess? ")
                AI_word = AI_word.strip()

                # Make the board. Must be outside of scope of the while loop down below.
                board = []
                past_guesses = ""

                # Start game. We only want this initialized once, so keep it out of the while loop.
                # This is an adaptation of the two-player code below.
                for character in AI_word:
                    if character in string.ascii_letters:
                        board.append("_")
                    else:
                        board.append(character)

                # Envelop the guesses in a while loop for a count of 6.
                num_guesses = 6
                while num_guesses > 0:

                    print(f"You have {num_guesses} guesses left!")
                    # This if is strictly for aesthetic purposes.
                    if num_guesses == 6:
                        print()
                    else:
                        print(f"You have already guessed: {past_guesses}")

                    print(*board)

                    import random

                    letter_frequency = ["e","e","e","e","e","e","e","i","i","i","i","i","i","t","t","t","t","t","t",
                                        "s","s","s","s","a","a","a","a","n","n","n","n",
                                        "h","h","h","h","u","u","u","u","r","r","r","r","d","d","d","d","m","m","m",
                                        "m","w","w","w","g","g","g","v","v","v","l","l","l",
                                        "f","f","f","b","b","b","k","k","k","o","o","p","p","p","j","j","x","x","c",
                                        "c","z","z","y","q"]

                    guess = randomLetter = random.choice(letter_frequency)

                    print()
                    print()

                    # Append guess to leaderboard
                    past_guesses += guess

                    # Penalize incorrect guesses
                    if guess not in AI_word.lower():
                        num_guesses -= 1

                    # Replace underscore where letter is in phrase.
                    for i in range(len(AI_word)):
                        if AI_word[i].lower() == guess.lower():
                            board[i] = AI_word[i]

                    # The computer wins statement
                    if "_" not in board:
                        print('The computer won! Maybe you could try something harder next time!')
                        exit()

                # The computer loses statement
                print(f"The AI didn't guess '{AI_word}' this time! Maybe it will another time! Or, try an easier word!")
                exit()


            elif menuy == "n":
                menuyn = input("You have to play with the computer if you're alone! Unless you want to quit... "
                               "You don't want to quit, do you? (Enter q or n.) ")
                if menuyn == "q":
                    exit()
                elif menuyn == "n":
                    continue

        elif menu == "n":
            menun = input("Do you want to play hangman with another human? y/n ")
            if menun == "y":
                flag2 = False
                flag = False
                break
            elif menun == "n":
                menu = "y"
                continue

    else:
        flag = True

word_phrase = input("Hello, and welcome to a two-player version of hangman! \n"
      "Enter the word or phrase that someone else will guess.\n"
      "Punctuation and spaces are preserved. Only letters are guessable.\n"
      "Guesses are not case sensitive. ")

word_phrase = word_phrase.strip()

print("Adjust your window size so that the guesser can't peek at the word!")

# Make the board. Must be outside of scope of the while loop down below.
board = []
past_guesses = ""

# Start game. We only want this initialized once, so keep it out of the while loop.
for character in word_phrase:
    if character in string.ascii_letters:
        board.append("_")
    else:
        board.append(character)

# Envelop the guesses in a while loop for a count of 6.
num_guesses = 6
while num_guesses > 0 :

    # Give some space to hide the input
    print()
    print()
    print()
    print()
    print()

    # Separate string into characters
    # Preserve punctuation
    # Sprinkle the spaces in among the underscores.

    # Print leaderboard

    print(f"You have {num_guesses} guesses left!")
    # This if is strictly for aesthetic purposes.
    if num_guesses == 6:
        print()
    else:
        print(f"You have already guessed: {past_guesses}")

    print(*board)
    guess = input(f"Enter a letter you think might be in the phrase.\n")

    print()
    print()

    if guess.isalpha() == False:
        print("You can only guess a letter! We even had mercy on you and made it case insensitive. "
              "That will cost you a point!")

    # Append guess to leaderboard
    past_guesses += guess

    # Penalize incorrect guesses
    if guess.lower() not in word_phrase.lower():
        num_guesses -= 1

    # Replace underscore where letter is in phrase.
    for i in range(len(word_phrase)):
        if word_phrase[i].lower() == guess.lower():
            board[i] = word_phrase[i]


    # You win statement
    if "_" not in board:
        print(f'You won! The word was "{word_phrase}". Have you considered a career in "Wheel of Fortune" guest appearances?')
        exit()

# You lose statement
print(f'You lose! You were supposed to guess "{word_phrase}"!\nDid the second player give you something fair?')
exit()


    # Take a different path if the user wants the computer to guess the word/phrase

