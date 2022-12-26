data = open('input').read()
# data = open('example').read()

def to_dec(num: str) -> int:
    pow = len(num)
    if pow == 0:
        return 0
    pow = 5 ** (pow -1)
    fst = num[0]
    nxt = num[1:]
    n = 0
    if fst == '2':
        n = 2 * pow
    elif fst == '1':
        n = pow
    elif fst == '0':
        n = 0
    elif fst == '-':
        n = -pow
    elif fst == '=':
        n = 0 - (2*pow)
    return n + to_dec(nxt)


def to_snafu(num: int) -> str:
    buf = ""

    while num > 0:
        if (num % 5) == 4:
            buf += '-'
            num += 1
        elif (num % 5) == 3:
            buf += '='
            num += 2
        else:
            buf += str(num % 5) 
        num //= 5

    return buf[::-1]


s = sum([to_dec(x) for x in data.splitlines()])
print(s)
print(to_snafu(s))