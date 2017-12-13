# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 20:45:09 2017

@author: SURAJ
"""

import csv
import pandas as pd
import numpy as np
import dictionary as dict
similarLayouts = []

allKeys=dict.dictionary.keys()
inputData =[]
def assignInputColumnNames(inputColumnArray):
    print('input columnArray',inputColumnArray)
    global inputData
    inputData= inputColumnArray
    print('assigned columnArray',inputData)

i = 0
def getKeyofInputColumnName():
  
    for key, value in dict.dictionary.items():
        index = 0;
        for input in inputData:
            inputDataLowerCase = input.lower()
            if inputDataLowerCase in value:
              print('----',key)
              inputData[index] = key
            index= index +1
               
# =============================================================================
# def compareDataWithLayoutField
# =============================================================================
         
def compareKeyWithOptimizedData(optimizedRow):
    layoutwithCommonFieldCount =[]
    global similarLayouts
    commonFields=list(set(inputData) & set(optimizedRow))
    if len(commonFields) > 0:
        layoutwithCommonFieldCount = [optimizedRow[0],len(commonFields)]
        similarLayouts.append(layoutwithCommonFieldCount)
    #print('common fields count',i)
    
        

def readOptimizedData():
    getKeyofInputColumnName()
    with open('./optimised1.csv', "rt") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            compareKeyWithOptimizedData(row)
    
    item = sorted(similarLayouts, key=lambda x: (-x[1], x[0]))
    return item
# =============================================================================
# test = readOptimizedData()
# print('similar data',test)
# =============================================================================
