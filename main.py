# Write your code here

class Hangman:
    print('\nH A N G M A N')
    quantity_attempt = 8
    input_list_of_letters = list()
    check_string = "qwertyuiopasdfghjklzxcvbnm"


    def __init__(self, the_word):
        self.the_word = the_word
        self.new_word = '-' * len(the_word)

    def print_new_word(self):
        print(f'\n{self.new_word}')

    def all_check(self):
        return self.the_word == self.new_word

    def check_quantity_attempt(self):
        return Hangman.quantity_attempt <= 0

    def check_the_word(self, type_letter):
        index_letter = -1
        number_of_letters = self.the_word.count(type_letter)

        if len(type_letter) != 1:
            print("\nYou should input a single letter")
            Hangman.input_list_of_letters.append(type_letter)

        elif type_letter not in Hangman.check_string:
            print("\nIt is not an ASCII lowercase letter")
            Hangman.input_list_of_letters.append(type_letter)

        elif type_letter in Hangman.input_list_of_letters:
            print("\nYou already typed this letter")

        elif type_letter not in self.the_word:
            print("\nNo such letter in the word")
            Hangman.quantity_attempt -= 1
            Hangman.input_list_of_letters.append(type_letter)

        elif number_of_letters > 0:
            for _ in range(number_of_letters):
                index_letter = self.the_word.find(type_letter, index_letter+1)
                self.new_word = "".join((self.new_word[:index_letter],
                                type_letter,
                                self.new_word[index_letter+1:]))
            Hangman.input_list_of_letters.append(type_letter)

        else:
            Hangman.input_list_of_letters.append(type_letter)
            print("\nчто-то не так, ошибка не обнаружена")
