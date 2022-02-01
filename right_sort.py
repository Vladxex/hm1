
def s_or_t(nn_list, sli):
    w_m = [((nn_list[1][0] - nn_list[0][0]) ** 2 + (nn_list[1][1] - nn_list[0][1]) ** 2) ** 0.5, 0]
    for idx, n in enumerate(nn_list[1::]):
        w_n = ((n[0] - nn_list[0][0]) ** 2 + (n[1] - nn_list[0][1]) ** 2) ** 0.5
        if w_m[0] > w_n:
            w_m = [w_n, idx+1]
    if w_m[1] > 0:
        nn_list[1], nn_list[w_m[1]] = nn_list[w_m[1]], nn_list[1]
    while len(nn_list)>3:
        sli.append(nn_list[0])
        return s_or_t(nn_list[1::],sli)
    sli.extend(nn_list)
    return sli
