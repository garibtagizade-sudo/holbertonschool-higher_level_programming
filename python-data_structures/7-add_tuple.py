#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new = f(tuple_a)
    new1 = f(tuple_b)
    return (new[0] + new1[0], new[1] + new1[1])


def f(t=()):
    # tuple uzunluğu 0-dırsa
    if len(t) == 0:
        return (0, 0)
    # tuple uzunluğu 1-dirsə
    elif len(t) == 1:
        return (t[0], 0)
    # tuple uzunluğu 2 və ya daha çoxdursa
    else:
        return (t[0], t[1])
