#!/usr/local/bin/python

from itertools import permutations, islice, combinations
import os


consonant_list = [
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
    # "ऩ",
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
    "ह",
]

vowel_list = [
    "अ",
    "आ",
    "इ",
    "ई",
    "उ",
    "ऊ",
    "ऋ",
    "ॠ",
    "ऌ",
    "ॡ",
    "ऍ",
    "ऎ",
    "ए",
    "ऐ",
    "ऑ",
    "ऒ",
    "ओ",
    "औ",
]

mAtrA_list = [
    "",
    "ऀ",
    "ँ",
    "ं",
    "ः",
    "ऺ",
    "ऻ",
    # "़",
    # "ऽ",
    "ा",
    "ि",
    "ी",
    "ु",
    "ू",
    "ृ",
    "ॄ",
    "ॢ",
    "ॣ",
    "ॅ",
    "ॆ",
    "े",
    "ै",
    "ॉ",
    "ॊ",
    "ो",
    "ौ",
    "्",
    # "ॎ",
    "ॏ",
]
def per_n_com(permutations_or_combinations):
    for L in range(0, len(consonant_list) + 1):
        if L > 1 and L < 5:
            if permutations_or_combinations == 'c':
                file_name = "combinations_of_" + str(L) + ".txt"
                bigData = combinations(consonant_list, L)
            elif permutations_or_combinations == 'p':
                file_name = "permuations_of_" + str(L) + ".txt"
                bigData = permutations(consonant_list, L)
            print(file_name)
            # clear file
            with open(file_name, "w") as fn:
                pass
            with open(file_name, "a") as fn:
                for subset in bigData:
                    # print(subset)
                    # item_joined = "्".join(subset)
                    # fn.write(item_joined)
                    # fn.write("\n")
                    for each_mAtrA in mAtrA_list:
                        item_joined = each_mAtrA.join(subset)
                        item_joined_with_mAtrA = item_joined + each_mAtrA
                        fn.write(item_joined_with_mAtrA)
                        fn.write("\n")

# 
if __name__ == "__main__":
    per_n_com('c')
    per_n_com('p')