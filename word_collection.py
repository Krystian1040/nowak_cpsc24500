"""
word_collection.py - Week 7 Starter

Holds a list of Word objects and supports iteration, indexing, filtering, and sorting.

Operator overloading:
- __len__, __getitem__, __contains__, __iter__, __repr__

Methods:
- add(word): TypeError if not a Word
- filter_by_pos(pos): returns a NEW WordCollection
- sorted_words(reverse=False): returns a NEW WordCollection sorted via Word.__lt__
- from_file(filepath): @classmethod that reads "word pos" lines and returns a WordCollection
"""

from word import Word


class WordCollection:

    def __init__(self):
        # TODO: empty internal list
        pass

    @classmethod
    def from_file(cls, filepath):
        # TODO: create a new WordCollection
        # TODO: open the file, read each line
        #   - strip; skip blank lines
        #   - split into text and pos; skip lines that don't parse
        #   - create a Word and add it (catch ValueError for invalid POS)
        # TODO: return the collection
        pass

    def add(self, word):
        # TODO: raise TypeError if not a Word
        # TODO: append to internal list
        pass

    def filter_by_pos(self, part_of_speech):
        # TODO: build a new WordCollection containing only matching words
        pass

    def sorted_words(self, reverse=False):
        # TODO: build a new WordCollection from sorted(self._words, reverse=reverse)
        # No `key` parameter -- relies on Word.__lt__
        pass

    def __len__(self):
        # TODO
        pass

    def __getitem__(self, index):
        # TODO
        pass

    def __contains__(self, item):
        # TODO
        pass

    def __iter__(self):
        # TODO: return iter(self._words)
        pass

    def __repr__(self):
        # TODO: return f"WordCollection({len(self)} words)"
        pass
