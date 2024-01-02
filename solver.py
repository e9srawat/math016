"""MATH 016"""


def solver(n):
    """
    Returns sum of digits of 2^n
    """
    starter = "1"
    for i in range(n):
        carry = None
        product = "0"
        fprod = []
        for j in reversed(range(len(str(starter)))):
            if carry:
                if j == 0:
                    product = str((int(starter[j]) * 2) + int(carry))
                    fprod.append(product)
                    break
                product = str((int(starter[j]) * 2) + int(carry))
            else:
                if j == 0:
                    product = str((int(starter[j]) * 2))
                    fprod.append(product)
                    break
                product = str(int(starter[j]) * 2)
            carry = product[:-1]
            product = product[-1]
            fprod.append(product)
        starter = "".join(reversed(fprod))

    return sum(int(i) for i in starter)
