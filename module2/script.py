from typing import Dict,List
#paket e gatshme
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


example='PythonListMethodsExplained'
example=example.lower()
count:[str,int]={}
for char in example:
    if char not in count.keys():
        count[char]=1
    else:
        count[char]+=1
print(count)
print(count.get('d'))
print(pcs.items())


qytetet:List[str|int]=['Prishtina','Elementi nr.33', 'New York', 'Prizreni','Tirana', 'Shkupi']
print(qytetet.index('Prizreni'))
qytetet.append("Tirana")
#bashkangjet qit element apet nfund tlistes

for i in range(5):
    qytetet.append(f"Elementi nr,{i}")

print(qytetet)
print(qytetet.count(f"Elementi nr.33"))
qytetet.insert(0,5)
print(qytetet)



