def calc(num1,num2):
    sum= num1 + num2
    sub=num2 - num1
    multi=num1 * num2
    division= num2 / num1
    modulus = num2 % 2

    print("The sum is :",sum)
    print("The minus is :",sub)
    print(multi)
    print(division)
    print(modulus)  
calc(10,20)

name=input("Your First name:")
print("Hello",name),"i hope you're doing good"
lang=input("Do you love coding?")
if(lang=='Yes'):
    print('Thats good',name,'then, lets play the game!')
    print("1.Let me cheer up your day a little bit ,with some codind jokes")
    joke1="1.Do you know that the first time as a IT student i didn't know how to turn on a computer?😂"
    joke2="2.I used to cram codes so that i can just be good at it😢😢,pretty sad"
    joke3="3.When I was creating my first website,I  actually coped everything😂😂🤣 the youtube guy was writing(javascript code) and i ended up having errors🤦‍♀️"
    joke4="4.This ain't a joke but this time i'm going to create an amazing project because i understand everything❤😜,"
    joke5="No cramming and nothing to loose for trying"


    print(joke1,"who does that?🤣😂🤣😎")
    print(joke2,'so sad')
    print(joke3,'pretty lame')
    print(joke4,'issa promise')

    joka=input('Which joke made your day?')
    if(joka==joke1):
        print("Thanks",name,'but i hope it never happened to you')
    elif(joka==joke2):
        print("i know you have tried that too",name)
    elif(joka==joke5):
        print("Just beleive my words",name)
    else:
        print(joke5,',,Thanks',name)
   
else:
    print("Okay",name,"Have a good time")






