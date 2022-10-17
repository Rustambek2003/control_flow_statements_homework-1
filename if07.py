def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    s = 0
    if a > 0:
        if a % 2 != 0:
            s = "positive odd number"
        else:
            s = "positive even number"
    elif a < 0:
        if a % 2 != 0:
            s = "negative odd number"
        else:
            s = "negative odd number"
    else:
        s = "the number is zero"

    return s
print(main(-9))