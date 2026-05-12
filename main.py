#Assignment #7- Story Teller
#Main class
#Christian Nowak
#OOP

from word_collection import WordCollection
from story_template import TEMPLATES
from word import Word


# print count for each part of speech
def print_summary(words):
    print(f"Loaded {len(words)} words:")

    for part in sorted(Word.VALID_PARTS):
        count = len(words.filter_by_pos(part))
        print(f"  {part}: {count}")


# let user choose a story template
def choose_template():
    print()
    print("Available story styles:")

    for i in range(len(TEMPLATES)):
        print(f"{i + 1}. {TEMPLATES[i].name}")

    while True:
        try:
            choice = int(input("Choose a style: "))

            if choice >= 1 and choice <= len(TEMPLATES):
                return TEMPLATES[choice - 1]

            print("Invalid choice. Try again.")

        except ValueError:
            print("Please enter a number.")


# get sentence amount from user
def get_sentence_count():
    while True:
        try:
            count = int(input("How many sentences? "))

            if count > 0:
                return count

            print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a valid number.")


def main():
    print("=" * 40)
    print("Welcome to StoryTeller")
    print("=" * 40)

    filepath = input("Enter path to word file: ").strip()

    try:
        words = WordCollection.from_file(filepath)
    except FileNotFoundError:
        print("File not found.")
        return

    print_summary(words)

    again = "yes"

    while again == "yes":
        template = choose_template()
        count = get_sentence_count()

        print()
        print(f"--- {template.name} Story ---")

        for i in range(count):
            print(template.generate(words))

        print()
        again = input("Generate another story? (yes/no): ").strip().lower()

    print("Thank you for using StoryTeller!")


if __name__ == "__main__":
    main()
