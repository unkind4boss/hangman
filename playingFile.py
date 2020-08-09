# Write your code here

from AMOgameWithClass import Hangman

while True:
    game = input('\nType "play" to play the game, "exit" to quit:')

    if game == "exit":
        exit()
    elif game == "play":
        the_word = "pythonnpy"
        playing = Hangman(the_word)
        playing.print_new_word()

        while True:
            type_letter = input('Input a letter:')
            playing.check_the_word(type_letter)

            if playing.all_check():
                playing.print_new_word()
                print("You guessed the word!\nYou survived!")
                exit()

            if playing.check_quantity_attempt():
                print('\nпопытки закончились вы проиграли')
                exit()

            playing.print_new_word()
