#!/usr/bin/python
import re

lines = open('4.txt', 'r').readlines()
entry = {}
data = [entry]
for line in lines:
    line = line.strip()
    if line == "":
        entry = {}
        data.append(entry)
        continue

    pairs = line.split(" ")
    for pair in pairs:
        name, value = pair.split(":")
        entry[name] = value


def part1():
    valid = 0
    for passport in data:
        ok = True
        for field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
            if not field in passport:
                ok = False
                break

        if ok:
            valid += 1

    print(valid)

def part2():
    valid = 0
    for passport in data:
        ok = True
        for field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
            if not field in passport:
                ok = False
                break
        if not ok:
            continue

        if int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
            continue

        if int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020:
            continue

        if int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030:
            continue

        m = re.match("^([0-9]+)(cm|in)$", passport["hgt"])
        if m:
            number, unit = m.groups()
            number = int(number)
            if unit == "cm":
                if number < 150 or number > 193:
                    continue
            if unit == "in":
                if number < 59 or number > 76:
                    continue
        else:
            continue

        if not re.match("^#[0-9a-f]{6}$", passport["hcl"]):
            continue

        if not passport["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"]:
            continue

        if not re.match("^[0-9]{9}$", passport["pid"]):
            continue

        valid += 1

    print(valid)


part1()
part2()
