def main(a,b,c):
    """
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    m = 0
    if a > 0 and b > 0 and c > 0:
        m += 3
    elif a > 0 and b > 0 or b > 0 and c > 0 or a > 0 and c > 0:
        m += 2
    else:
        m += 1
    return m
print(main(5,-9,-6))