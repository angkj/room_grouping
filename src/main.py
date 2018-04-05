from data_extraction_preparation import file_extraction
from room_sorting import room_sorting

MALE_ROOMING_FILE = '../data/Legacy18_Rooming_Male.csv'
FULL_CAMPERS_LIST = '../data/Legacy18_name&nric.csv'

# Prompt for user's input
while True:
    gender = input('Male or Femal room sorting? [M/F]')

    if gender != 'M' and gender != 'F':
        print('Please enter "M" or "F"')
    else:
        break
    print()

file_extraction(MALE_ROOMING_FILE, 'M', FULL_CAMPERS_LIST)
room_sorting()
print('I m here')