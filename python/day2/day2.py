input = open('input').read();

lines = [line.strip() for line in input.split("\n")]

score = 0
for line in lines:
    (a, b) = line.split(" ")

    if b == "X":
        score += 1
    if b == "Y":
        score += 2
    if b == "Z":
        score += 3

    if a == "A":
        if b == "X":
            score += 3
        if b == "Y":
            score += 6
        if b == "Z":
            score += 0
    if a == "B":
        if b == "X":
            score += 0
        if b == "Y":
            score += 3
        if b == "Z":
            score += 6
    if a == "C":
        if b == "X":
            score += 6
        if b == "Y":
            score += 0
        if b == "Z":
            score += 3

print(score) 


score = 0
for line in lines:
    (a, b) = line.split(" ")

    if b == "X":
        score += 0
    if b == "Y":
        score += 3
    if b == "Z":
        score += 6
    if a == "A": 
        if b == "X":
            score += 3
        if b == "Y":
            score += 1
        if b == "Z":
            score += 2
    if a == "B":
        if b == "X":
            score += 1
        if b == "Y":
            score += 2
        if b == "Z":
            score += 3
    if a == "C":
        if b == "X":
            score += 2
        if b == "Y":
            score += 3
        if b == "Z":
            score += 1

print(score)