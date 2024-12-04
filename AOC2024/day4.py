def part1(data):
    count = 0
    for i, elem in enumerate(data):
        for j, letter in enumerate(elem):
            if letter == 'X':
                # Back
                if i > 2:
                    count += (data[i-1][j] == 'M' and data[i-2][j] == 'A' and data[i-3][j] == 'S')
                    # UpperLeft
                    if j > 2:
                        count += (data[i - 1][j - 1] == 'M' and data[i - 2][j - 2] == 'A' and data[i - 3][j - 3] == 'S')
                    # UpperRight
                    if j < len(elem)-3:
                        count += (data[i - 1][j + 1] == 'M' and data[i - 2][j + 2] == 'A' and data[i - 3][j + 3] == 'S')
                # Left
                if j > 2:
                    count += (data[i][j-1] == 'M' and data[i][j-2] == 'A' and data[i][j-3] == 'S')

                # Right
                if j < len(elem)-3:
                    count += (data[i][j+1] == 'M' and data[i][j+2] == 'A' and data[i][j+3] == 'S')
                # Front
                if i < len(data) - 3:
                    count += (data[i + 1][j] == 'M' and data[i + 2][j] == 'A' and data[i + 3][j] == 'S')
                    # DownLeft
                    if j > 2:
                        count += (data[i + 1][j - 1] == 'M' and data[i + 2][j - 2] == 'A' and data[i + 3][j - 3] == 'S')
                    # DownRight
                    if j < len(elem)-3:
                        count += (data[i + 1][j + 1] == 'M' and data[i + 2][j + 2] == 'A' and data[i + 3][j + 3] == 'S')
    return count

def part2(data):
    count = 0
    for i, elem in enumerate(data):
        if 0 < i < len(data)-1:
            for j, letter in enumerate(elem):
                if letter == 'A' and len(elem) - 1 > j > 0:
                    if data[i-1][j-1] == 'M' and data[i-1][j+1] == 'M' and data[i+1][j-1] == 'S' and data[i+1][j+1] == 'S':
                        count += 1
                    elif data[i - 1][j - 1] == 'S' and data[i - 1][j + 1] == 'S' \
                            and data[i + 1][j - 1] == 'M' and data[i + 1][j + 1] == 'M':
                        count += 1
                    elif data[i - 1][j - 1] == 'S' and data[i - 1][j + 1] == 'M' \
                            and data[i + 1][j - 1] == 'S' and data[i + 1][j + 1] == 'M':
                        count += 1
                    elif data[i - 1][j - 1] == 'M' and data[i - 1][j + 1] == 'S' \
                            and data[i + 1][j - 1] == 'M' and data[i + 1][j + 1] == 'S':
                        count += 1
    return count


def read(file):
    with open(file) as f:
        return [list(line.strip()) for line in f]


data = read('day4.txt')
print(part1(data))
print(part2(data))
