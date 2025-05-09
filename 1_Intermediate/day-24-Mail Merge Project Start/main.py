#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt", mode = "r") as letter:
    letter_data = letter.read()
    with open("Input/Names/invited_names.txt", mode = "r") as names:
        names_data = names.readlines()
        for name in names_data:
            name = name[:-1]
            with open(f"Output/ReadyToSend/letter_{name}.txt", mode = 'w') as output:
                letter_new = letter_data.replace("[name]", name)
                output = output.write(letter_new)