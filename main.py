import json 
from tabulate import tabulate
def bodyindex(bmi,height):
    return bmi/height

class List(list):
    def push(self, x):
        self.append(x)

def healthrisk(x):
    if (x<=18.4) :
         return "Malnutrition risk"
    elif(x<=24.9) :
         return "Low risk"
    elif(x<=29.9):
         return "Enhanced risk"
    elif(x<=34.9) :
         return "Medium risk"
    elif(x<=39.9) :
         return "High risk"
    else :
         return "Very high risk"
  
def category(x):
    if (x<=18.4) :
         return "Underweight"
    elif(x<=24.9) :
         return  "Normal weight"
    elif(x<=29.9):
         return "Overweight"
    elif(x<=34.9) :
         return "Moderately obese"
    elif(x<=39.9) :
         return "Severly obese" 
    else :
         return "High risk"

myTable = []

def main1():
    jsonstrings = ['{"Gender":"Male","WeightKg":60,"HeightCm":10}',
    '{"Gender":"Male","WeightKg":460,"HeightCm":20}',
    '{"Gender":"Male","WeightKg":160,"HeightCm":30}',
    '{"Gender":"Male","WeightKg":260,"HeightCm":40}',
    '{"Gender":"Male","WeightKg":160,"HeightCm":50}']
    for jsonstring1 in jsonstrings:
        jsonobject = json.loads(jsonstring1)
        mass  = jsonobject.get('WeightKg')
        height  = jsonobject.get('HeightCm')
        bmi= mass/height
        arr=[]
        arr.append(bmi)
        arr.append(category(bmi))
        arr.append(healthrisk(bmi))
        myTable.append(arr)

main1()
print(tabulate(myTable))


import json 
from tabulate import tabulate
import numpy as np

def bodyindex(bmi,height):
    return bmi/height

class List(list):
    def push(self, x):
        self.append(x)

def healthrisk(x):
    if (x<=18.4) :
         return "Malnutrition risk"
    elif(x<=24.9) :
         return "Low risk"
    elif(x<=29.9):
         return "Enhanced risk"
    elif(x<=34.9) :
         return "Medium risk"
    elif(x<=39.9) :
         return "High risk"
    else :
         return "Very high risk"
  
def category(x):
    if (x<=18.4) :
         return "Underweight"
    elif(x<=24.9) :
         return  "Normal weight"
    elif(x<=29.9):
         return "Overweight"
    elif(x<=34.9) :
         return "Moderately obese"
    elif(x<=39.9) :
         return "Severly obese" 
    else :
         return "High risk"

myTable = []


data = ['{"Gender":"Male","WeightKg":60,"HeightCm":10}']
 

def main1(jsonstrings):
    for jsonstring1 in jsonstrings:
        jsonobject = json.loads(jsonstring1)
        mass  = jsonobject.get('WeightKg')
        height  = jsonobject.get('HeightCm')
        bmi= mass/height
        arr=[]
        arr.append(bmi)
        arr.append(category(bmi))
        arr.append(healthrisk(bmi))
        myTable.append(arr)
    return myTable
main1(data)

print(myTable)
table= [[6.0, 'Underweight', 'Malnutrition risk']]
print(tabulate(myTable))
print(np.array_equal(table,myTable))
