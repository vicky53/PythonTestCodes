def binary_search(a_list, search_number):
    result = False
    list_length = len(a_list)
    low_length = 0
    high_length = list_length - 1
    if high_length < low_length:
        return False
    middle_length = (high_length - low_length) // 2
    if search_number == a_list[middle_length]:
        return True
    elif search_number < a_list[middle_length]:
        result = binary_search(a_list[:middle_length], search_number)
    else:
        result = binary_search(a_list[middle_length + 1:], search_number)
    return result


num_list = [1, 4, 7, 12, 25, 39, 55, 63]
print(binary_search(num_list, 12))
