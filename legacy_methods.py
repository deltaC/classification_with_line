def middle_point(arr):
    a1 = list()
    a2 = list()
    mid_tpx1 = None; mid_tpy1 = None; mid_tpx2 = None; mid_tpy2 = None
    for subj in arr:
        if subj.o_type == 0:
            a1.append([subj.length, subj.height])
        else:
            a2.append([subj.length, subj.height])
    for i in a1:
        mid_tpx1 = sum([j[0] for j in a1]) / len(a1)
        mid_tpy1 = sum([j[1] for j in a1]) / len(a1)
    for i in a2:
        mid_tpx2 = sum([j[0] for j in a2]) / len(a2)
        mid_tpy2 = sum([j[1] for j in a2]) / len(a2)
    return [(mid_tpx1, mid_tpy1), (mid_tpx2, mid_tpy2)]


def a_coef(mid_points):
    return (mid_points[0][1] + mid_points[1][1]) / (mid_points[0][0] + mid_points[1][0])
