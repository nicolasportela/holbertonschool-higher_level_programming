#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    else:
        for k, v in a_dictionary.items():
            if v > (v - 1):
                maxi = k
                v = v + 1
            else:
                v = v + 1
                continue
        return maxi
