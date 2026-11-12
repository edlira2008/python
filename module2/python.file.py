words=('spam', 'sausages', 'eggs')
words[2]='meat'
#se supporton se osht taple edh immutable

words=('spam', 'sausages', 'eggs')
print(words.index('sausages'))
print(words.count('spam'))
#count i numron sa psh sausages i kena mrena

#taple i ka dy funksione veq count edhe index


#set osht unike dhe e sortume/bashkesi albania
x={"3",4,5,6,False , False}
print(x)
print(type(x))


student={1:{'emri':'Lirak', 'mosha':23, 'student':False},
         2:{'emri':'Edlira', 'mosha':17, 'student':False}}

#
for key,val in student.items():
     for k,v in val.items():
         print(f"Studenti me id{key}, {k}:{v}")


