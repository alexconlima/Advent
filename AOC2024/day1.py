import numpy as np

def part1(c1, c2):
    c1.sort()
    c2.sort()

    return np.abs(c1 - c2).sum()

def part2(c1, c2):
    suma = sum(num * times for num, times in zip(*np.unique(c2, return_counts=True)) if num in set(c1))

    return suma

c1, c2 = np.loadtxt('day1.txt', dtype=int, unpack=True)
print(part1(c1, c2))
print(part2(c1, c2))