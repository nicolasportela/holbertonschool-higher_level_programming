#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lista = list(tuple_a)
    listb = list(tuple_b)
    if len(lista) == 0:
        lista.append(0)
        lista.append(0)
    elif len(lista) == 1:
        lista.append(0)
    if len(listb) == 0:
        listb.append(0)
        listb.append(0)
    elif len(listb) == 1:
        listb.append(0)
    tuple_a = tuple(lista)
    tuple_b = tuple(listb)
    add1 = tuple_a[0] + tuple_b[0]
    add2 = tuple_a[1] + tuple_b[1]
    return add1, add2
