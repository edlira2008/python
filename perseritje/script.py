from dis import print_instructions

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

kompjutera: Dict[int,'str'] |  List['str'] = {1:'dell',
                                               2:'hp',
                                               3:'acer',
                                               4:'samsung',
                                               5:'lenovo',
                                               6:['lg','bga','hdmi']
                                               }
for key,value in kompjutera.items():


    if isinstance(value,list):

        for brand in value:
         print(f"per  kompjuerin {key} brandi i ti eshte: {brand} ")
    else:
         print(f"per kompjuterin {key} brandi i tij eshte: {value}")


qytetet:List[str|int] = ['peja','prizsreni','obiloiq','shkup','berat']
print(qytetet)
qytetet.append('shkoder')
print(qytetet)
print(qytetet.index('prizsreni'))




for i in range(100):
    print('i love u ')

for i in range (101):
     print(i)


def mbledhja(x,y):
    return x/y

rezultati = mbledhja(45,5)
print(rezultati)


word ="computer works for us"

for c in word:
    print(c)


mosha = 18

if mosha != 18:
    print(f'ur not 18')
elif mosha ==18:
    print(f"ur 18")
else:
    print('u are so minor for this show!')

nails =['french','solid','cateye','ombre']
print(nails)
print(nails.count('red_nails'))

list = ['edlira','edlira','edlira','error', 'edlira','error']

print(list)