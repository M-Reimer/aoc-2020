#!/usr/bin/python

lines = open('1.txt', 'r').readlines()
numbers = list(map(int, lines))

def part1():
    for n1 in numbers:
        for n2 in numbers:
            if n1 + n2 == 2020:
                print(n1 * n2)
                return

def part2():
    for n1 in numbers:
        for n2 in numbers:
            for n3 in numbers:
                if n1 + n2 + n3 == 2020:
                    print(n1 * n2 * n3)
                    return

part1()
part2()
