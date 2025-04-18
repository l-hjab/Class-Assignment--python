#defining a class
# class Project:
#     type='Dashboard'
#     Tool='Power BI'

#     #method
#     def analysis(self):
#         print('Dashboard for Raw Mac Nuts')

# #creating an object
# Data_analysis=Project()
# print(Data_analysis.type,Data_analysis.Tool)
# Data_analysis.analysis()

# # class 2
# class Recipe:
#     color='pink'
#     size='large'

#     def describe(self):
#         print('A four layered structured vanilla cake')

# Cake=Recipe()
# print('The color of cake should be',Cake.color)
# Cake.describe()

# #Constructor
# class House:
#     def __init__(self,bedrooms,washroom):
#         self.bedrooms=bedrooms
#         self.washroom=washroom
# Apartment1=House('2 bedrooms','3 washrooms')
# Apartment2=House('beautiful living room','a  balcony with a beautiful view')
# print(Apartment1.bedrooms,'and',Apartment1.washroom)
# print(Apartment2.bedrooms,'and',Apartment2.washroom)

#Inheritance
class Car:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
        
class Vehicle1(Car):

    def color(self):
        print( 'white')
    
class Vehicle2(Car):
    
    def color(self):
        print( 'gray')
    
class Vehicle3(Car):

    def color(self):
        print ('pink')
    
car1=Vehicle1('Mercedes Benz','A80')
car2=Vehicle2('Audi','A812')
car3=Vehicle3('Harrier','A23w')


for type in (car1,car2,car3):
    type.color()

# class girlfriends:
#     def __init__(self,beautiful,tall):
#         self.beautiful=beautiful
#         self.tall=tall
        
# class GirlA(girlfriends):
#     def __init__(self, beautiful, tall):
#         super().__init__(beautiful, tall)
        
# class GirlB(girlfriends):
#     pass

# shawrie=GirlA('gorgeous',5.6)
# print(f'She is so {shawrie.beautiful} and she is {shawrie.tall} tall')
# shawrie=GirlB('darksin',5.6)
# print(shawrie.beautiful)


