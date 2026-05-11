"""
main.py - Week 7 Starter

Flow:
1. Ask for a path to a word file, load via WordCollection.from_file()
2. Print a count per part of speech
3. Show available story templates and let the user pick one
4. Ask how many sentences to generate
5. Generate and print the sentences
6. Ask if the user wants another story (loop if yes)
"""

from word_collection import WordCollection
from story_template import TEMPLATES


def main():
    # TODO: ask for the path; load the WordCollection
    # TODO: print summary (count per part of speech)
    # TODO: loop:
    #   - show templates with numbers
    #   - get user choice
    #   - ask how many sentences
    #   - call template.generate(words) for each
    #   - ask "Generate another story?" and break if not yes
    pass


if __name__ == "__main__":
    main()
