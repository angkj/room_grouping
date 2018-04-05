from collections import deque
from pprint import pprint as pp

from data_extraction_preparation import get_gender_specific_list, get_index_data_structure, get_rooming_request


rooming_request = get_rooming_request()
unregistered_campers = []  # list of unregistered campers, for us to remove from the grping_assignment
error_flags = []  # contains a list of warnings to flag out
final_room_assignment = {}  # Array containing all those in the same group to be grouped together


def room_sorting():
    counter = 1
    camper_index, reverse_camper_index, grping_assignment = get_index_data_structure()
    gender_specific_lst = get_gender_specific_list()
    camper_matrix = [[0] * len(gender_specific_lst) for x in range(len(gender_specific_lst))]

    for roomie in rooming_request:
        participant_index = camper_index[roomie[0]]

        try:
            if roomie[1] != '':
                if roomie[1] in gender_specific_lst:
                    roomie_1_index = camper_index[roomie[1]]
                    camper_matrix[participant_index][roomie_1_index] = 1
                    camper_matrix[roomie_1_index][participant_index] = 1
                else:
                    unregistered_campers.append(roomie[1])
                    error_flags.append("{}'s roommate: {} is not registered for camp."
                                       .format(reverse_camper_index[participant_index], roomie[1]))

            if roomie[2] != '':
                if roomie[2] in gender_specific_lst:
                    roomie_2_index = camper_index[roomie[2]]
                    camper_matrix[participant_index][roomie_2_index] = 1
                    camper_matrix[roomie_2_index][participant_index] = 1
                else:
                    unregistered_campers.append(roomie[2])
                    error_flags.append("{}'s roommate: {} is not registered for camp."
                                       .format(reverse_camper_index[participant_index], roomie[2]))
        except KeyError as ke:
            print()

    for camper in gender_specific_lst:
        counter += 1
        if grping_assignment[camper] != 0:
            counter -= 1
            return
        queue = deque([])
        queue.append(camper)

        while queue:
            node = queue.popleft()
            grping_assignment[node] = counter
            for col_index, cell in enumerate(camper_matrix[camper_index[node]]):
                if cell == 0:
                    continue
                if grping_assignment[reverse_camper_index[col_index]] != 0:
                    continue
                queue.append(reverse_camper_index[col_index])

    for camper, grp_number in grping_assignment.items():
        final_room_assignment.setdefault(grp_number, []).append(camper)

    pp(final_room_assignment)