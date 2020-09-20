def list_operation(x, y, n):
    return [value for value in range(x, y+1) if value % n == 0]


def change_list_value(L = [12, 13]):
    L[0] = 56


L2 = [14, 15]
change_list_value(L2)
print(L2)


