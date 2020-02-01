from designations import Subject
from reading_module import generate_array_from_list, read_text

L = 0.5


def generating_array(number_of_subjects):
    arr = list()
    for i in range(number_of_subjects):
        o_type, length, height = [float(j) for j in input().split()]
        ob = Subject(o_type, length, height)
        arr.append(ob)
    return arr


def A_calculating(arr):
    A = 1
    """I am not sure about need this code, but actually this working more accurately"""
    for subj in arr:
        if subj.o_type == 1:
            y0 = subj.height + 0.1
            E = y0 - A * subj.length
            dA = L * E / subj.length
            A += dA
    for subj in arr:
        if subj.o_type == 0:
            y0 = subj.height - 0.1
            E = y0 - A * subj.length
            dA = L * E / subj.length
            A += dA
    return A


# print('Type number of objects')
# n = int(input())
subjects = generate_array_from_list(read_text('set.txt'))
print(A_calculating(subjects))