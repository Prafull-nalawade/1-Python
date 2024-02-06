

age1 = input('please enter your age:')
print(type(age1))
print(age1)

age2 = input('please enter your age:')
print(type(age2))
print(age2)
age = age1 + age2
print(age)

************

age1 = input('please enter your age:')
print(type(age1))
print(age1)

****************


exchange_rate = 1.83
print(exchange_rate)
print(type(exchange_rate))

*****************

int_value = 100
string_value = '1.5'
float_value = float(int_value)
print('int value as a float:',float_value)
float_value = float(int_value)
print(type(int_value))

****************


#Complex number

c1 = 1
c2 = 2j
print('c1:', c1, ',c2:', c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)

**************


#Boolean Values
#Boolean type can only be one of true or false


all_ok = True
print(all_ok)
all_ok = False
print(all_ok)
print(type(all_ok))

*************


#you can convert string into boolean as long as string contain it

status = bool(input('OK it is confirmed?:'))
print(status)
print(type(status))

*************



home = 10
away = 15
print(home + away)
print(type(home + away))

goal_for = 10
goal_against = 7
print(goal_for - goal_against)
print(type(goal_for - goal_against))

***********



print (100/20)
print(type(100/20))

*******

print(100//20)
print(type(100//20))

*********

print('Modulus division 100 % 13:', 100 % 13)
print('Modulus divisiom 3%2:, 3%2)
      
*********

#power oparator

a = 4
b = 3
print(a**b)      


********



#compound operator

x = 0
x += 1 # has the same behaviour as x = x+1


***************

#none Value

winner = None
print(winner is None)

***********


winner = None 
print('winner:', winner)
print('winner is None:', winner is None)
print(type(winner))
print('winner is not None:', winner is not None)
print(type(winner))
print('set winner to True')
winner = True

**************




num = int(input('Enter a number: '))
if num > 0:
   print(num)

**************



num = int(input('Enter yet another number:'))
if num < 0:
    print('Its negative')
else:
    print('Its not negative')




#Advance Python (31 july 2023)


#list compression


lst = []
for num in range(0,20):
    lst.append(num)
    print(lst)
    
#we can write same method using list comprehemsion

lst=[num for num in range(0,20)]
print(lst)



##########################################

names=['date', 'mama','kaka']
lst=[name.capitalize() for name in names]
print(lst)


##################################



#how to add if statement in list comprehension

def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]
print(lst)     

###############################################



lst=[f"{x}{y}" for x in range(3)for y in range(3) ]
print(lst)


########################################

#Set comprehension

set_one={x for x in range(3)}
print(set_one)

###########################

#Dictionary comprehension

dict={x:x*x for x in range(3)}
print(dict)

################################################################

#Generator

#it is another way of creating iterator
#in a simple way 
#uese a keyword "yeild"

gen=(x
     for in range(3)
     )
print(gen)
for num in gen:
    print(num)
    
############################

gen=(x
     for x in range(3) 
     )
next(gen)
next(gen)

##########################

#function which return mutilple values

def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)

##########################################################

#now instead of using for loop we can write our own generator

gen=range_even(6)
next(gen)
next(gen)
next(gen)

############################################

#Chaining genrator

def length(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*' 
        
password=["not-good","give'm-pass","00100=100"]
for password in hide(length(password)):
          print(password)
          
          
 #################################

#Enumerate
#printing list with index

lst=["milk","egg","Bread"]
for index in range(len(lst)):
    print(f'{index+1} {lst[index]}')


###############################

#same code can be implemented using enumirate

lst=["milk","egg","Bread"]
for index,item in enumerate(lst,start=1):
    print(f'{index} {item}')
    
###################################    
         

#find all the number from 1-1000 that are divisible by 7

div7=[n for n in range(1,1000) if n%7==0]
print(div7)

##################################

#find all the number from 1-1000 that have a 3 in them

lst=[n for n in range(1,1000) if '3' in str(n)]
print(lst)


###############################################

#count the  number of spaces in a string

some_string = 'the slow solid swam sumptuously through the slimy swam'
spaces= [s for s in some_string if s ==' ']
print(len(spaces))


###########################################################

#creat a list of all the consonant in the string

sentence = '''Yellow yaks like yelling and yawning and yesturday theyyodled while eating yuky yams'''
result = [letter for letter in sentence if letter not in 'a,e,i,o,u," "']
print(result)


##########################################################


#find the common number in two lists(without using tuple or set)list'''

list_a = [2,4,5,6]
list_b = [4,5,6,7]
common = [a for a in list_a if a in list_b]
print(common)

#########################################################

#Get only the number in a sentence like'In 1984 there were 13 instances of a protect with over 1000 people attending'

sentences = 'In 1984 there were 13 instances of a protect with over 1000 people attending'
word = sentences.split()
result = [number for number in word if not number.isalpha()]
print(result)

################################################


for n in range(20): 
    if n%2==0:
        result.append('even')
    else:
        result.append('odd')
print(result)
        
#list comprehension

result = ['even' if n%2==0 else 'odd' for n in range(20)]          
print(result)

###################################

#produce a list of tuple consisting of only the matching number in these lists 
# list_a = [1,2,3,4,5,6,7,,8,9]
#list_b =[2,7,1,12]
#result look like (4,4), (12,12)

list_a = [1,2,3,4,5,6,7,8,9]
list_b = [2,7,1,12]

result = [(a,b) for a in list_a for b in list_b if a==b]
print(result)

########################################################

#find all of the word in a string that are less than 4 letter
sentence = 'On a summer day Ramnath sonar went swwimming in the sun and his red skin stung'

examine = sentence.split()
result = [word for word in examine if len(word)>=4]
print(result)

#################################################

#write a python programm to print specified list
#after removing the 0th,4th and 5th elements.

color = ['Red','Green','White', 'Black' ,'Pink', 'Yellow']
color = [x for (i,x)in enumerate(color) if i not in (0,4,5)]
print(color)

####################################################

#write a python that creat a generator function 
#that yield cubes of numbers from 1 to n. Accept n from the user
def cube_generator(n):
    for i in range (1,n+1):
        yield i ** 3
        
#Accept input form the user
n = int(input("Input a number:"))
#creat the generator object
cubes = cube_generator(n)

#Iterate over the generator and print th cube
print("cube of number from 1 to ", n)
for num in cubes:
    print(num)
        
##############################################

#write a python programm to implement a generator that generates
#random number within a given range

import random
def random_number_generator(start,end):
    while True:
        yield random.randint(start,end)

#accept a input from user
start=int(input("Input the start value"))
end=int(input("input the end value:"))

#create a generator object
random_number=random_number_generator(start, end)
#generator and print 10 random number 

print("Random numbers between",start,"and",end)
for _ in range(10):
    print(next(random_number))                                                                                                         


#########################################################

#Python programm to creat 3*4*6 3D array whose each elemrnt is *.

 array =[[['*' for col in range(6)] for col in range(4)] for row in range(3)]
print(array)

#########################################################

#write a python program to print the number of a
#specifoed list after removing even number from it.

num =[7,8,120,25,44,20,27]
num = [x for x in num if x%2!=0]
print(num)


################################################

#zip function

name = ['dada', 'kaka', 'mama']
info = [3455,4555,4342]
countries = ['india', 'italy','america']
for nm,inf,coun in zip(name,info,countries):
    print(nm,inf,coun) 
    
    
 #use of zip function with his match list   


name = ['dada', 'kaka', 'mama', 'baba']
info = [3455,4555,4342]
for nm,inf in zip(name,info):
    print(nm,inf)


########################################################

#zip_longest

from itertools import zip_longest
name = ['dada', 'kaka', 'mama', 'baba']
info = [3455,4555,4342]
for nm,inf in zip_longest (name,info):
    print(nm,inf)

########################################################


#use of fill value insted none

from itertools import zip_longest
name = ['dada', 'kaka', 'mama', 'baba']
info = [3455,4555,4342]
for nm,inf in zip_longest (name,info,fillvalue=0):
    print(nm,inf)



######################################################

#use of all(), the values are true then it will produce output

lst=[2,3,6,8,9]
if all(lst):
    print('all values are true')
else:
    print('unless')
    
 #use of all(), the values are true then it will produce output

lst=[2,3,-6,8,9] #value must be non zero,+ve,-ve
if all(lst):
    print('all values are true')
else:
    print('unless')   
    
    
    
#use of any if any one non zero value

lst=[0,0,0,-8,0]
if any(lst):
    print('It has some true')
else:
    print('Useless')
    
    
    
#use of any

lst=[0,0,0,0,0]
if any(lst):
    print('It has some true')
else:
    print('Useless')
 



####################################################
    

#count

from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))


#Now let us start from 1 

counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))


###################################################



#cycle

#suppose you have repeated tasks to be done
#then you can use this method

import itertools

intruction=('Eat','code', 'sleep')
for intruction in itertools.cycle(intruction):
    print(intruction)

################################################



#repeat()

from itertools import repeat
for msg in repeat ("keep patient", times=3): 
    print(msg) 
    
    
    
################################################


#Combination


from itertools import combinations
players = ['John', 'Jani', 'Janardhan']
for i in combinations(players,2): 
    print(i)
  
##########################################

#permutations


 
from itertools import permutations
players = ['John', 'Jani', 'Janardhan']
for i in permutations(players,3): 
    print(i)   
    
######################################################

#product 


from itertools  import product
team_a=['Rohit', 'Pandey', 'Bumrah']
team_b=['virat','Manish','sami']
for pair in product(team_a,team_b):
    print(pair)


######################################################


age = [27,17,21,19]
adults = filter(lambda age:age>=18,age)

print([age for age in adults])

################################################

#Assignment operation 
#this will be only creat a new variable with 

list_a = [1,2,3,4,5]
list_b = list_a

list_a[0] = -10
print(list_a)
print(list_b)

#############################################################

#Shallow copy
#one level deep. modifying on level 1 does not affect the other 


import copy
list_a = [1,2,3,4,5]
list_b = copy.copy(list_a)

#not affect the other list

list_b[0]= -10
print(list_a)
print(list_b)

##################################################

#Drawback of shallow copy

import copy
list_a = [1,2,3,4,5],[6,7,8,9,10]
list_b = copy.copy(list_a)

#affect the other

list_a[0][0]= -10
print(list_a)
print(list_b)

########################################################

#Deep copy

#full independed clones. use copy.deepcopy().

import copy
list_a = [1,2,3,4,5],[6,7,8,9,10]
list_b = copy.deepcopy(list_a)

#affect the other

list_a[0][0]= -10
print(list_a)
print(list_b)

###############################################

#write a python program to create an iterator
#from several iteral in sequence and siplay
#the type of elemtn of the new iterator

from itertools import chain
def chain_f(lst1,lst2,lst3):
    return chain(lst1,lst2,lst3)

result = chain_f([1,2,3],['a','b','c','d'],[4,5,6,7,8,9])
print ("Type of the new iterator: ")
print(type(result))
print("The new iterator is: ")
for i in result:
    print(i) 


#############################################################


#Tuple

from itertools import chain
def chain_f(lst1,lst2,lst3):
    return chain(lst1,lst2,lst3)

result = chain_f((10,20,30),('a','b','c','d'),(40,50,60,70,80,90))
print ("Type of the new iterator: ")
print(type(result))
print("The new iterator is: ")
for i in result:
    print(i)

######################################################

#write a python programm that generator the running product
#of elements in an iterable.


from itertools import accumulate 
import operator
def running_product(lst):
    return accumulate(lst,operator.mul)

#list
result = running_product([1,2,3,4,5,6,7])
print("Running product of a list:")
for i in result:
    print(i)

# The first element is 1.
# The second element is 1 * 2 = 2.
# The third element is 2 * 3 = 6.
# The fourth element is 6 * 4 = 24.
# The fifth element is 24 * 5 = 120.
# The sixth element is 120 * 6 = 720.
# The seventh element is 720 * 7 = 5040.
# The eighth element is 5040 * 8 = 40320.
# The ninth element is 40320 * 9 = 362880.


########################################################

#tuple

result = running_product((1,2,3,4,5,6,7))
print("Running product of a list:")
for i in result:
    print(i)


##########################################################


#write a python programm to contruct an infinite iterator that
#return evenly spaced values starting with a specified number and step


import itertools as it
start = 10
step = 1
print("the starting number is ",start,"and step is", step)
my_counter = it.count(start,step)
#following loop will run for ever
print("the said function print never-ending items:")
for i in my_counter: 
    print(i)


##############################################################


#Write a python to generate an infinite cycle
#of element from an iterable

import itertools as it
def cycle_data(iter):
    return it.cycle(iter)

#following loops will run for ever
#list

result = cycle_data(['A','B','C','D'])
print("The said function print never-ending items:")
for i in result:
    print(i) 
    
    
 ########################################################

#string
   
result = cycle_data('python itertools')
print("The said function print never-ending items:")
for i in result:
    print(i)


#############################################################

#write a python programm to make an iterator that drops
#elements from the iterable as soon as elemrnts is positive number

import itertools as it
def drop_while(nums):
    return it.dropwhile(lambda x:x<0, nums)
nums=[-1,-2,-3,4,-10,2,0,5,12]
print("Original list : ",nums)
result=drop_while(nums)
print("Drops elements from the iterable when a positive number arises\n",list(result))


























