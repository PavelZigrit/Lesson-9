def lines_count(file_name):
    with open(file_name, encoding='utf-8') as f:
        str_count = len(f.readlines())
    return str_count


def get_data(file_name):
    with open(file_name, encoding='utf-8') as f:
        data = f.read()
    return data


def files_merge(file_name1, file_name2, file_name3,  merge_file):
    str_count1 = lines_count(file_name1)
    str_count2 = lines_count(file_name2)
    str_count3 = lines_count(file_name3)
    if str_count1 == min(str_count1, str_count2, str_count3):
        min_file = file_name1
        min_str = str_count1
        if str_count2 == max(str_count1, str_count2, str_count3):
            max_file = file_name2
            max_str = str_count2
            mid_file = file_name3
            mid_str = str_count3
        else:
            max_file = file_name3
            max_str = str_count3
            mid_file = file_name2
            mid_str = str_count2
    elif str_count1 == max(str_count1, str_count2, str_count3):
        max_file = file_name1
        max_str = str_count1
        if str_count2 == min(str_count1, str_count2, str_count3):
            min_file = file_name2
            min_str = str_count2
            mid_file = file_name3
            mid_str = str_count3
        else:
            min_file = file_name3
            min_str = str_count3
            mid_file = file_name2
            mid_str = str_count2
    elif str_count2 == min(str_count1, str_count2, str_count3):
        min_file = file_name2
        min_str = str_count2
        max_file = file_name3
        max_str = str_count3
        mid_file = file_name1
        mid_str = str_count1
    else:
        min_file = file_name3
        min_str = str_count3
        max_file = file_name2
        max_str = str_count2
        mid_file = file_name1
        mid_str = str_count1
    data_min = get_data(min_file)
    data_mid = get_data(mid_file)
    data_max = get_data(max_file)

    with open(merge_file, "w", encoding='utf-8') as f:
        f.write(min_file + '\n')
        f.write(str(min_str) + '\n')
        f.write(data_min + '\n')
        f.write(mid_file + '\n')
        f.write(str(mid_str) + '\n')
        f.write(data_mid + '\n')
        f.write(max_file + '\n')
        f.write(str(max_str) + '\n')
        f.write(data_max + '\n')

    return get_data(merge_file)


# print(files_merge("1.txt", "2.txt", "3.txt", "Merge.txt"))

