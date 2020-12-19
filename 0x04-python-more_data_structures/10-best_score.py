#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    k_list = list(a_dictionary.keys())
    v_list = list(a_dictionary.values())
    maxv = v_list[0]
    for v in v_list:
        if v > maxv:
            maxv = v
    position = v_list.index(v)
    maxk = k_list[position]
    return maxk
