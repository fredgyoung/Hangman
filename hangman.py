import string


class Hangman():

    def __init__(self):
        self.unused_letters = None
        self.word = None
        self.game_loop()

    def game_loop(self):

        play_again = True

        while play_again:
            self.reset_game()
            self.choose_word()

            solved = False

            while not solved:
                self.show_hangman()
                self.show_unused_letters()

                solved = True

            play_again = False

    def reset_game(self):
        self.unused_letters = list(string.ascii_lowercase)

    def choose_word(self):
        self.word = "horse"

    def show_unused_letters(self):
        print("Unused Letters:", end=" ")
        for letter in self.unused_letters:
            print(letter, end=" ")

    def gather_input(self):
        pass

    def show_hangman(self):
        print("\t", end=" ")
        for letter in self.word:
            print('_', end=" ")
        print()


if __name__ == '__main__':

    game = Hangman()
