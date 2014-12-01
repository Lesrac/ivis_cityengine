'''
Created on Nov 24, 2014

@author: sschubiger
'''
from scripting import *

import csv

# get a CityEngine instance
ce = CE()

states = {}
suiss = {}
counter = 0

if __name__ == '__main__':
    f = open('/Users/Daniel/CityEngine/ivis/data/age.csv', 'rt')
    try:
        reader = csv.reader(f)
        for row in reader:
            try:
                if counter == 0 :
                    counter += 1
                elif counter == 1:
                    counter += 1
                    suiss[0] = row
                else:
                    states[float(row[1])] = row
                    counter += 1
            except ValueError:
                pass
    finally:
        f.close()
            
    for ch in ce.getObjectsFrom(ce.getObjectsFrom(ce.scene, ce.withName('Schweiz'))[0]):
        row = suiss[0]   
        pop = 0
        pip = 0
        prop = 0
        kip = 0
        for i in range(0,18):
            pop += float(row[i+3].replace(',',''))
        for i in range(18,49):
            pip += float(row[i+3].replace(',',''))
        for i in range(49,68):
            prop += float(row[i+3].replace(',',''))
        for i in range(68,101):
            kip += float(row[i+3].replace(',',''))
        ce.setAttribute(ch, "YOUNGEST", pop)
        ce.setAttributeSource(ch, "YOUNGEST", "OBJECT")
        ce.setAttribute(ch, "WORKINGPARTY", pip)
        ce.setAttributeSource(ch, "WORKINGPARTY", "OBJECT")
        ce.setAttribute(ch, "BABYBOOMER", prop)
        ce.setAttributeSource(ch, "BABYBOOMER", "OBJECT")
        ce.setAttribute(ch, "SENIORS", kip)
        ce.setAttributeSource(ch, "SENIORS", "OBJECT")
        ce.setAttribute(ch, "TOTALPOP", float(row[2].replace(',','')))
        ce.setAttributeSource(ch, "TOTALPOP", "OBJECT")
        
            
    for state in ce.getObjectsFrom(ce.getObjectsFrom(ce.scene, ce.withName('Kantone'))[0]):
        row = states[ce.getAttribute(state, 'KTNR')]
        pop = 0
        pip = 0
        prop = 0
        kip = 0
        for i in range(0,18):
            pop += float(row[i+3].replace(',',''))
        for i in range(18,49):
            pip += float(row[i+3].replace(',',''))
        for i in range(49,68):
            prop += float(row[i+3].replace(',',''))
        for i in range(68,101):
            kip += float(row[i+3].replace(',',''))
        ce.setAttribute(state, "YOUNGEST", pop)
        ce.setAttributeSource(state, "YOUNGEST", "OBJECT")
        ce.setAttribute(state, "WORKINGPARTY", pip)
        ce.setAttributeSource(state, "WORKINGPARTY", "OBJECT")
        ce.setAttribute(state, "BABYBOOMER", prop)
        ce.setAttributeSource(state, "BABYBOOMER", "OBJECT")
        ce.setAttribute(state, "SENIORS", kip)
        ce.setAttributeSource(state, "SENIORS", "OBJECT")
        ce.setAttribute(state, "TOTALPOP", float(row[2].replace(',','')))
        ce.setAttributeSource(state, "TOTALPOP", "OBJECT")