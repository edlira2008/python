
fruits = ['molla', 'banane', 'dredhz','portokall']
fruits.append('kivi')
print(fruits)
#bashkon ni element ne fund te listes
print('-------------'*6)

#data structure
t1 = (3,3,3,5,6,7,0)
print(t1)
s1= {3,43,3,3,3,5665,7,54}
print(s1)
d1 = {'edlira':18, 'aid':17}
print(d1['edlira'])
print(type(d1['aid']))

print('------------------------------------------')
students = ['edlira','aid','zahir', 'qefsere']
for student in students:
    print(student)
print('--'*6)
print(students.index('aid'))

print("=----------------------------------------------p")
#t

from typing import Dict,List
pcs:Dict[int,'str'|List[str]]={1:'dell',
                                               2:'hp',
                                               3:'acer',
                                               4:'samsung',
                                               5:'lenovo',
                                               6:['lg','bga','hdmi']
                                               }
for key,value in pcs.items():


    if isinstance(value,list):

        for brand in value:
         print(f"per  pcs {key} brandi i ti eshte: {brand} ")
    else:
         print(f"per pcs {key} brandi i tij eshte: {value}")
