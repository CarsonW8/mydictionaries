"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $50,000


can use json file in python and convert it into a list using []
naia conference number football must match with the number of the data given to use, use to figure it out
"""
import json

infile = open('school_data.json', 'r')

schools = json.load(infile)
#taking school data json file and loading it into an object called schools (a list)
conference_schools = [372,108,107,130]
print(len(schools))
#can find out we have 649 total schools

#school is a dictionary
for school in schools:
    #can also do - for i in conference_Schools and then if i == school['NCAA']['NAIA conference number football (IC2020)']
    if school['NCAA']['NAIA conference number football (IC2020)'] in conference_schools:
        if school['Graduation rate  women (DRVGR2020)'] > 75:
            print(f"University: {school['instnm']}")
            print(f"Graduation Rate for Women: {school['Graduation rate  women (DRVGR2020)']}%\n")
for school in schools:
    if school['NCAA']['NAIA conference number football (IC2020)'] in conference_schools:                        #!= None is the same as not even putting it there
        if school['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)'] != None:
            if school['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)'] > 50000:
                print(f"University: {school['instnm']}")
                print(f"Total price for in-state students living off campus: ${school['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)']:,}\n")