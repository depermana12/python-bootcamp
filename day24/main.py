with open("Input/Names/invited_names.txt") as names:
    recipient = names.readlines()

with open("Input/Letters/starting_letter.txt", "r") as default_letter:
    msg = default_letter.read()
    for name in recipient:
        print_letter = msg.replace("[name]", name.strip())
        with open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt", "w") as data:
            data.write(print_letter)
