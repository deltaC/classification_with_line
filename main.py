from designations import Subject


def generating_array(number_of_subjects):
    arr = list()
    for i in range(number_of_subjects):
        o_type, length, height = [float(j) for j in input().split()]
        ob = Subject(o_type, length, height)
        arr.append(ob)
    return arr


print('Type number of objects')
n = int(input())
subjects = generating_array(n)