import pandas

nato_dictionary = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dictionary = {row.letter: row.code for (index, row) in nato_dictionary.iterrows()}

word = input("Type a word: ").upper()

word_code = [new_dictionary[letter] for letter in word]
print(word_code)

