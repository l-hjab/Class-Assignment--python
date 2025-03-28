import random
# def jokes():
#     list=['Tall','Dark','Handsome','Rich','Smart']
#     list2=['brayo','jose','dylan','garvin']
#     list.append(list2)
#     list2.sort()
   
# jokes()
# #function
# def name(fname,lname):
#     print('Hello',fname,'',lname)
# name('jane','doe')

# #game1
# username=input("Enter Your Name:")
# color=input("What's your favorite color?")
# print('Hello', username,'Your favorite color is:',color)

#game2 jokes generator
joke=[
    'I skipped game 2 because i gorra think about it',
    'At first i used to cram code so that i can feel like a pro',
    'Python is really fascinating and am falling in love with the learning',
    'Stop scrolling and Go to bed you son of a bitch'
]
print(random.choice(joke))

#game3 Quiz game
def game():
    Name=input('Your Nickname:')
    print('Hey',Name,'Welcome to our Quiz Game')
    Question1=input('1. Is python a markup language?')
    if(Question1=='No'):
        print('Brilliant mind Tech guru')
    else:
        print('Wrong answer,Python is a programming language')
    datatype=['integer','string','float','boolean','list']
    print(datatype)
    Question2=input('2. Which of the above is not a data type')
    
    if(Question2=='list'):
        print('Brilliant mind')
    else:
        print('No,list is not datatype')
    
game()