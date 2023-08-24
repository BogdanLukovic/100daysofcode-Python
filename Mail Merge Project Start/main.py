#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("Input/Names/invited_names.txt") as name_list:
    names = name_list.read().split("\n")
print(names)
with open("Input/Letters/starting_letter.txt") as starting_letter:
    letter_contents = starting_letter.read()
    for name in names:
        new_text = letter_contents.replace("[name]", name)
        path = "Output/ReadyToSend/" + name.replace("\n", "")
        with open(path, mode="w") as a:
            a.write(new_text)
