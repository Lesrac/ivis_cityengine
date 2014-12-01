'''
Created on Nov 24, 2014

@author: sschubiger
'''
from scripting import *

import csv

# get a CityEngine instance
ce = CE()

states = {}

if __name__ == '__main__':
    f = open('/Users/Daniel/CityEngine/ivis/data/age.csv', 'rt')
    try:
        reader = csv.reader(f)
        for row in reader:
            try:
                states[float(row[1])] = row
            except ValueError:
                pass
    finally:
        f.close()
            
    for state in ce.getObjectsFrom(ce.getObjectsFrom(ce.scene, ce.withName('Kantone'))[0]):
        row = states[ce.getAttribute(state, 'KTNR')]
        print row[0]
      #  pop = []
        pop = 0
        pip = 0
        kip = 0
        for i in range(0,18):
            pop += float(row[i+3].replace(',',''))
        for i in range(18,65):
            pip += float(row[i+3].replace(',',''))
        for i in range(65,101):
            kip += float(row[i+3].replace(',',''))
        ce.setAttribute(state, "YOUNGEST", pop)
        ce.setAttributeSource(state, "YOUNGEST", "OBJECT")
        ce.setAttribute(state, "WORKINGPARTY", pip)
        ce.setAttributeSource(state, "WORKINGPARTY", "OBJECT")
        ce.setAttribute(state, "SENIORS", kip)
        ce.setAttributeSource(state, "SENIORS", "OBJECT")
        ce.setAttribute(state, "TOTALPOP", float(row[2].replace(',','')))
        ce.setAttributeSource(state, "TOTALPOP", "OBJECT")