def part1(data):
    suma = 0
    for row in data:
        destroy = False
        if row[0] > row [1] and (row[0] - row[1]) <= 3:
            for i in (range(1, len(row)-1)):
                if row[i] <= row[i+1] or (row[i] - row[i + 1]) > 3:
                    destroy = True
                    break
            if destroy:
                continue
            suma += 1
        elif row[0] < row[1] and (row[1] - row[0]) <= 3:
            for i in (range(1, len(row)-1)):
                if row[i] >= row[i+1] or (row[i+1] - row[i]) > 3:
                    destroy = True
                    break
            if destroy:
                continue
            suma += 1
        else:
            continue
    return suma

def part2(data):
    suma = 0
    for row in data:
        errors = 0
        if row[0] > row [1]:
            for i in (range(len(row)-1)):
                if row[i] <= row[i+1] or (row[i] - row[i + 1]) > 3:
                    errors += 1
            if errors > 1:
                continue
            suma += 1
        elif row[0] < row[1]:
            for i in (range(len(row)-1)):
                if row[i] >= row[i+1] or (row[i+1] - row[i]) > 3:
                    errors += 1
            if errors > 1:
                continue
            suma += 1
        else:
            errors += 1
            up = None

            for i in (range(1, len(row)-1)):
                if up:
                    if row[i] <= row[i+1] or (row[i] - row[i + 1]) > 3:
                        errors += 1
                        break
                elif not up:
                    if row[i] >= row[i + 1] or (row[i + 1] - row[i]) > 3:
                        errors += 1
                        break
                elif up is None:
                    if row[i] > row[i+1] and (row[i] - row[i + 1]) <= 3:
                        up = True
                    elif row[i+1] > row[i] and (row[i+1] - row[i]) <= 3:
                        up = False
                    else:
                        errors += 1
                        break

            if errors > 1:
                continue
            suma += 1
    return suma



def read(file):
    lines = []
    with open(file) as f:
        for line in f:
            lines.append(list(map(int, line.split())))
    return lines



rows = read("day2.txt")
print(part1(rows))
print(part2(rows))