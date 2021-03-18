def lines_count(file_name):
    with open(file_name, encoding='utf-8') as f:
        str_count = len(f.readlines())
    return str_count


def get_data(file_name):
    with open(file_name, encoding='utf-8') as f:
        data = f.read()
    return data


def files_merge(files_list, merge_file):
    files_dict = {}
    files_len_list = []
    for file in files_list:
        file_len = lines_count(file)
        files_dict[file] = file_len
        files_len_list.append(file_len)
    while len(files_dict) != 0:
        for file, str_count in files_dict.copy().items():
            if str_count == min(files_len_list):
                data = get_data(file)
                with open(merge_file, "a", encoding='utf-8') as f:
                    f.write(file + '\n')
                    f.write(str(str_count) + '\n')
                    f.write(data + '\n')
                files_dict.pop(file)
                files_len_list.remove(str_count)
    return get_data(merge_file)


print(files_merge(["1.txt", "2.txt", "3.txt"], "Merge.txt"))

