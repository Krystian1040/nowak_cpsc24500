"""
story_template.py - Week 7 Starter

A StoryTemplate holds a sentence pattern and can generate sentences from a WordCollection.

Pattern format: a list of strings.
- Literal words are plain strings: "The"
- Placeholders use braces: "{n}", "{v}", "{adj}", "{adv}", "{prep}"

Example:
    ["The", "{adj}", "{n}", "{v}", "{adv}"]

generate(words) walks through the pattern, replaces each placeholder with a random
word of that part of speech from the WordCollection, and returns the sentence
(capitalized, ending with a period).
"""

import random


class StoryTemplate:

    def __init__(self, name, pattern):
        # TODO: store name and pattern
        pass

    @property
    def name(self):
        return self._name

    @property
    def pattern(self):
        return self._pattern

    def generate(self, words):
        # TODO: walk through self._pattern
        #   - if token starts with "{" and ends with "}", extract the POS
        #     and pick a random Word of that POS from `words`
        #   - otherwise keep the token as-is
        # TODO: join with spaces, capitalize, add a period at the end
        pass


# TODO: define at least 3 templates here
TEMPLATES = [
    # StoryTemplate("Adventure", ["The", "{adj}", "{n}", "{v}", "{adv}", "{prep}", "the", "{adj}", "{n}"]),
    # StoryTemplate("Mystery", [...]),
    # StoryTemplate("Simple", [...]),
]
