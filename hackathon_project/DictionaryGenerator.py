# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 16:01:25 2017

@author: SUMAN
"""
import csv
import difflib

#load all row from csv file
inputlayout=[];
with open('E:\\ahack\\HAckthon\\column_names.CSV') as csvfile:
        abc = csv.reader(csvfile)
        for row in abc:
            inputlayout.append(row)
          
# remove empty elements          
inputlayer1=[]
for row in inputlayout:
    row[:] = [item for item in row if item != '']
    inputlayer1.append(row)   
    
## lowercase, remove: underscore,SPACE,hash    
inputlayer1 = [[w.replace("_","").replace("#","").replace(" ","").lower() for w in line] for line in inputlayer1]   
              
# extract all column                
allcolumn =[]
for row in inputlayer1:
    for item in row:
        allcolumn.append(item)
        
#unique column_names
uniquecolumn = list(set(allcolumn))  

# sort column
uniquecolumn.sort()

#remove integer value 
col = uniquecolumn[4225:]

x = ['primarycarephysiciannumber','primarycarephysicianid','primarycarephysicianname','primarydiagcode','primarydiagcodeicd','primarydiagnosis','primarydxcode','primarydxdescr','primaryemployeessn','primaryicdcode','primaryicdprocedurecode','primaryinsurancename','primaryinsuranceindicator','primaryphone','primaryphysiciannumber','primaryphysicianprovnumber','primaryproccode','primaryproductkey','primarycareproviderqlifier','primarydiag','primysubidcd','prinproccode','principlediagnosiscode','principlediagnosis','priorauthtypecode','priorauthorization','priorauthorizationindicator','priorauthorizationnumber','priorauthorizationcode','priorauthorixationmedicalcode','priorauthclaimflag','priorauthindicator','procedurecode','proceduredesc','procdiagcode','proccodeubsurg','proctype','processdate','processornumber','procmod','proddate','providergroupname','providernumber','prvno','provideraddress','provnpi','provseq','providerspecialtycode','provtypedescription','ptntfrstname','qtydispense','rxnumber','rxquantity','rxrefillnumber','rxclaimnumber','remark','salestaxamnt','sexcode','subnumber','subgroupnumber','servicedate','submittedamount','specialtydesc','subriberfirstname','subribermiddlename','subriberlastname','surgicalproc','taxamnt','taxid','telephone','terminationdate','thirdpartytype','throughdate','zipcode']


mylist = [];
finalist =[];
for item in x:
    mylist = difflib.get_close_matches(item,col,20,0.9)
    #print mylist
    itm = item[0:1] + item[1:].replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
    #print itm
    delvowel = difflib.get_close_matches(itm,col,20,0.9)
    #print delvowel
    for myitem in delvowel:
        mylist.append(myitem)
    uniquelist = list(set(mylist))
    firstletter = item[0:1]
    #print uniquelist
    for z in uniquelist:
        if z.find(firstletter,0,1)==0:
            finalist.append(z)
    dictrow = "'"+item + "':" + str(finalist) + ","
    print dictrow
    text_file = open("E:\\ahack\\HAckthon\\dict1.txt","a")
    text_file.write(dictrow + " \n")
    text_file.close()
    mylist[:]=[]
    uniquelist[:]=[]
    finalist[:]=[]




        
                