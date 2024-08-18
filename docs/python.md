# Python

All about python modules, syntax and function

## For-loop

```python
# print even
list=[4,5,25,6,8,8,9,2,2,3,97,52,96,32,84,19]
for i in list:
    if i%2 == 0:
        print(i, end="")
        
# using while loop
candy=10
withdrawal=12
i=1
while i <= withdrawal:
    if i > candy:
        print(f"{i} : out of stock")
        break
    print(f"{i} : withdrawal")
    i+=1

# create list by taking input from user

list=[]
enter_range=int(input("enter the range to create list of elements"))
for i in range(enter_range):
    enter_num=input(f"enter element {i+1} :")
    list.append(enter_num)
print(list)
```

## Args and Kwargs

```python
##args

def sum(*args):
    total = 0
    for i in args:
        total = total+i
    print(total)

sum(5,6,7,8,9)  ##we can pass n number of arguments

###for key word arguments
 
def student(**data):
    for key,value in data.items():
        print(f"{key} {value}")
   
##callable = student(key=value,key=value)

student(name="John",age=30)
student(name="Ram",age=26)

```

## Dictionary

```python
person = {
    "name":"ram",
    "age":25,
    "gender":"male",
    "profession":"engineer"
}

## find value with key
print(person.get("age"))

##print all dict
print(person)

#or using for loop
for i,j in person.items():
    print(f"keys: {i} , values :{j}")
    
##print all keys
print(person.keys())

##print all values
print(person.values())

##items return list containing all values in tuple 
print(person.items())


##update dict
person.update({"salary":"100000"})
print(person)

print(person.get("amount"))
```

## Lambda

```python
##passing argument in lambda

numbers=[2,4,6,8,10]

def multiple(x):

    for i in x:
        i=i*2
        print(i,end=" ")

multiple(numbers)

##passing argument in lambda using map
 
doubled_map = list(map(lambda x: x*2,nums))
print(doubled_map)
```

### Filter

```python
##filter is similar to mapping
 
nums_list = [1,2,3,4,5,6,7,8,9]
even=[]
for x in nums_list:
    if x % 2 == 0:
        even.append(x)

print(even)
 
#with filter
 
def even(x):
    return x%2==0
 
even_list= list(filter(even,nums_list))
print(even_list)
```

### Mapping

```python
double_num = []
numbers = (5,6,7,8,9)

for num in numbers:
    double_num.append(num * 2)

print(double_num)
 
##using map

def double(num):
    return num*2
 
double_List = list(map(double,numbers))
print(double_List)
```

### List Comprehension

```text
syntax > [return-value for-loop if-condition]

```

```python
## with out list comprehension 
## print number which are divisible by 3

ls=[]
for i in range(100):
    if i%3==0:
        ls.append(i)
print(ls)

## using list comprehension

ls=[i for i in range(100) if i%3==0]
print(ls)
```

### Dictionary Comprehension

```text
syntax > {return-value for-loop if-condition}
```

```python

dict1={i:f"item{i}" for i in range(100)}
print(dict1)

nums_List=[5,6,7,8]

## listcomprehension for maping

mapping = list(x*2 for x in nums_List)
print(mapping)
 
## listcomprehension for filtering

filtering = list(x for x in nums_List if x%2==0)
print(filtering)
```

## Decorator

```python
def first(func):    ##passing the func as an argument
    def second():
        print("execute the first line")
        func() ##call the funct
        print("execute the second line")
    return second()
   
@first   ###decorate
def middle():
    print("execute the middle line")
   
# mid = first(middle)  ##another way to call decorate
middle()
```

## Read Write File

```python
f = open("./read_write_demo.txt","r")  ##r=read
print(f.read())   ##read() to print the txt 
f.close() ##close
```

### Logging

```python
import logging

##using getlogger to create seperate log files
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO) ##set logging level

## formatter is to set logs format
log_format=logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

## fileHandler is user to create a file
log_file=logging.FileHandler("example.log")

log_file.setFormatter(log_format)
logger.addHandler(log_file)

## further code
def something():
    logger.info("this is a something function")
```

## Class

### basic class structure

```python


class Student:
    ##self hold the value of instant obj

    def __init__(self,name,age) -> None:   ##here self represent to b1
        self.name = name
        self.age = age
   
    def __str__(self) -> str:   ##__str__() function controls what should be returned when the class object is representd as string.
        return f"{self.name}"
 
    def hello(self):  ## funct is called methods in class
        print("heellooo")
 
    def get_name(self):
        return self.name
   
    def get_details(self):
        print("name",self.name)
        print("age",self.age)

   

## for every class we need to define obj
## here b1 var is obj for class Book

b1 = Student("RAM",26)  ##b1 here is obj
b1.hello()   ##obj.method
print(b1.get_name())    ##obj.method
b1.get_details()

 
b2=Student("Krishna",11)   ##use the same class by creating another obj
b2.get_details()
```

### Isinstance

```python

x = isinstance("Hello", (float, int, str, list, dict, tuple))
print(x)

```

```python
class Myclass:
    name = "John"

obj = Myclass()
x = isinstance(obj, Myclass)
```

### Dataclass

```python
#without dataclass

class Person():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

person=Person("Ram","krishna",26)
print(person.first_name)
 
##with dataclass

from dataclasses import dataclass   ##import dataclass

@dataclass
class Book:

    title : str    ###variables are define without using __init__ instance
    author : str
    price : float
  
book=Book("Peaceofmind","Unknown",50.50)
print(book.price)
```

### Method-Static

```python
##class method :A class method is a method which is bound to the class and not the object of the class.
##static method : A static method is used when we want to create a function without using self as instance-(just to create a independent fucntion)

from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # a class method to create a
    # Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
    
    # a static method to check if a
    # Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18

    ##static method eg 2
    ##this function is independent of the class ,created without using self as instance
    @staticmethod
    def thankyou(msg):
        return msg

person1 = Person('ram', 21)
person2 = Person.fromBirthYear('ram', 1997)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))

# print thankyuu msg
print(Person.thankyou("thanks for looking up this file"))

```

### Inheritance

```python
class Publisher:

    def __init__(self,title,price) -> None:
        self.title=title
        self.price=price
 
class Author(Publisher):   ##add class name to inherit

    def __init__(self,title,price,pages,period) -> None:
        super().__init__(title,price)   ###add module super()to fetch the var for Publisher class
        self.period=period
        self.pages=pages
  
class Book1(Publisher):    ##add class name to inherit

    def __init__(self,title,price,author) -> None:
        super().__init__(title,price)
        self.author=author    ##adding variable rather then class
      
class Magazine1(Author):

    def __init__(self,title,author,pages,period) -> None:   ##using Author class to fetch the values
        super().__init__(title,author,pages,period)
      
class Newspaper1(Author):

    def __init__(self,title,price,pages,period) -> None:
        super().__init__(title,price,pages,period)

      
b1=Book1("PeaceofMind","Unknown",100)

m1=Magazine1("Vogue","Kiran",20,15)

n1=Newspaper1("TOI","toi",5,10)

print(b1.author)

print(m1.period)
```
