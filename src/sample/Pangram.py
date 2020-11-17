class IsPangram:
    
    def game(self, word):
        if type(word) is not str:
            raise Exception("Must_be_string")
        letters = "abcdefghijklmnopqrstuvwxyz"
        word = word.replace(" ", "")
        word = word.lower()
        for letter in letters:
            if letter not in word:
                return False
        return True


