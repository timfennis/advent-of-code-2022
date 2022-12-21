input = open('input').read()

def calc(humn):
    D = dict()
    i = 0
    while 'root' not in D.keys():
        i += 1
        for line in input.split('\n'):
            val, op = line.split(': ')

            if val == 'humn' and humn is not None:
                D['humn'] = humn
            if val == 'root':
                a, b = op.split(' + ')
                if a in D.keys() and b in D.keys():
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

# part 1
a, b, _ = calc(None)
print("part 1", a + b)

lower_bound = None
upper_bound = None

for i in range(20):
    upper_bound = 10 ** i
    a, b, _ = calc(upper_bound)
    if a - b < 0:
        break
    else:
        lower_bound = upper_bound

outcome = -1
while outcome != 0:
    human_number = lower_bound + ((upper_bound - lower_bound) // 2)
    
    a, b, _ = calc(human_number)

    outcome = a - b
    if outcome < 0:
        upper_bound = human_number
    elif outcome > 0:
        lower_bound = human_number
    
print("part 2", human_number)