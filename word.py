"""
word.py - Week 7 Starter

A Word holds text and a part-of-speech code.

Class attribute:
- VALID_PARTS = {"n", "v", "adj", "adv", "prep"}

Constructor stores text/POS lowercased and stripped.
Raises ValueError if part_of_speech is not in VALID_PARTS.

Operator overloading:
- __eq__: same text AND same POS
- __lt__: compares by POS first, then by text
- __gt__: reverse of __lt__
- __hash__: hash((self._text, self._part_of_speech))
- __repr__: Word('castle', 'n')
- __str__: just the text

For __eq__/__lt__/__gt__, return NotImplemented if `other` is not a Word.
"""


class Word:

    VALID_PARTS = {"n", "v", "adj", "adv", "prep"}

    def __init__(self, text, part_of_speech):
        # TODO: strip and lowercase text and part_of_speech
        # TODO: raise ValueError if POS not in VALID_PARTS
        # TODO: store as self._text and self._part_of_speech
        pass

    @property
    def text(self):
        return self._text

    @property
    def part_of_speech(self):
        return self._part_of_speech

    def __eq__(self, other):
        # TODO: if not isinstance(other, Word): return NotImplemented
        # TODO: equal if same text AND same POS
        pass

    def __lt__(self, other):
        # TODO: NotImplemented if not a Word
        # TODO: compare POS first, then text
        pass

    def __gt__(self, other):
        # TODO: reverse of __lt__
        pass

    def __hash__(self):
        # TODO: return hash((self._text, self._part_of_speech))
        pass

    def __repr__(self):
        # TODO: return f"Word({self._text!r}, {self._part_of_speech!r})"
        pass

    def __str__(self):
        # TODO: return just the text
        pass
