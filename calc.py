def calc():#function definition
    print("Welcome to DN Calculator")
    num1=int(input("Enter the first number:")) #variable declaration
    num2=int(input("Enter the second number:"))

    sum= num1 + num2
    sub=num1 - num2
    mult= num1 * num2
    div=num1 / num2

    calculate=input("What calculation do you want to perform:")
    if(calculate =='+'):
        print("Sum🤞:",sum)
    elif(calculate== '-'):
        print("Subtraction🤞:", sub)
    elif(calculate=='*'):
        print("Multiplication👏:", mult)
    elif(calculate=='/'):
        print("Division🤞:", div)
    else:
        print("Please select the right function")
    print('Created by Data analyst Daphie😜👩')
    

calc()#calling the function