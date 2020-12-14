#!/usr/bin/python

lines = open('5.txt', 'r').readlines()
lines = list(map(str.strip, lines))

data = []
for line in lines:
    entry = {}
    rows = line[:7]
    columns = line[-3:]

    lower = 0
    upper = 127
    for char in rows:
        if char == "F":
            upper = int((upper + lower - 1) / 2)
        elif char == "B":
            lower = int((upper + lower + 1) / 2)

    if (lower != upper):
        print("Something went wrong...")
        exit
    entry["row"] = upper

    lower = 0
    upper = 7
    for char in columns:
        if char == "L":
            upper = int((upper + lower - 1) / 2)
        elif char == "R":
            lower = int((upper + lower + 1) / 2)

    if (lower != upper):
        print("Something went wrong...")
        exit
    entry["column"] = upper

    entry["id"] = entry["row"] * 8 + entry["column"]
    data.append(entry)



def part1():
    highest = 0
    for seat in data:
        if seat["id"] > highest:
            highest = seat["id"]

    print(highest)


def part2():
    seatids = [seat["id"] for seat in data]
    for seatid in range(896):
        if not seatid in seatids and \
           (seatid + 1) in seatids and \
           (seatid - 1) in seatids:
            print(seatid)


part1()
part2()
