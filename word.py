#Assignment #7- Story Teller
#Word class
#Christian Nowak
#OOP


class Word:

    VALID_PARTS = {"n", "v", "adj", "adv", "prep"}

    def __init__(self, text, part_of_speech):
        self._text = text.strip().lower()
        self._part_of_speech = part_of_speech.strip().lower()

        if self._part_of_speech not in Word.VALID_PARTS:
            raise ValueError("Invalid part of speech")

    # word text
    @property
    def text(self):
        return self._text

    # part of speech
    @property
    def part_of_speech(self):
        return self._part_of_speech

    # check if two words are equal
    def __eq__(self, other):
        if not isinstance(other, Word):
            return NotImplemented

        return self._text == other._text and self._part_of_speech == other._part_of_speech

    # less than comparison
    def __lt__(self, other):
        if not isinstance(other, Word):
            return NotImplemented

        if self._part_of_speech == other._part_of_speech:
            return self._text < other._text

        return self._part_of_speech < other._part_of_speech

    # greater than comparison
    def __gt__(self, other):
        if not isinstance(other, Word):
            return NotImplemented

        return other < self

    # allows word to be used in sets
    def __hash__(self):
        return hash((self._text, self._part_of_speech))

    def __repr__(self):
        return f"Word('{self._text}', '{self._part_of_speech}')"

    # print the word
    def __str__(self):
        return self._text
    