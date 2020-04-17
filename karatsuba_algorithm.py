from math import log, ceil, floor


def karatsuba(x, y):
    if x < 10 and y < 10:
        return x * y

    # firstNumberBits = ceil(log(x, 10)) if x > 0 else 0
    # secondNumberBits = ceil(log(y, 10)) if y > 0 else 0
    firstNumberBits = len(str(x))
    secondNumberBits = len(str(y))
    print(firstNumberBits, secondNumberBits)
    nBits = max(firstNumberBits, secondNumberBits)
    halfNBits = ceil(nBits / 2)
    # print(nBits, halfNBits)

    Xh = floor(x // 10 ** halfNBits)
    Xl = (x % (10 ** halfNBits))
    Yh = floor(y // 10 ** halfNBits)
    Yl = (y % (10 ** halfNBits))

    st1 = karatsuba(Xh, Yh)
    st2 = karatsuba(Xl, Yl)
    st3 = karatsuba(Xh + Xl, Yh + Yl) - st1 - st2
    return int(st1 * (10 ** (halfNBits * 2)) + st3 * (10 ** halfNBits) + st2)


x = 1111111111111111111111111111111111111111111111111111111111111111
y = 2222222222222222222222222222222222222222222222222222222222222222

result = karatsuba(x, y)
print(result)
