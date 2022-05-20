#!/usr/bin/env python3

chr_list = ["l", "i", "u", "t"]
bad_list = ["c","r","e","m", "a", "b", "p", "s", "g"]
pos_list = ["", "", "", "", ""]
possible = []

##############################################
def check_any_list(str, set):
    return any(x in str for x in set)
def check_all_list(str, set):
    return all(x in str for x in set)

def reduce(pos, letter, list):
    matches = []
    for index, line in enumerate(list):
        if letter == line[pos]:
            matches.append(line)

    return matches

file  = open('files/sgb-words.txt', 'r')
lines = file.readlines()

# Reduce list to words with known letters
for index, line in enumerate(lines):
    if not check_any_list(line, bad_list) and check_all_list(line, chr_list):
        possible.append(line)

# Check positional characters
if pos_list[0] != "":
    possible = reduce(0, pos_list[0], possible)

if pos_list[1] != "":
    possible = reduce(1, pos_list[1], possible)

if pos_list[2] != "":
    possible = reduce(2, pos_list[2], possible)

if pos_list[3] != "":
    possible = reduce(3, pos_list[3], possible)

if pos_list[4] != "":
    possible = reduce(4, pos_list[4], possible)

file.close()

print(possible)