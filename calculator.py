# def calculate_discount(price, discount_percent):

#     price=float(input('Enter the Original price:'))
#     discount_percent=float(input('Enter the discount percentage:'))

#     discount=price * discount_percent / 100
#     final_price=price - discount
#     if(discount_percent >= 20):
#         print('The price Final Price is:',final_price)
#     else:
#         print('The Price is :',price)
# calculate_discount(price='',discount_percent='')

#     Create a function named calculate_discount(price, discount_percent) that calculates the final price 
#     after applying a discount. The function should take the original 
#     price (price) and the discount percentage (discount_percent) as parameters.
#     If the discount is 20% or higher, apply the discount; otherwise, return the original price.
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price

def number(a,b):
    print(a + b)
number(10,20)

def name(Fname='Jane',Lname='Doe'):
    print('Hello',Fname,Lname)
name()
#lambda function
sum=lambda x ,y : x+y
print(sum(20,30))

list=lambda m,n,w: m+n-w
print(list(20,10,5))

#calculator
message=['Welcome to Nexas Calc']
updated_msg=[msg.upper() for msg in message]
print(updated_msg)

oper=('+','-','*','/','%')
print(oper)
operation=(input('Choose the operation you to be perfomed:'))

num1=int(input('Enter your first number:'))
num2=int(input('Enter your second number:'))


if(operation=='+'):
    sum=num1 + num2
    print(f'The Sum is:',num1 + num2)
elif(operation=='-'):
    subtraction= num1 - num2
    print(f'The Subtraction is {subtraction}')
elif(operation=='*'):
    multiplication = num1 * num2
    print(f'The multiplication is {multiplication}')
elif(operation=='/'):
    division = num1 / num2
    print(f'The division is {division}')
elif(operation =='%'):
    modulus= num1 % num2
    print(f'The modulus is {modulus}')
else:
    print('choose the right operation')


