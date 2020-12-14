#!/usr/bin/python

lines = open('2.txt', 'r').readlines()
data = []
for line in lines:
    rule, password = line.strip().split(": ")
    range, character = rule.split(" ")
    lower, upper = range.split("-")
    data.append({"password": password,
                 "character": character,
                 "lower": int(lower),
                 "upper": int(upper)})

def part1():
    valid = 0

    for entry in data:
        counter = 0

        for character in entry["password"]:
            if character == entry["character"]:
                counter += 1

        if counter >= entry["lower"] and counter <= entry["upper"]:
            valid += 1

    print(valid)

def part2():
    valid = 0

    for entry in data:
        first = entry["password"][entry["lower"] - 1]
        second = entry["password"][entry["upper"] - 1]
        counter = 0

        if first == entry["character"]:
            counter += 1
        if second == entry["character"]:
            counter += 1

        if counter == 1:
            valid += 1

    print(valid)


part1()
part2()
