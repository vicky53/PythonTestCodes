def filter_list(l):
    number = []
    for num in l:
        if type(num) == int and num not in number:
            number.append(num)
    return number
