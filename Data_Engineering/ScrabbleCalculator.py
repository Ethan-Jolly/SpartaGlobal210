class ScrabbleCalculator:
    def __init__(self):
        self.dictionary = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

    def get_word_score(self, word):
        score = 0
        """ My version 1 """
        # for values in self.dictionary.items():
        #     for letter in word:
        #         if values[0] == letter.lower():
        #             score += values[1]
        """ Better version taken from Andre"""
        for letter in word.lower():
            score += self.dictionary[letter]
        return score


def main():
    sc = ScrabbleCalculator()
    print(sc.get_word_score('Hello'))


if __name__ == '__main__':
    main()
