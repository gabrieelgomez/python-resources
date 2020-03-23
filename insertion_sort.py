def insertion_sort(list):

    for index in range(1, len(list)):
        current_value = list[index]
        current_position = index

        while current_position > 0 and list[current_position - 1] > current_value:
            list[current_position] = list[current_position - 1]
            current_position -= 1

        list[current_position] = current_value
