#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    # It was an alternative way, which works well but checker doesn't like...
    # k_list = list(a_dictionary.keys())
    # v_list = list(a_dictionary.values())
    # maxv = v_list[0]
    # for v in v_list:
    #    if v > maxv:
    #        maxv = v
    # position = v_list.index(v)
    # maxk = k_list[position]
    # return maxk
    #
    maxv = 0
    for k, v in a_dictionary.items():
        if v > num:
            maxv = v
    for k, v in a_dictionary.items():
        if v == maxv:
            return k
