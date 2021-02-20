# file1 = open("Input/Names/invited_names.txt")
# file2 = open("Input/Letters/starting_letter.txt")
#
# names = file1.readlines()
#
# for i in range(len(names)-1):
#     names[i] = names[i].strip('\n')
#
# text = file2.readlines()
#
# for i in range(len(names)-1):
#     if i==0:
#         text[0] = text[0].replace("[name]", f"{names[i]}")
#     else:
#         text[0] = text[0].replace(f"{names[i-1]}", f"{names[i]}")
#
#     with open(f"Output/ReadyToSend/To {names[i]}", mode="w") as file3:
#         for i in text:
#             file3.write(i)
#
# file1.close()
# file2.close()

PLACERHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()


with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACERHOLDER, stripped_name)
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
