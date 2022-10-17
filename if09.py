def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    m = a % 10
    n = (a // 10) % 10

    A = m * 10 + n
    s = 0
    print(A)
    print(a)
    if a >= A:
        s = True
    else:
        s = False

    return s
print(main(54))