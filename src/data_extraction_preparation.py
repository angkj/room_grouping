import csv
import re


full_camper_lst = []  # entire list of campers, incl Females
gender_specific_lst = []  # list to contain either all Male or Female campers
camper_index = {}  # nric: index
reverse_camper_index = {}  # index: nric
grping_assignment = {}  # 'nric': 'group number'
rooming_request = []  # Data structure to contain the rooming requests based on the registration form


def file_extraction(gender_specific_campers_file, gender, full_campers_file):
    with open(full_campers_file, 'r', encoding='utf-8-sig') as file:
        csv_reader = csv.reader(file)
        for index, row in enumerate(csv_reader):
            full_camper_lst.append({
                'nric': row[1].upper(),
                'details': {
                    'full_name': row[0],
                    'gender': row[2]
                }
            })
            if row[2] == gender:
                gender_specific_lst.append(row[1].upper())

    with open(gender_specific_campers_file, 'r', encoding='utf-8-sig') as file:
        csv_reader = csv.reader(file)
        for index, row in enumerate(csv_reader):
            camper_index[row[0].upper()] = index
            reverse_camper_index[index] = row[0].upper()
            grping_assignment.setdefault(row[0], 0)
            rooming_request.append((row[0].upper(),
                                    '' if not re.match('^\w\d{7}\w$', row[1].upper()) else row[1].upper(),
                                    # Check to make sure that non valid NRICs are not added inside
                                    '' if not re.match('^\w\d{7}\w$', row[2].upper()) else row[2].upper()))


def get_gender_specific_list():
    return gender_specific_lst


def get_index_data_structure():
    return camper_index, reverse_camper_index, grping_assignment


def get_rooming_request():
    return rooming_request