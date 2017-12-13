# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 08:40:29 2017

@author: SURAJ
"""

from tkinter import *
from compare_test_with_dict import * 
import csv


i=3
rows = []
columnNameArray = []
preProcessedLayoutIdArray =[]
preProcessedData =[]

root = Tk()
root.title("Team MS4")
leftFrame = Frame(root)
leftFrame.grid(row=0,column=0,sticky="n")
rightFrame = Frame(root)
rightFrame.grid(row=0,column=1,)
# Left column layout

def getLayoutDataAfterPreprocessing():
     RecommendedArrayList = []
     with open('./Data/layouts.csv', "rt") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for layoutId in preProcessedLayoutIdArray:
                if layoutId[0] in row:
                    RecommendedArrayList = [layoutId[0],row[1],row[3],layoutId[1]]
                    preProcessedData.append(RecommendedArrayList)
     print('preProcessedData',preProcessedData)

def renderSimilarLayouts():
    rowIndex = 2
    if len(preProcessedData) > 0:
        for row in preProcessedData:
            Label(rightFrame, text=row[0]).grid(row=rowIndex,column=0)
            Label(rightFrame, text=row[1]).grid(row=rowIndex,column=1)
            Label(rightFrame, text=row[2]).grid(row=rowIndex,column=2)
            Label(rightFrame, text=row[3]).grid(row=rowIndex,column=3)
            rowIndex=rowIndex+1
    else:
         Label(rightFrame, text="Sorry No Similar Layouts found.").grid(row=2,column=0)
                    
def saveLayout():
    global preProcessedLayoutIdArray
    for rowno, row in list(enumerate(rows)):
        columnNameArray.append(row[0].get())
        print(columnNameArray)
    assignInputColumnNames(columnNameArray)
    preProcessedLayoutIdArray = readOptimizedData()
    getLayoutDataAfterPreprocessing()
    renderSimilarLayouts()

def delete_row(columnName,dataType):
    for rowno, row in reversed(list(enumerate(rows))):
        if (row[0].get() == columnName and row[1].get() == dataType):
            for i in row:
                i.destroy()
            rows.pop(rowno)

def add_row():
    _columnName= columnNameEdit.get()
    _dataType= variable.get()
    _length= lengthValue.get()
    global i 
    i=i+1
    items = []
    for j in range(0,3): #Columns
        _columnNameContent = StringVar()
        _dataTypeContent = StringVar()
        _lengthContent = StringVar()
        
        _columnNameContent.set(_columnName)
        _dataTypeContent.set(_dataType)
        _lengthContent.set(_length)
       
        _columnNameLabel = Entry(leftFrame, textvariable=_columnNameContent, state = 'readonly')
        _dataTypeLabel = Entry(leftFrame, textvariable=_dataTypeContent, state = 'readonly')
        _lengthLabel = Entry(leftFrame, textvariable=_lengthContent, state = 'readonly')
        deleteFieldButton = Button(leftFrame,text="X",fg="red",bg="white",command = lambda: delete_row(_columnName,_dataType))
        
        items.append(_columnNameLabel)
        items.append(_dataTypeLabel)
        items.append(_lengthLabel)
        items.append(deleteFieldButton)
        _columnNameLabel.grid(row=i, column=0)
        _dataTypeLabel.grid(row=i, column=1)
        _lengthLabel.grid(row=i, column=2)
        deleteFieldButton.grid(row=i, column=3)
    rows.append(items)
    columnNameValue.set("")
    variable.set("NVARCHAR2")
    lengthValue.set("")

Label(leftFrame, text="Add New Layout",fg="Blue",font = "Helvetica 14 bold italic").grid(row=0,column=0)


Label(leftFrame, text="Column Name").grid(row=1,column=0)
Label(leftFrame, text="DataType").grid(row=1,column=1)
Label(leftFrame, text="length").grid(row=1,column=2)

columnNameValue = StringVar()
columnNameEdit = Entry(leftFrame, textvariable = columnNameValue)

lengthValue = StringVar()
lengthEdit = Entry(leftFrame,textvariable = lengthValue)
lengthValue.set("")
addFieldButton = Button(leftFrame,text="+",fg="green",bg="white",command = add_row)

saveButton = Button(leftFrame,text="Save",fg="white",bg="green",command= lambda:saveLayout())


variable = StringVar(leftFrame)
variable.set("NVARCHAR2") # default value
dropdownDatatype = OptionMenu(leftFrame, variable,"NVARCHAR2", "DATE", "VARCHAR2", "NUMBER","CHAR","CURRENCY","DATETIME","INTEGER","MONEY","NUMERIC","TIMESTAMP","VARCHAR")



columnNameEdit.grid(row=2, column=0)
dropdownDatatype.grid(row=2, column=1)
lengthEdit.grid(row=2, column=2)
addFieldButton.grid(row=2,column = 3)
saveButton.grid(row=2,column = 4)

#right column

Label(rightFrame, text="Recommended Layouts for given fields",font = "Helvetica 14 bold italic").grid(row=0)

Label(rightFrame, text="Layout Id").grid(row=1,column=0)
Label(rightFrame, text="Payor").grid(row=1,column=1)
Label(rightFrame, text="DataType").grid(row=1,column=2)
Label(rightFrame, text="matched count").grid(row=1,column=3)


root.geometry("1250x800")

root.mainloop()