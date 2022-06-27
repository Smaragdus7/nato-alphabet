import pandas

nato_dictionary = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dictionary = {row.letter: row.code for (index, row) in nato_dictionary.iterrows()}


def generate_phonetic():
    word = input("Type a word: ").upper()
    try:
        word_code = [new_dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters allowed.")
        generate_phonetic()
    else:
        print(word_code)


generate_phonetic()
