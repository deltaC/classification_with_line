from designations import Subject


def read_text(file_name):
    arr = list()
    f = open(f"{file_name}", "r")
    for line in f:
        arr.append(line)
    f.close()
    return arr


def generate_array_from_list(arr):
    res_arr = list()
    for elem in arr:
        o_type, length, height = [float(i) for i in elem.split()]
        res_arr.append(Subject(o_type, length, height))
    return res_arr
