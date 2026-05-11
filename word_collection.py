#Assignment #7- Story Teller
#WordCollection class
#Christian Nowak
#OOP


from word import Word

class WordCollection:

    def __init__(self):
        self._words = []

    # load words from a file
    @classmethod
    def from_file(cls, filepath):
        collection = cls()

        with open(filepath, "r") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split()

                if len(parts) != 2:
                    continue

                try:
                    word = Word(parts[0], parts[1])
                    collection.add(word)
                except ValueError:
                    continue

        return collection

    # add a word to the collection
    def add(self, word):
        if not isinstance(word, Word):
            raise TypeError("Only Word objects can be added")

        self._words.append(word)

    # filter words by part of speech
    def filter_by_pos(self, part_of_speech):
        new_collection = WordCollection()
        part_of_speech = part_of_speech.strip().lower()

        for word in self._words:
            if word.part_of_speech == part_of_speech:
                new_collection.add(word)

        return new_collection

    # return sorted words
    def sorted_words(self, reverse=False):
        new_collection = WordCollection()

        for word in sorted(self._words, reverse=reverse):
            new_collection.add(word)

        return new_collection

    # get amount of words
    def __len__(self):
        return len(self._words)

    def __getitem__(self, index):
        return self._words[index]

    # check if word is inside collection
    def __contains__(self, item):
        return item in self._words

  
    def __iter__(self):
        return iter(self._words)

    def __repr__(self):
        return f"WordCollection({len(self)} words)"