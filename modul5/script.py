
def greet(emri):
    print(f'hello {emri}')

student1='drini'
students=['drini','edliraa','ernesi','olti']

for student in students:
    greet(student)


print('------'*3)

def power(nr,pow):
    return nr**pow

result =power(pow=3, nr=5) #implicite
print(result)

#kur ekena funksionin me RETURN e bojna qi tmnyr gjith per me ekzekutu
#detyra me fuqi psh 5 ne 3

def rectangle_area(a:float,b:float)->float:
    area = a*b  #ska scope jashte funksionit
    return round(area,2)

print('siperfaqja e drejtekndeshit eshte:', rectangle_area(10.0 , 4.5),"njesi katrore")


def circle_area(radius):
    global pi #global ka scope dhe jashte funksionit
    pi = 3.14
    return pi*(radius**2)

rrethi1=circle_area(10.33)
print('vlera e konstantes pi eshte: ', pi)
print(rrethi1)



#vlera by default perdoret veq ne rastet ku nuk i dhurojna argument

#detyra

def fuqi(i:int,pow:int)->int:
    return i**pow

rezultati = fuqi(pow=2, i=19)
print(rezultati)


def mbledhja(x,y):
    return x+y
rezultati = mbledhja(5,66)
print(rezultati)