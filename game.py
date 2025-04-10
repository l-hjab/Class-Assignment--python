# write a program that accepts user input to create a list ,then compute the sum
# of all the integers in the list

# salary=int(input('How much do you earn per month?:'))
# allowance=int(input('Your House Allowance per monthly?:'))
# others=int(input('Transport Cost?:'))
# #adding the user input to the total list using extending method of another list 
# t_amount=[salary , allowance , others]
# print(t_amount)
# print('Total money earned is :Kshs',salary + allowance + others)

#challenge 2
# create a tuple containing the names of the five of your favorite books.then
# use the loop to print each book name on a separate line
# import random
# books=('Pychology of Money','The Silent Patient','Married to the Devils Son','Why Men Marry Bitches','The Alchemist')
# print('My First Fav is:',random.choice(books))
# print(type(books))
# for i in books:
#     print(i)
# love='Good Night Daphine😉🌹,am so proud of you, you are very smart and So beautiful💋😜'
# print(love,'I love you so much❤❤')
# print('Dont ever be scared because you can do it.am gonna get you a bouquet of roses')

#challenge 3
# age=int(input('Enter Your Age:'))
# sibling_age=int(input('Enter Age of your sibling:'))
# sibling_age1=int(input('Enter Age of your sibling:'))
# sibling_age2=int(input('Enter Age of your sibling:'))
# #set1
# total_age=set ()
# total_age.add(age)
# total_age.add(sibling_age)
# #set 2
# age2=set()
# age2.add(sibling_age1)
# age2.add(sibling_age2)

# print('Set 1',total_age)
# print('Set 2',age2)
# print('intersect:', total_age & age2)

# for i in range(1,10):
#     print(i)

#challenge 4
# write a program that accepts user uses a dictionary to store information about a 
# such as their name, age and favorite color.Ask the user for input and store the informationin the dictinary
# then print to the console

# infor={}
# # print(type(infor))
# name=input('Enter Your Name:')
# age=int(input('How old are You?:'))
# color=input('What is your favorite color?:')
# infor['Name']=name
# infor['Age']=age
# infor['Favorite-Color']=color
# print(infor)
# infor['Favorite-Color']='Mustard'
# print(infor)

#challenge 5
# create a program that stores a list of words.Then ,user list comprehension to create
# a new list that contains only the words that have an odd number of characters
word=['Hey','Hello','Hi','hawayu','imma','gorra']
Updated_words=[x for x in word if len(x) % 2!= 0  ]
print(Updated_words)

