#!/usr/bin/python3
def magic_calculation(a, b):
    rzlt = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                rzlt += (a ** b) / i
        except Exception:
            rzlt = b + a
            break
    return (rzlt)
