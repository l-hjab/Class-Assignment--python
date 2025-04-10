#reading a new file >> example.txt
file2=open('example.txt','r')
data2=file2.read()
print(data2)
 
file=open('books.txt','w')
data=file.write('Hello,Daphy i love you so much...Hello,Find the list of books that i have read')

try:
    datafile=input('Enter the name of the file:')
    datafile=open(datafile,'r')
    dataread=datafile.read()
except FileNotFoundError:
    print('Create the file before its read')


