from designations import Subject
L = 0.5
REPETITIONS = 1


def generating_array(number_of_subjects):
    arr = list()
    for i in range(number_of_subjects):
        o_type, length, height = [float(j) for j in input().split()]
        ob = Subject(o_type, length, height)
        arr.append(ob)
    return arr


def A_calculating(arr):
    A = 0.25
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


print('Type number of objects')
n = int(input())
subjects = generating_array(n)
print(A_calculating(subjects))