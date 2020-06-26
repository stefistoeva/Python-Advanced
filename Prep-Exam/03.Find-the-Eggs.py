def find_strongest_eggs(eggs, sub_list_count):
    sub_lists = []
    best_eggs = []
    for i in range(sub_list_count):
        sub_lists.append([eggs[index] for index in range(i, len(eggs), sub_list_count)])
    for sub_list in sub_lists:
        mid_element = sub_list[len(sub_list) // 2]
        left_element = sub_list[len(sub_list) // 2 - 1]
        right_element = sub_list[len(sub_list) // 2 + 1]
        if left_element < mid_element > right_element > left_element:
            best_eggs.append(mid_element)

    return best_eggs


test = ([-1, 7, 3, 15, 2, 12], 2)
print(find_strongest_eggs(*test))