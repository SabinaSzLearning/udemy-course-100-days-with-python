# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

import pandas as pd

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

with open('nato_phonetic_alphabet.csv', 'r') as file:
    df = pd.read_csv(file)

letters = {row.letter:row.code for (index, row) in df.iterrows()}
print(letters)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_list():
    user_input = input("Give me the name: ")
    try:
        answer = [letters[item.upper()] for item in user_input]
    except KeyError:
        print("Only letters, try again")
        generate_list()
    else:
        print(answer)

generate_list()
