"""
 * dna.py
 *
 * Introductie Programmeren
 * Ezra Lynch
 *
 * - finds dna patterns in a dna sequence
 * - assigns a dna sequence to a person
"""
from sys import argv
from csv import reader
from csv import DictReader

# number of arguments must be 3
while len(argv) != 3:
    print("Usage: dna.py database.csv sequence.txt")
    break

# opens the txt file with the sequence and puts it in a list
with open(argv[2]) as dnasequence:
    sequencereader = reader(dnasequence)

    for row in sequencereader:
        sequence = row

seq = sequence[0]

# opens the csv file with the keys and puts it in a list
with open(argv[1]) as keys:
    readkeys = reader(keys)

    for row in readkeys:
        dnakeys = row
        dnakeys.pop(0)
        break

numbersequence = {}

# adds the keys to a dictionairy
for eachkey in dnakeys:
    numbersequence[eachkey] = 1

# checks the sequence for every single dna key
for key in dnakeys:
    length = len(key)
    max = 0
    temp = 0

    for i in range(len(seq)):

        # if a certain part of the sequence corresponds with the key it goes to the next
        if seq[i: i + length] == key:
            while seq[i - length: i] == seq[i: i + length]:
                temp += 1
                i = i + length
                continue


        # if a certain part doesn't correspond it records the maximum
        elif seq[i: i + length] != key:
            if seq[i - length: i] == key:
                i = i - length + 1

            if temp > max:
                max = temp
                temp = 0

            continue

    # if a key has been checked the max is put in a list with the keys
    max = max + 1
    numbersequence[key] = max

# open the csv file again, now as an index of people
with open(argv[1], newline='') as people:
    readpeople = DictReader(people)

# checks if the maximums in the list correspond with those in the csv file
    for person in readpeople:
        match = 0

        for number in numbersequence:

            if numbersequence[number] == int(person[number]):
                match = match + 1

            if match == len(numbersequence):
                print(person['name'])
                exit()

    print('No match')





