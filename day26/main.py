import pandas as pd

raw_data = pd.read_csv("nato_phonetic_alphabet.csv")

nato_phonetic = {row.letter: row.code for (index, row) in raw_data.iterrows()}
print(nato_phonetic)

user_input = input("Enter your name: ").upper()

phonetic_result = [nato_phonetic.get(letter) for letter in user_input]
print(phonetic_result)
