# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 13:20:41 2017

@author: saroj
"""
import csv
import pandas as pd
import dictionary as dict
import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "./Data/all_layouts_csv.csv"
abs_file_path = os.path.join(script_dir, rel_path)
""" function to remove duplicate column values """
def removeDuplicateColumns(row):
        layoutId=row.pop(0)
        row=list(set(row))
        row.insert(0,layoutId)
        return row
    
""" code to assign key column values """
inputlayout=[]
dataList=[]
allKeys=dict.dictionary.keys()
csv.field_size_limit(100 * 1024 * 1024)
with open(abs_file_path.replace("\\","/"), "rt") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
          inputlayout.append(row)                  
    for row in inputlayout:      
        row=filter(None,row)
        row = [element.lower() for element in row]
        dataList.append(row)          
    for row in range(len(dataList)): 
        count=0
        for column in range(1,len(dataList[row])):
            for key in allKeys:                   
                isAvailable=dataList[row][column].replace("_","").replace("#","").replace(" ","") in dict.dictionary[key]                
                if isAvailable:
                    count=count+1    
                    dataList[row][column]=key                               
df = pd.DataFrame(dataList)
df.to_csv("optimised1.csv", index=False)
                
               