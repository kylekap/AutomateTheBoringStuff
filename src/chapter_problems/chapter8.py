import pyperclip


def pyperclip_example(text=""):
    if text == "":
        text = pyperclip.paste()  # Get the text off the clipboard.

    alt_text = ""  # This string holds the alternating case.
    for pos_id, character in enumerate(text):
        # Go through each character and add it to alt_text:
        if pos_id % 2 == 0:
            alt_text += character.upper()
        else:
            alt_text += character.lower()
    pyperclip.copy(alt_text)  # Put the result on the clipboard.
    print(alt_text)  # Print the result on the screen too.


def bulletpointadder(text=""):
    if text == "":
        text = pyperclip.paste()
    text_lines = text.split(r"\n")
    for line in range(len(text_lines)):
        text_lines[line] = "* " + text_lines[line]
    final_str = "\n".join(text_lines)
    pyperclip.copy(final_str)
    return final_str


def piglatin_translator(message):
    vowels = ("a", "e", "i", "o", "u", "y")

    pig_latin_translation = []

    for word in message.split():
        working_word = word
        prefix = ""
        while len(working_word) > 0 and not working_word[0].isalpha():
            prefix += working_word[0]
            working_word = working_word[1:]
        if len(working_word) == 0:
            pig_latin_translation.append(prefix)
            continue
        suffix = ""
        while not working_word[-1].isalpha():
            suffix = working_word[-1] + suffix
            working_word = working_word[:-1]

        # Remember if the word was in uppercase or title case:
        was_upper = working_word.isupper()
        was_title = working_word.istitle()

        working_word = working_word.lower()  # Make the word lowercase for translation.

        # Separate the consonants at the start of this word:
        prefix_consonants = ""
        while len(working_word) > 0 and working_word[0] not in vowels:
            prefix_consonants += working_word[0]
            working_word = working_word[1:]

        # Add the pig latin ending to the word:
        if prefix_consonants != "":
            working_word += prefix_consonants + "ay"
        else:
            working_word += "yay"

        # Set the word back to uppercase or title case:
        if was_upper:
            working_word = working_word.upper()
        if was_title:
            working_word = working_word.title()

        # Add the non-letters back to the start or end of the word.
        pig_latin_translation.append(prefix + working_word + suffix)

    # Join all the words back together into a single string:
    return " ".join(pig_latin_translation)


def main():
    bulletpointadder()
    pyperclip_example()
    print(piglatin_translator("My name is AL SWEIGART and I am 4,000 years old."))


if __name__ == "__main__":
    """[summary]"""
    main()


"For example, if I copied this sentence to the clipboard and then called paste(), it would look like this:"
"Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars"


"""
1.What are escape sequences?

2.What do the \n and \t escape sequences represent?
    \n is newline, \t is tab
3.How can you put a \\ backslash character in a string?
    make it a raw string r""
4.The string value "Howl's Moving Castle" is a valid string. Why isn't it a problem that the single quote character in the word Howl"s isn't escaped?
    Because the wrapping string characters are ", so ' is allowed in the string
5.If you don't want to put \n in your string, how can you write a string with newlines in it?
    using multiline string, three " in a row
6.What do the following expressions evaluate to?

"Hello, world!"[1]
    "e"
"Hello, world!"[0:5]
    "Hello"
"Hello, world!"[:5]
    "Hello"
"Hello, world!"[3:]
    "lo, world!"
7.What do the following expressions evaluate to?

"Hello".upper()
    "HELLO"
"Hello".upper().isupper()
    TRUE
"Hello".upper().lower()
    hello

8.What do the following expressions evaluate to?

"Remember, remember, the fifth of November.".split()
    ["Remember,", "remember,", "the", "fifth", "of", "November."]
"-".join("There can be only one.".split())
    "There-can-be-only-one."
9.What string methods can you use to right-justify, left-justify, and center a string?
    rjust, ljust, center
10.How can you trim whitespace characters from the beginning or end of a string?
    .strip()
"""  # noqa: W605
