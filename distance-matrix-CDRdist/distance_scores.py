#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:11:23 2024

@author: guanyingxue
"""

from two_sequences_scores import getDistanceSW
import pandas as pd

# read the TRA sequence of CDR3
cdr_pd=pd.read_csv('./TRA_prepared.csv', header=None)
print(cdr_pd)
cdr_list=[]
for cdr in cdr_pd[0]:
    cdr_list.append(cdr)
print(cdr_list)

# calculate distance scores and return a dictionary of dictionaries of scores
def calculate_scores(cdr_list, length_dep=True):
    memo = {}
    scores = {}
    for cdr in cdr_list:
        cdr_dict = {}
        for other_cdr in cdr_list:
            if cdr != other_cdr:
                if (cdr, other_cdr) in memo:
                    cdr_dict[other_cdr] = memo[(cdr, other_cdr)]
                elif (other_cdr, cdr) in memo:
                    cdr_dict[other_cdr] = memo[(other_cdr, cdr)]
                else:
                    score = getDistanceSW(cdr, other_cdr, length_dep, gap_penalty=-10)
                    cdr_dict[other_cdr] = score
                    memo[(cdr, other_cdr)] = score
        scores[cdr] = cdr_dict
    return scores

distance_scores = calculate_scores(cdr_list)

def convert_to_distance_matrix(distance_scores):
    distance_matrix = {}
    for cdr, scores in distance_scores.items():
        distance_matrix[cdr] = {}
        for other_cdr, score in scores.items():
            distance_matrix[cdr][other_cdr] = score
        # Set the distance score of each sequence from itself to 0
        distance_matrix[cdr][cdr] = 0
    return distance_matrix

# Convert distance score to distance matrix
distance_matrix = convert_to_distance_matrix(distance_scores)

# Print distance matrix
def print_distance_matrix(distance_matrix, cdr_list):
    print("\t" + "\t".join(cdr_list))
    for cdr1 in cdr_list:
        print(cdr1 + "\t", end="")
        for cdr2 in cdr_list:
            print("{:.6f}".format(distance_matrix[cdr1].get(cdr2, 0)), end="\t")
        print()
print_distance_matrix(distance_matrix, cdr_list)



