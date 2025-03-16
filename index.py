print("Hello World, Welcome to expertise transformation of Daphine")
#python basics

#variables > memory storage
#Data types
name="Daphine Nekesa,a Data Analyst and a manager"
age= 22
height= 5.6
female =True
 
print("Hello" ,name, "are you okay")
print("How old are you?",age,"Your height:",height,female,"intelligent and pretty")


#list uses [] only,its like a shopping list
languages=['python','java', 'java','Javascript','C',20,True]

print(type(languages))
languages.append('react')
languages.remove(True)

print(languages)

#sets uses {} and doesn't allow repetition,it only pick 1 number
age={21,28,30,35,21,21,'daphine','Nekesa'}
age.add('Nekesa')
print(age)
age.discard('daphine')
print(age)




#dictionaries uses {}
Sneakers={"black":"converse","grey":"converse","white":"J4"}
Name ={
    'fname':'Elosy Karimi',
    'sname':'Daphine Nekesa',
    'tname':'Millicent Gacheri'
}
print(Name)

print(Sneakers)
#tuples use () only
Age=(20,12,23,34)
print(type(Age))
