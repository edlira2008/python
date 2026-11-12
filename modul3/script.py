a_list=list([3,4,5,6,7,])
xyz=[24.234,234,235]


my_set={1,2,3}
if isinstance(my_set,set):
    print('this is a set')

other_set=set(['orange','pear','apple'])

other_set=set(xyz)
print(other_set)

#unioni e ben bashkimin e elementeve
#metod per set
union_result=other_set.union(my_set)
union_result_2=my_set | other_set
print(f"Union function: {union_result_2 | union_result}")

#prerja bashkon elementet e njejta  / intersect
intersect_result = other_set.intersection(my_set)
intersect_result_sign = other_set & my_set
print(f"Intersect function: {intersect_result_sign}")


#diferenca i dalon elementet e bashksive
set_difference=union_result.difference(my_set)
print(f"Difference between {union_result} and {my_set} is: {set_difference}")
sign_difference=union_result -my_set
print(sign_difference==set_difference)
#njejt si - njejt si difference me fjal e sjell rezultatinn e njejt



list1 = ['red', 'green', 'blue', 'black']
list2  = ['orange', 'white', 'yellow', 'black']


set1=set(list1)
set2=set(list2)
unique_set = set1 | set2
print(unique_set)



