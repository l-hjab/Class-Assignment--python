# #1. empty list
# my_list=[]

# #2. appending value to the empty list
# my_list.append()
# my_list.append(20)
# my_list.append(30)
# my_list.append(40)
# print(my_list)
#3. adding  15 to the second position in the my_list
# my_list.insert(1,15)
# #position 15 to the second position of the list
# print(my_list)

# #4.creating extending my_list with another list
# new_list=[50,60,70]
# my_list.extend(new_list)
# print('Extended list is:',my_list)

# #5.removing the last element
# my_list.remove(70)
# print(my_list)

# #6. list in ascendiing order
# my_list.sort()
# print('The list in ascendig order',my_list)

# # 7. finding index number 30
# print('The index oof 30 is :',my_list.index(30))

#comprehesion list
#traditional way
# squares=[]
# for x in range(5):
#     squares.append(x**2)
#     print(squares)

#list compehension
# squares=[x**2 for x in range(5)]
# print( squares)

#helps with with upper case 
result=[ x for x in range(10)]
print(result)

names=['Bundi','John','Morris','Elsie']
result=[ name.lower() for name in names]
print(result)

names=['mangoes','apples','strawberries']
list=[fruit.upper() for fruit in names]
print(list)