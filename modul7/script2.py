#type casting


nr=int('42')
print(type(nr))

print(str(False))

print(bool(21))

#z-int('8abesd87637') nuk funksionon
print(type(float('52.5')))

name=input("enter ur name:\n")
age=int(input(f'enter ur age mr.ms. {name}:\n'))
print(age)



#error handling
try:
    print(50/0)
except ZeroDivisionError as e:
    print('ka ndodhur nje gabim gjate ekzekutimit')

try:
    with open('./script.py') as o:
      result=o.readlines()
      print(result)
except FileNotFoundError as e:
    print('file nuk u gjet')
finally:
    o.close()
