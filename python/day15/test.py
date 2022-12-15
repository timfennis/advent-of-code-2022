from itertools import chain

a = [1,2,3,4,5]
a[-1:] = [6,7]
print(a)
exit()
# -330877, 393210), range(-903979, 1487250
# -808542, 2277491), range(-808542, 4842206 
a = range(-808542, 2277491)
b = range(-808542, 4842206)

def merge(a: range, b: range):
    if b.start <= a.stop <= b.stop:
        return [range(min(a.start, b.start), b.stop)]
    elif a.start <= b.stop <= a.stop:
        return [range(min(a.start, b.start), a.stop)]
    else:
        return [a, b]
        
print(merge(a, b))