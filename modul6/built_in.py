import os#operatinhg system
import json #java script object nmotation
import datetime # ak te beje me daten dhe kohen
import re #regular expression
#paketaq te gatshme ne pyton

print(os.path.isfile('..module1.py'))
for item in os.listdir('./.'):
    if os.path.isfile(f'./{item}'):
        print(item)

print(datetime.date.isoweekday(datetime.date.today()))
print(re.search('[a-zA-Z0-9]','sot osht e marte'))