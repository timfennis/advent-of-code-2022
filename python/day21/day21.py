input = open('input').read()
# input = open('example').read()


def calc(humn):
    D = dict()
    i = 0
    while 'root' not in D.keys():
        i += 1
        for line in input.split('\n'):
            val, op = line.split(': ')

            if val == 'humn':
                D['humn'] = humn
            if val == 'root':
                a, b = op.split(' + ')
                if a in D.keys() and b in D.keys():
                    # print(D[a], D[b], i)
                    return (D[a], D[b], D[a] == D[b])
            if val not in D.keys():
                if '+' in op:
                    a, b = op.split(' + ')
                    if a in D.keys() and b in D.keys():
                        a = D[a]
                        b = D[b]
                        D[val] = a + b
                elif '-' in op:
                    a, b = op.split(' - ')
                    if a in D.keys() and b in D.keys():
                        a = D[a]
                        b = D[b]
                        D[val] = a - b
                elif '*' in op:
                    a, b = op.split(' * ')
                    if a in D.keys() and b in D.keys():
                        a = D[a]
                        b = D[b]
                        D[val] = a * b
                elif '/' in op:
                    a, b = op.split(' / ') 
                    if a in D.keys() and b in D.keys():
                        a = D[a]
                        b = D[b]
                        D[val] = a // b
                else:
                    D[val] = int(op)
    return D['root']

# print(clac(585))
# print(clac(586))
# x, _, _ = clac(0)

lower_bound = 1000000000000
upper_bound = 10000000000000

while True:
    human_number = lower_bound + ((upper_bound - lower_bound) // 2)
    
    a, b, _ = calc(human_number)

    print(lower_bound, upper_bound, human_number, a, b, a - b)
    outcome = a - b
    if outcome < 0:
        upper_bound = human_number
    elif outcome > 0:
        lower_bound = human_number
    else:
        print(human_number)
        break
    

# current(100) = 55_641_397_879_860
# target       =  6_745_394_553_620