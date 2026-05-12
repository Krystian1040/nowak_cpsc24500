#Assignment #7- Story Teller
#Story Template class
#Christian Nowak
#OOP

import random


class StoryTemplate:

    def __init__(self, name, pattern):
        self._name = name
        self._pattern = pattern

    # template name
    @property
    def name(self):
        return self._name

    # sentence pattern
    @property
    def pattern(self):
        return self._pattern

    # generate one sentence
    def generate(self, words):
        sentence_words = []

        for token in self._pattern:

            # check if token is a placeholder
            if token.startswith("{") and token.endswith("}"):
                part_of_speech = token[1:-1]
                matching_words = words.filter_by_pos(part_of_speech)

                if len(matching_words) == 0:
                    raise ValueError("No words found for part of speech")

                random_word = random.choice(list(matching_words))
                sentence_words.append(str(random_word))

            else:
                sentence_words.append(token)

        sentence = " ".join(sentence_words)
        sentence = sentence.capitalize() + "."

        return sentence


# story templates
TEMPLATES = [
    StoryTemplate("Adventure", [
        "The", "{adj}", "{n}", "{v}", "{adv}",
        "{prep}", "the", "{adj}", "{n}"
    ]),

    StoryTemplate("Mystery", [
        "A", "{adj}", "{n}", "{adv}", "{v}",
        "while", "the", "{n}", "{v}",
        "{prep}", "the", "{n}"
    ]),

    StoryTemplate("Simple", [
        "The", "{adj}", "{n}", "{v}", "{adv}"
    ])
]


