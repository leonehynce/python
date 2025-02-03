# list datastructure
# list are mutable
# lists are orderd
# lists are indexed
fruits=['apples','banana','mangoes','orange','pear','strawberry']
print(fruits)
fruits[0]="watermelon"
numbers=[1,2,3,4,5,6,7,8,9]
numbers2=[67,5,5-7,0,13,5,1,23,3,-5,-4]
print(f"i love eating {fruits[0]}")
print(numbers)
numbers.append(11)
print(numbers)
numbers2.sort(reverse=True)
print(numbers2)
print("sum=",sum(numbers2))
# tuples are immutable(unchangable)
# tuple datastructure
# tuples are ordered
# tuples are indexed
cars=('audi','toyota','subaru','honda',)
print(cars)

nambari=(43,5,87,2,1,-3,-9,-100,-2345,9,1,0)
print(nambari)
# nambari.sort()
print(sorted(nambari))
print(nambari)
# set datastructure
# set are unorderd
# set are not indexed
computers={'hp','dell','asus','apple','lenovo',}

computers.add('ibm')
computers.remove('asus')
print(computers)
num1={1,2,3}
num2={4,6,7}
union_set=num1.union(num2)
print(union_set)
# cars[0]="bmw"
# print(cars)
# dictionary data structures
student={'name':'hynce','age':'19','gender':'male','location':'Nairobi'}
print(f"student name:{student['name']}")
print(f"student age:{student['age']}", f"student gender :{student['gender']}", f"students location:{student['location']}")
