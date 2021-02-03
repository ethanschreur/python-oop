from random import choice
"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    ...
    def __init__(self, path):
        file = open(path)
        self.words = self.get_words_list(file)
        print(f'{len(self.words)} words read')

    def get_words_list(self, file):
        return [words.strip() for words in file]

    def random(self):
        num_words = len(self.words)
        random_index = choice([num for num in range(num_words)])
        return self.words[random_index]
    
class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        super().__init__(path)
    def get_words_list(self, file):
        return [w.strip() for w in file
                if w.strip() != '' and not w.startswith("#")]

# I thought you had to initialize the super but it looks like you don't
# need to in order to access the parent class' attributes

# with and without the init function that calls the parent class it does the same thing
# so should i include it to make it clear what is happenign or should i not include it?