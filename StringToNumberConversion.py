import math
import re


def str_to_int(num):
    j = 0
    number = 0
    for i in num[::-1]:
        if i == "-":
            number = number * -1
        else:
            digit_value = ord(i) - ord('0')
            number = number + (digit_value * 10 ** j)
            j += 1
    return number


def correct_signs(txt):
    result = False
    lst = txt.strip().split()
    for i in range(0, len(lst)):
        if lst[i] == "<":
            if int(lst[i - 1]) < int(lst[i + 1]):
                result = True
            else:
                return False
        elif lst[i] == ">":
            if int(lst[i - 1]) > int(lst[i + 1]):
                result = True
            else:
                return False
    return result


def square_areas_difference(r):
    square2 = (2 * r) * (2 * r)
    square1 = square2 // 2
    return square2 - square1


def century_from_year(num):
    number = num // 100
    if num % 100 == 0:
        return number
    else:
        return number + 1


def validate_card(num):
    if len(str(num)) < 13 or len(str(num)) > 19:
        return False
    last_digit = num % 10
    reverse_num = str(num)[:-1][::-1]
    sum_card = 0
    for i in range(0, len(reverse_num)):
        if (i + 1) % 2 == 1:
            val = int(reverse_num[i]) * 2
            count = 0
            for j in str(val):
                count = count + int(j)
            sum_card = sum_card + count
        else:
            sum_card = sum_card + int(reverse_num[i])
    if last_digit == (10 - (sum_card % 10)):
        return True
    else:
        return False


def sqrt_num(num):
    print(math.sqrt(num))


# lst = ["bad cookie", "good cookie", "bad cookie", "good cookie", "good cookie"]
# pattern = "*.bad.*"
# print(len(re.findall(pattern, ", ".join(lst))))

# print(str_to_int("-123"))
# print(correct_signs("3 < 7 < 11"))
# print(correct_signs("13 > 44 > 33 > 1"))
# print(correct_signs("1 < 2 < 6 < 9 > 3"))
# print(correct_signs("4 > 3 > 2 > 1"))
# print(correct_signs("5 < 7 > 1"))
# print(correct_signs("5 > 7 > 1"))
# print(correct_signs("9 < 9"))
# print(square_areas_difference(5))
# print(square_areas_difference(6))
# print(square_areas_difference(7))
# print(square_areas_difference(17))
# print(century_from_year(2005))
# print(century_from_year(2020))
# print(century_from_year(200))
# print(century_from_year(1700))
# print(century_from_year(1705))
print(validate_card(4400663686628309))
# print(validate_card(79927398713))
# print(validate_card(45391424543493400011))
# sqrt_num(1)
