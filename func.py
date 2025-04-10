#Code Challenge 1
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
# def game():
    # score=0
    # Name=input('Your Nickname:')
    # print('Hey',Name,'Welcome to our Quiz Game')
    # Question1=input('1. Is python a markup language?')
    # if(Question1=='no'):
    #     print('Brilliant mind Tech guru')
    #     score +=1
    # else:
    #     print('Wrong answer,Python is a programming language')
    #     #question2
    # datatype=['integer','string','float','boolean','list']
    # print(datatype)
    # Question2=input('2. Which of the above is not a data type:')
    
    # if(Question2=='list'):
    #     print('Brilliant mind')
    #     score +=1
       
    # else:
    #     print('No,list is not datatype')
    # Question3=input('python is very simple language and enjoyable,right?')
    # if(Question3 == 'yes'):
    #     print('Good answer,all you gotta do is to have a positive mindset')
    #     score +=1
    #     print('Your scored:',score)
    # else:
    #     print('Wrong,just learn to understand the basics')
    #     print('You scored:',score)
# game()
def greet(name):
    print( f'Hello {name},hope you are doing fine')
greet('jane')