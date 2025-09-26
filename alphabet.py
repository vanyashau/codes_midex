import string
class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = 0

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)
        EngAlphabet.__letters_num = len(self.letters)

    def if_en_letter(self, letter):
        if letter in self.letters:
            return True
        return False

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        return "Hello, World!"


eng_alphabet = EngAlphabet()

eng_alphabet.print()

print(eng_alphabet.letters_num())

print(eng_alphabet.if_en_letter('F'))

print(eng_alphabet.if_en_letter('Щ'))

print(EngAlphabet.example())    