import pandas as panda
import  numpy as nm
import matplotlib.pyplot as plt


def area(x ,y = 1) :
   return x * y

def multipleReturns ():
    first = int(1)
    second = int(2)
    third = int(3)
    return  first, second,third

def attempt_float(x):
    try:
        return float(x)
    except:
        return x

result = area(5, 2)

print(" Result is ",result)

result = area(5)
print(" Result Default values is ",result)

## Print Hello World 3 times

print("Hello World "*3)

x = 1

fruitList = {'Apple','Orange','Mango','Grapes'}

for fruit in fruitList :
    print(fruit)

for number in range(6):
    print(number)


for x in range(2,6):
    print(x)

message = "Hello World "

print(message*2)
print(message[0])
print(message[2:5])
print(message[-4])

# BOTH Refer to new object fruitNewList and fruitList
print(fruitList)
fruitNewList=fruitList
print(fruitNewList)
fruitList.add("Mongo")
print(fruitNewList);

str = "This is String"
num = str.count('s')
print(" Count is ",num)

cibil_score = 450

status = "Approved" if(cibil_score  > 750 ) else "Reject";

print(" Loan status is ",status)

employeeTuple = tuple(["Sandeep","370941",37.22,31])
employeeList = tuple([("Sandeep","370941",37.22,31),("San","370",37.22,30),("Deep","941",37.22,31)])

print("************"*2)
for name,empId,perDay,age in employeeList:
    print(" Record ",name,empId,perDay,age)

strings = ['a', 'as', 'bat', 'car', 'dove', 'python']

first,second,third = multipleReturns()
print(first)
print(second)
print(third)



#numPandaArray = nm.random.randn(2,2)

#print(numPandaArray)

numPandaArray = nm.array([[1,2,3,4],[5,6,7,8]])


print(numPandaArray)

print(numPandaArray.sum())
print(numPandaArray.max())
print(numPandaArray.min())

plt.plot(nm.random.randn(50).cumsum())