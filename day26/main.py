import pandas as pd

raw_data = pd.read_csv("nato_phonetic_alphabet.csv")

nato_phonetic = {row.letter: row.code for (index, row) in raw_data.iterrows()}
print(nato_phonetic)


def recursive_phonetic():
    user_input = input("Enter your name: ").upper()
    try:
        # if using get() method, the error return none
        phonetic_result = [nato_phonetic[letter] for letter in user_input]
    except KeyError:
        print("Error, please input only a letter")
        # invoke the function itself
        recursive_phonetic()
    else:
        print(phonetic_result)


recursive_phonetic()
