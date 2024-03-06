#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 6 16:26:43 2024

@author: XiaofeiSong
"""
from two_sequences_scores import getDistanceSW
import pandas as pd
import numpy as np
from sklearn.preprocessing import RobustScaler
import matplotlib.pyplot as plt
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
print(1)
print(distance_scores)