#!/usr/local/bin/python

from itertools import permutations, islice, combinations
import os


list_a = [
    "क",
    "ख",
    "ग",
    "घ",
    "ङ",
    "च",
    "छ",
    "ज",
    "झ",
    "ञ",
    "ट",
    "ठ",
    "ड",
    "ढ",
    "ण",
    "त",
    "थ",
    "द",
    "ध",
    "न",
    "ऩ",
    "प",
    "फ",
    "ब",
    "भ",
    "म",
    "य",
    "र",
    "ल",
    "ळ",
    "व",
    "श",
    "ष",
    "स",
    "ह"
]

# Use combinations
for L in range(0, len(list_a)+1):
    if L>1 and L < 6:
        file_name = "permutations_of_" + str(L) + ".txt"
        # clear file
        with open(file_name, "w") as fn:
            pass
        with open(file_name, "a") as fn:
            for subset in combinations(list_a, L):
                print(subset)
                item_joined = "्".join(subset)
                fn.write(item_joined)
                fn.write("\n")

