city={'Kenye':'Nairobi','Uganda':'Kampala','South Africa':'Cape Town'}
print(city)
city['Nigeria']='Lagos'
city['France']='Paris'
print(city)
del city['Uganda']
print('Updated list',city)

for i in city:
    print(i)
print(city['Kenye'])

#set
Id={12,32,34,12,43,23}
print(Id)
Id.discard(43)
print(Id)
#empty set
empty_set= set ()
empty_set.add(20)
empty_set.add(30)
empty_set.add(40)
empty_set.add(50)
print(empty_set)
#update method of list to set
names=['john','jane','doe']
empty_set.update(names)
print(empty_set)
#count numbers in a set
even_numbers={2,4,5,7,6,8,10}
print(len(even_numbers))
      
    #union in Sets A|B(unite)
set1={2,3,4,5}
set2={7,8,9,0}
print('The union is:',set1 |set2)
print('Second way of union:',set1.union(set2))

#set intersection displays common items betweeen A and B A&B
set1={2,3,9,7}
set2={7,8,9,0}
print('interset', set1 & set2)
print('Second way of intersect:',set1.intersection(set2))

name={'Mikinduri':'Douglas','Equator':'Dyna','Kariene':'Peter','Kiangondu':'Michael'}
print(name)

#adding morris to the list
name ['Weru']='Morris'
print(f'Another buying center was added {name}')

#changing the value of equator from dyna to nancy
name ['Equator']='Nancy'
print(name)

#deleting an item from the dictionary
del name['Mikinduri']
print(name)


