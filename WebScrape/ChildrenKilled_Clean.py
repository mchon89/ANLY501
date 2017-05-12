import numpy as np
import pandas as pd
from pprint import pprint

myData=[]               #creating an array to bring my data into

dataFile = open('C:/Users/Mike/Desktop/ChildrenKilled.csv', "r")    #the location of my data, change the directory to where the ChildrenKilled file is stored in your computer! 

line = dataFile.readline()          #reading line in my data file 
while(line):                        #while every line in the file
    if line.endswith('\n'):         
        line=line[:-1]
    myData.append(line)             #append every line into myData 
    line = dataFile.readline()      #read line into data file

dataFile.close()            #close my array containg all the lines


myDataFrame = pd.read_csv('C:/Users/Mike/Desktop/ChildrenKilled.csv', sep=',', encoding='latin1')

myDataFrame.columns=["Incident Id", "Incident Date", "State", "City or County", 'Address', '# killed', '# injured']     #I created headers for each column




################################################################################################################ Incident ID


TotalNumberID=len(myDataFrame['Incident Id'])                   #I am going to find the total number of rows for the column Incident Id
print("\n\nThe total number of the rows of Incident Id is")
pprint(TotalNumberID+1)
                                                                            
EveryRowIDWValues=myDataFrame['Incident Id'].notnull().sum()                  #I am going to find the number of every row with values       
print("\n\nThe number of missing values in the Incident Id is")
pprint(int(EveryRowIDWValues)+1)

print("\n\nThen the number of missing values is")                      #The number of rows missing values is total number - number of every row with values
pprint((TotalNumberID+1)-(int(EveryRowIDWValues)+1))                   

print("\n\nThe fraction of missing values for Incident Id")                               #The fraction of missing values is the number of rows missing values over the total number of rows in the column
pprint(((TotalNumberID+1)-(int(EveryRowIDWValues)+1))/(TotalNumberID+1))


Count=0                                                                            #trying to count the number of noise values
i=0                                                                                #I figured that the type of Incident ID is numpy.int64 
                                                                                   #so if one of the row of the column contains something other than the type numpy.int64, that row contains a noise.
                                                                                   
FrameID=myDataFrame['Incident Id']                                                 #I created another variable assigned the column
for j in range(1,(len(FrameID))):                                                  #for j in range of 1 and the length of the column
    if type(FrameID[i])==type(FrameID[j]):                                         #If the type of frameID[i] is equal to the next row, pass
            pass
    if type(FrameID[i])!=type(FrameID[j]):                                         #If the type of frameID[i] is not equal to the next row, then add 1 to the count
            Count+=1

print("\n\nThe number of noise values is")
print(Count)

#the fraction of noise values for this attribute is 0. 

print("\n\nIncident ID is fairly clean")





################################################################################################################ Incident Date
                                                                        
TotalNumberDate=len(myDataFrame['Incident Date'])                               #I am using the same logic as above, to find the total number of rows for Incident Date, to find the number of every row with values, and the fraction of missing values
print("\n\nThe total number of the rows of Incident Date is")
pprint(TotalNumberDate+1)
                                                                            
EveryRowDateWValues=myDataFrame['Incident Date'].notnull().sum()                         
print("\n\nThe number of missing values in the Incident Date is")
pprint(int(EveryRowDateWValues)+1)

print("\n\nThen the number of missing values is")                      
pprint((TotalNumberDate+1)-(int(EveryRowDateWValues)+1))                   

print("\n\nThe fraction of missing values for Incident Date")
pprint(((TotalNumberDate+1)-(int(EveryRowDateWValues)+1))/(TotalNumberDate+1))



Count=0                                                                            #trying to count the number of noise values
i=0                                                                                #I figured that the type of Incident Date is string 
                                                                                   #so if one of the row of the column contains something other than the type string, that row contains a noise.
                                                                                   
FrameDate=myDataFrame['Incident Date']                                               #I created another variable assigned the column
for j in range(1,(len(FrameDate))):                                                  #for j in range of 1 and the length of the column
    if type(FrameDate[i])==type(FrameDate[j]):                                         #If the type of frameID[i] is equal to the next row, pass
            pass
    if type(FrameDate[i])!=type(FrameDate[j]):                                         #If the type of frameID[i] is not equal to the next row, then add 1 to the count
            Count+=1

print("\n\nThe number of noise values is")
print(Count)

#the fraction of noise values for this attribute is 0. 

print("\n\nIncident Date is fairly clean")






################################################################################################################ State
                                                                        
TotalNumberState=len(myDataFrame["State"])                               #I am using the same logic as above, to find the total number of rows for State, to find the number of every row with values, and the fraction of missing values
print("\n\nThe total number of the rows of State is")
pprint(TotalNumberState+1)
                                                                            
EveryRowStateWValues=myDataFrame["State"].notnull().sum()                         
print("\n\nThe number of missing values in the State is")
pprint(int(EveryRowStateWValues)+1)

print("\n\nThen the number of missing values is")                      
pprint((TotalNumberState+1)-(int(EveryRowStateWValues)+1))                   

print("\n\nThe fraction of missing values for State")
pprint(((TotalNumberState+1)-(int(EveryRowStateWValues)+1))/(TotalNumberState+1))



Count=0                                                                            #trying to count the number of noise values
i=0                                                                                #I figured that the type of state is string 
                                                                                   #so if one of the row of the column contains something other than the type string, that row contains a noise.
                                                                                   
FrameState=myDataFrame['State']                                                    #I created another variable assigned the column
for j in range(1,(len(FrameState))):                                                  #for j in range of 1 and the length of the column
    if type(FrameState[i])==type(FrameState[j]):                                         #If the type of frameID[i] is equal to the next row, pass
            pass
    if type(FrameState[i])!=type(FrameState[j]):                                         #If the type of frameID[i] is not equal to the next row, then add 1 to the count
            Count+=1

print("\n\nThe number of noise values is")
print(Count)

#the fraction of noise values for this attribute is 0. 

print("\n\nState is fairly clean")








################################################################################################################ City or County


TotalNumberCity=len(myDataFrame["City or County"])                                         #I am using the same logic as above, to find the total number of rows for city or county, to find the number of every row with values, and the fraction of missing values
print("\n\nThe total number of the rows of City or County is")
pprint(TotalNumberCity+1)
                                                                            
EveryRowCityWValues=myDataFrame["City or County"].notnull().sum()                         
print("\n\nThe number of missing values in the City or County is")
pprint(int(EveryRowCityWValues)+1)

print("\n\nThen the number of missing values is")                      
pprint((TotalNumberCity+1)-(int(EveryRowCityWValues)+1))                   

print("\n\nThe fraction of missing values for City or County")
pprint(((TotalNumberCity+1)-(int(EveryRowCityWValues)+1))/(TotalNumberCity+1))




Count=0                                                                            #trying to count the number of noise values
i=0                                                                                #I figured that the type of city or county is string 
                                                                                   #so if one of the row of the column contains something other than the type string, that row contains a noise.
                                                                                   
FrameCity=myDataFrame["City or County"]                                               #I created another variable assigned the column
for j in range(1,(len(FrameCity))):                                                  #for j in range of 1 and the length of the column
    if type(FrameCity[i])==type(FrameCity[j]):                                         #If the type of frameID[i] is equal to the next row, pass
            pass
    if type(FrameCity[i])!=type(FrameCity[j]):                                         #If the type of frameID[i] is not equal to the next row, then add 1 to the count
            Count+=1

print("\n\nThe number of noise values is")
print(Count)

#the fraction of noise values for this attribute is 0. 

print("\n\nCity or County is fairly clean")







################################################################################################################ Address


TotalNumberAddress=len(myDataFrame["Address"])                                          #I am using the same logic as above, to find the total number of rows for Address, to find the number of every row with values, and the fraction of missing values
print("\n\nThe total number of the rows of Address is")
pprint(TotalNumberAddress+1)
                                                                            
EveryRowAddressWValues=myDataFrame['Address'].notnull().sum()                         
print("\n\nThe number of the rows with values in the City or County is")
pprint(int(EveryRowAddressWValues)+1)

print("\n\nThen the number of missing values is")                      
pprint((TotalNumberAddress+1)-(int(EveryRowAddressWValues)+1))                   

print("\n\nThe fraction of missing values for Address")
pprint(((TotalNumberAddress+1)-(int(EveryRowAddressWValues)+1))/(TotalNumberAddress+1))       


print("\n\nFor this attribute, We have lots of missing values")



Count=0                                                                            #trying to count the number of noise values
i=0                                                                                #I figured that the type of Address is string 
                                                                                   #so if one of the row of the column contains something other than the type string, that row contains a noise.
                                                                                   
FrameCity=myDataFrame["City or County"]                                               #I created another variable assigned the column
for j in range(1,(len(FrameCity))):                                                  #for j in range of 1 and the length of the column
    if type(FrameCity[i])==type(FrameCity[j]):                                         #If the type of frameID[i] is equal to the next row, pass
            pass
    if type(FrameCity[i])!=type(FrameCity[j]):                                         #If the type of frameID[i] is not equal to the next row, then add 1 to the count
            Count+=1

print("\n\nThe number of noise values is")
print(Count)

#the fraction of noise values for this attribute is 0. 

print("\n\nAddress is fairly clean")







################################################################################################################ '# killed'


TotalNumberKilled=len(myDataFrame['# killed'])                                          #I am using the same logic as above, to find the total number of rows for Address, to find the number of every row with values, and the fraction of missing values
print("\n\nThe total number of the rows of # killed is")
pprint(TotalNumberKilled+1)
                                                                            
EveryRowKilledWValues=myDataFrame['# killed'].notnull().sum()                         
print("\n\nThe number of the rows with values in the City or County is")
pprint(int(EveryRowKilledWValues)+1)

print("\n\nThen the number of missing values is")                      
pprint((TotalNumberKilled+1)-(int(EveryRowKilledWValues)+1))                   

print("\n\nThe fraction of missing values for # killed")
pprint(((TotalNumberKilled+1)-(int(EveryRowKilledWValues)+1))/(TotalNumberKilled+1))       


Count=0                                                                            #trying to count the number of noise values
i=0                                                                                #I figured that the type of # killed is numpy.int64 
                                                                                   #so if one of the row of the column contains something other than the type string, that row contains a noise.
                                                                                   
FrameCity=myDataFrame['# killed']                                               #I created another variable assigned the column
for j in range(1,(len(FrameCity))):                                                  #for j in range of 1 and the length of the column
    if type(FrameCity[i])==type(FrameCity[j]):                                         #If the type of frameID[i] is equal to the next row, pass
            pass
    if type(FrameCity[i])!=type(FrameCity[j]):                                         #If the type of frameID[i] is not equal to the next row, then add 1 to the count
            Count+=1

print("\n\nThe number of noise values is")
print(Count)

#the fraction of noise values for this attribute is 0. 

print("\n\n# killed is fairly clean")





################################################################################################################ '# injured'


TotalNumberInjured=len(myDataFrame['# injured'])                                          #I am using the same logic as above, to find the total number of rows for Address, to find the number of every row with values, and the fraction of missing values
print("\n\nThe total number of the rows of # injured is")
pprint(TotalNumberInjured+1)
                                                                            
EveryRowInjuredWValues=myDataFrame['# injured'].notnull().sum()                         
print("\n\nThe number of the rows with values in the City or County is")
pprint(int(EveryRowInjuredWValues)+1)

print("\n\nThen the number of missing values is")                      
pprint((TotalNumberInjured+1)-(int(EveryRowInjuredWValues)+1))                   

print("\n\nThe fraction of missing values for # injured")
pprint(((TotalNumberInjured+1)-(int(EveryRowInjuredWValues)+1))/(TotalNumberInjured+1))       


Count=0                                                                            #trying to count the number of noise values
i=0                                                                                #I figured that the type of # killed is numpy.int64 
                                                                                   #so if one of the row of the column contains something other than the type string, that row contains a noise.
                                                                                   
FrameCity=myDataFrame['# injured']                                               #I created another variable assigned the column
for j in range(1,(len(FrameCity))):                                                  #for j in range of 1 and the length of the column
    if type(FrameCity[i])==type(FrameCity[j]):                                         #If the type of frameID[i] is equal to the next row, pass
            pass
    if type(FrameCity[i])!=type(FrameCity[j]):                                         #If the type of frameID[i] is not equal to the next row, then add 1 to the count
            Count+=1

print("\n\nThe number of noise values is")
print(Count)

#the fraction of noise values for this attribute is 0. 

print("\n\n# injured is fairly clean")


################################################################################################################ Feature Generation

NSList=[]                   #create an empty list
NorthernState=["Connecticut", "Illinois", "Indiana", "Iowa", "Kansas", "Maine", "Massachusetts", "Michigan", "Minnesota", "Missouri", "Nebraska", "New Hampshire", "New Jersey", "New York", "North Dakota",
               "Ohio", "Pennsylvania", "Rhode Island", "South Dakota", "Vermont", "Wisconsin"] #The list that contains northern states

DataState=myDataFrame['State']          #I assignged the column to anothern name

for i in range(0,len(myDataFrame['State'])):      #for i between 0 and the length of the column
    if DataState[i] in NorthernState:               #if the rows of the column state contains one of the northernstate list
        NSList.append(1)                            #append 1 in the NSList
    else:
        NSList.append(0)                            #otherwise 0 in the NS List

NSDataFrame=pd.DataFrame(NSList)                #turning the list into pandas dataframe
NSDataFrame.columns=["North/South"]             #with the header North/South

myDataFrame=pd.concat([myDataFrame,NSDataFrame], axis=1, join='inner')  #concatenate the existing mydataframe and the NSDataFrame





EWList=[]               #I am using the same method for Eastern and western states
EasternState=["Maine", "Vermont", "New Hampshire", "Massachusetts", "Connecticut", "Rhode Island", "New York", "New Jersey", "Pennsylvania", "Delaware",
              "Maryland", "West Virginia", "Virginia", "North Carolina", "South Carolina", "Georgia", "Florida", "Alabama", "Mississippi", "Tennessee", 
              "Kentucky", "Illinois", "Indiana", "Ohio", "Michigan", "Wisconsin"]

DataState=myDataFrame['State']

for i in range(0,len(myDataFrame['State'])):
    if DataState[i] in EasternState:
        EWList.append(1)
    else:
        EWList.append(0)

EWDataFrame=pd.DataFrame(NSList)
EWDataFrame.columns=["East/West"]

myDataFrame=pd.concat([myDataFrame,EWDataFrame], axis=1, join='inner')



FivePeople=[]                           #I created an empty list with the name of five people
DataKilled=myDataFrame["# killed"]       #I assigned the column # killed to another name
DataInjured=myDataFrame["# injured"]      #I assigned the column # injured to another name

for i in range(0,len(myDataFrame["# killed"])):    #for i between 0 and the length of the column
    if DataKilled[i]+DataInjured[i]<5:             #if the sum of the number of killed and the number of injured is less than 5
        FivePeople.append(0)                        #append 0 into the fivepeople list
    else:
        FivePeople.append(1)                        #otherwise append 1 into the fivepeople list
        
FivePeopleData=pd.DataFrame(FivePeople)             #turning the list into pandas dataframe
FivePeopleData.columns=["More than 5 people"]       #with the header

myDataFrame=pd.concat([myDataFrame, FivePeopleData], axis=1, join='inner') #concatenate the existing mydataframe and the FivePeople

print(myDataFrame)

#myFileName="ChildrenKilled_Clean.csv"
#myDataFrame.to_csv(myFileName,mode='w', index=False)





















