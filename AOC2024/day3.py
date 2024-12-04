import re

def part1(data, part2=False):
    suma = 0
    ENABLE = True
    for item in data:
        ints = re.findall(r'\d{1,3}', item)
        if len(ints) == 1:
            print("Numero repetido")
        if len(ints) == 2 and ENABLE:
            suma += (int(ints[0]) * int(ints[1]))
        elif item == "do()" and part2:
            ENABLE = True
        elif item == "don't()" and part2:
            ENABLE = False
    return suma

def read(file):
    s = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', open(file).read())
    return s

data = read("day3.txt")
print(part1(data))
print(part1(data, True))
