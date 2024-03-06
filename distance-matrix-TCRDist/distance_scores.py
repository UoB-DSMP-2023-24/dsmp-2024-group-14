#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 00:10:52 2024

@author: guanyingxue
"""
from sw_scoring import getDistanceSW
cdr_list=["CASRGASGSYEQYF","CASSQGSGWETQYF","CASSPQRGPYEQYF","CASRRGTDLTDTQYF"]

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

print(distance_scores)