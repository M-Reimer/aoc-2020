#!/usr/bin/python

lines = open('3.txt', 'r').readlines()
lines = list(map(str.strip, lines))

def part1():
    position = 0
    trees = 0

    for line in lines:
        if position >= len(line):
            position -= len(line)
        if line[position] == '#':
            trees += 1
        position += 3

    print(trees)

def part2():
    trees1 = 0
    trees2 = 268 # Known good result of part 1
    trees3 = 0
    trees4 = 0
    trees5 = 0

    position = 0
    for line in lines:
        if position >= len(line):
            position -= len(line)
        if line[position] == '#':
            trees1 += 1
        position += 1

    position = 0
    for line in lines:
        if position >= len(line):
            position -= len(line)
        if line[position] == '#':
            trees3 += 1
        position += 5

    position = 0
    for line in lines:
        if position >= len(line):
            position -= len(line)
        if line[position] == '#':
            trees4 += 1
        position += 7

    position = 0
    skip = False
    for line in lines:
        if skip:
            skip = False
            continue

        if position >= len(line):
            position -= len(line)
        if line[position] == '#':
            trees5 += 1
        position += 1

        skip = True

    print(trees1 * trees2 * trees3 * trees4 * trees5)

part1()
part2()
