# Hangman game

# libraries required
import random
import sys


class Hangman:
    def __int__(self, fname, lname):
        self._fname = fname
        self._lname = lname
        self.__word = None
        self._meaning = None

    def display(self):
        return f"Hello, {self._fname} {self._lname}"

    def word_and_meaning(self):
        words_meaning = [
            {"foxglove": "a tall Eurasian plant with erect spikes of pinkish-purple (or white) flowers shaped like the "
                         "fingers of gloves. It is a source of the drug digitalis"},
            {"rapture": "A feeling of extreme happiness"},
            {"crap": "nonsense"}
        ]
        return words_meaning

    def generation(self):
        words_meaning = Hangman.word_and_meaning(self)
        given = random.choice(words_meaning)
        for word, meaning in given.items():
            self.__word = word
            self._meaning = meaning

    def give_the_user_word(self):
        code = "I quit"
        vowels = ['a', 'e', 'i', 'o', 'u']
        words = self.__word
        _list_for_guessess = ['h', 'a', 'n', 'g', 'm', 'a', 'n']
        alphabets = []
        realword = [word for word in words]
        final_word = []
        for word in range(len(words)):
            if words[word] in vowels:
                __w = words[word]
                print(__w, end="")
                final_word.append(__w)

            else:
                print("_", end="")
                final_word.append("_")
        print()
        print(f"meaning of the word given: {self._meaning}")

        points = 7

        while True:
            print(f"Points left: {points}")
            guess = input("guess: ")

            for alphabets in final_word:
                print(alphabets, end="")
            print()

            if guess in realword:
                a = realword.index(guess)
                final_word[a] = guess

            else:
                print("Wrong")
                points -= 1

            print(final_word)

            if "_" not in final_word and points <= 0:
                print("You won")
                sys.exit()

            elif points == 0:
                print("You Lost")
                print(f"The word was {self.__word}")
                sys.exit()

            else:
                continue

        


def main():
    hangman = Hangman()
    hangman.generation()
    hangman.give_the_user_word()


if __name__ == '__main__':
    main()
