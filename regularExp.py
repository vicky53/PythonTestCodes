import re
lst = ["bad cookie", "good cookie", "bad cookie", "good cookie", "good cookie"]
print(", ".join(lst))
pattern = '(?<!good )cookie'
print(len(re.findall(pattern, ", ".join(lst))))
num_list = [4, 3, 2, 6, 7, 8,1]
num_list.sort()
print(num_list)