from typing import Dict,List

from modul3.script import union_result, intersect_result

pcs:Dict[int,'str'|List[str]]={3:'Lenovo',
                               4:'HP' ,
                               5:['msi','Dell']
                               }
for key,value in pcs.items():


    if isinstance(value,list):
        #check per kushtin e dhene ne argumente

        for brand in value:
            print(f"Per pc nr.{key}, eshte brandi: {brand}")
    else:

        print(f"Per pc nr.{key}, eshte brandi: {value}")


from typing import Dict,List
kompjutera: Dict['str',int | List['str']] = {
    'lenovo':1,
    'hp':2,
    'samsung':3,
    'acer':4,
    5: ['dell','msi','asus']
}
for key ,value in kompjutera.items():

       if isinstance(value,list):
           for brand in value:
               print(f"nr of pcs is {key} and brand is {brand}")
       else:
               print(f'nr of pcs is {key} and brnd is {value}')



from typing import Dict

students: Dict[int,'str'] = {
     1:'edlira kastrati',
     2:'aid plakolli',
     3:'jona kastrati',
     4:'qefsere dobratiqi',
    5:'zahir kasrati'
 }
print('-----------------------------------------------------------')

for key,value in students.items():
    print(f'Nxenesi nr.{key} eshte {value}')

print('-----------------------------------------------------------')


qytetet = ['obiliq','prishtina','vushtrri','peja','prizreni',
                          'ferizaj','gilan','gjakov']

print(qytetet)
qytetet.append('edlira')
print(qytetet)
(print(qytetet.index('gjakov')))
qytetet.insert(2,'jona')
print(qytetet)

print(qytetet.count('edlira kastrati'))
print('--------------------------------')

s1 = {1,2,3,4}
if isinstance(s1,set):
   print('this is set')

other_set ={1,2,34,3,2008 ,2009}



union_result = s1 | other_set
print(union_result)


intersect_results = s1.intersection(other_set)
intersect_results =  s1 & other_set
print(intersect_results)

set_difference = other_set.difference(s1)
result_difference = other_set - s1
print(result_difference)


age = 18

if age > 18:
    print('over 18 ')
elif age ==18:
    print('ur uqual')
else:
    print('minor')



city = True
color= 'red'

if color != 'yellow' and city is True:
    print('ur right')
elif color !='black' and city is False:
    print('ur wrong')

else:
    print('out of conent')

#conditionals


for age in range(100):
    print('age')

