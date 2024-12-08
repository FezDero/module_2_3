my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list) and my_list[index] >= 0:
    count = my_list[index]
    index = index + 1
    if count > 0:
        print (count)
    elif count == 0:
        continue
    elif count < 0:
        break