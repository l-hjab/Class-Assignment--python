#creating a class
class Books:
    #constructors
    def __init__(self,money,fiction):
        self.money=money
        self.fiction=fiction

#inheritance
class name1(Books):

    def description(self):
        print('The pychology of Money') 

class name2(Books):

    def description(self):
        print('The Silent Patient')


#creating object
book_l = name1('Pyschology of Money','Knowledge')
book_2 = name2('The Silent Patient','Fiction')
# print(f'Interesting 1st book is : {nove2.name},and it is a {nove2.type}')
# print(nove2.type)
# print(novel.name,novel.type)

# polymorphism
for novels in (book_l,book_2):
    novels.description()

# Activity 2
class Animals:
    def __init__(self,type,legs):
        self.type=type
        self.legs=legs
        
class cat(Animals):
     
     def move(self):
         print('A cat moves by walking')

class eagle(Animals):

    def move(self):
        print('A bird moves by flying')

Animal1=cat('Animal',4)
Animal2=eagle('Bird',2)

print(f'An {Animal1.type} has {4} legs, while A {Animal2.type} has {2} legs with 4 wings')

#polymorphism
for movement in (Animal1,Animal2):
    movement.move()

