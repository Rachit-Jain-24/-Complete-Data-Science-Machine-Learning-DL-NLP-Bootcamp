# Basis of python

'''
________________________________________________________________________________________________

'''

# 1. print
print("This is the way to print output in python") # simple print
sum=5+6
print("the sum of 5 + 6 =" ,sum,"can be printed using variable too in this statement itself") #variable along
print("To enter a new line we use \n slash N for new line or separators like end=,sep=, etc") # new line
print(f"sum of 5+6 is equal to {sum}") #f-string method to print 

print("________________________________________________________________________________________")

'''
________________________________________________________________________________________________

'''

# 2. Variables
#ways of assigning variables
a=10
b=20
c=a+b
str1="10"
float_var=0.5
boolean1=True
boolean2=False

print("________________________________________________________________________________________")

'''
________________________________________________________________________________________________

'''

#3. Data types:
a=10
print("data type of a is",type(a))
b='Hello'
print("data type of b is",type(b))
c=10.5
print("data type of c is",type(c))
d=True
print("data type of d is",type(d))
e=10+5j
print("data type of e is",type(e))
f=complex(10,2)
print("data type of f is",f,type(f))


print("________________________________________________________________________________________")

'''
________________________________________________________________________________________________

'''
# 4. operators

# Arithmetic operators
# Operator	Operator Name	Example
#    +	    Addition	     15+7
#    -	    Subtraction	     15-7
#    *	    Multiplication	 5*7
#    **     Exponential	     5**3
#    /	    Division	     5/3
#    %	    Modulus	         15%7
#    //	    Floor Division	 15//7

n = 15
m = 7
ans1 = n+m
print("Addition of",n,"and",m,"is", ans1)
ans2 = n-m
print("Subtraction of",n,"and",m,"is", ans2)
ans3 = n*m
print("Multiplication of",n,"and",m,"is", ans3)
ans4 = n/m
print("Division of",n,"and",m,"is", ans4)
ans5 = n%m
print("Modulus of",n,"and",m,"is", ans5)
ans6 = n//m
print("Floor Division of",n,"and",m,"is", ans6)
print("________________________________________________________________________________________")


#comparison operator
# Operator	Operator Name	Example
#    >	    Greater Than	     15>7
#    <	    Less Than	     15<7
#    >=	    Greater Than or Equal to	 15>=7
#    <=	    Less Than or Equal to	 15<=7
#    ==	    Equal to	     15==7
#    !=	    Not Equal to	     15!=7

n = 15
m = 7
ans1 = n>m
print("Greater than",ans1)
ans2 = n<m
print("Less than",ans2)
ans3 = n>=m
print("Greater than or equal to",ans3)
ans4 = n<=m
print("Less than or equal to",ans4)
ans5 = n==m
print("Equal to",ans5)
ans6 = n!=m
print("Not equal to",ans6)
print("________________________________________________________________________________________")

# logical operator
# Operator	Operator Name	Example
#    and	    Logical AND	     15>7 and 5==5
#    or	    Logical OR	     15>7 or 5==5
#    not	    Logical NOT	     not 15>7

n = 15
m = 7
ans1 = n>m and m==5
print("Logical AND",ans1)
ans2 = n>m or m==5
print("Logical OR",ans2)
ans3 = not n>m
print("Logical NOT",ans3)
print("________________________________________________________________________________________")

# bitwise operator
# Operator	Operator Name	Example
#    &	    Bitwise AND	     15&7
#    |	    Bitwise OR	     15|7
#    ^	    Bitwise XOR	     15^7
#    ~	    Bitwise NOT	     ~15
#    <<	    Left Shift	     15<<2
#    >>	    Right Shift	     15>>2
n = 15
m = 7
ans1 = n&m
print("Bitwise AND",ans1)
ans2 = n|m
print("Bitwise OR",ans2)
ans3 = n^m
print("Bitwise XOR",ans3)
ans4 = ~n
print("Bitwise NOT",ans4)
ans5 = n<<m
print("Left Shift",ans5)
ans6 = n>>m
print("Right Shift",ans6)
print("________________________________________________________________________________________")

# identity operator
# Operator	Operator Name	Example
#    is	    Identity	     x is y
#    is not	Identity not	     x is not y
#    in	    Membership	     x in y
#    not in	Membership not	     x not in y
x = 10
y = 10
ans1 = x is y
print("Identity",ans1)
ans2 = x is not y
print("Identity not",ans2)
print("________________________________________________________________________________________")


# membership operator
# Operator	Operator Name	Example
#    in	    Membership	     x in y
#    not in	Membership not	     x not in y

print("________________________________________________________________________________________")

'''
________________________________________________________________________________________________

'''
# 5. input
val = input("Enter your value: ") 
print(val) 
print("")
num = int(input("Enter a number: ")) 
print(num, " ", type(num)) 
print("")
# Taking list1 input from user as list
list1 = list(input("Please Enter Elements of list1: "))
 
# Taking list2 input from user as list
list2 = list(input("Please Enter Elements of list2: "))
 # appending list2 into list1 using .append function
for i in list2:
    list1.append(i)
 
# printing list1
print(list1)

print("________________________________________________________________________________________")

# Python program showing how to
# multiple input using split
# split is used to take multiple inputs at a time with default separator i.e. space , we can give , also as a sep
#split can be used with map and list function.

# taking two inputs at a time
x, y = input("Enter two values: ").split(" ")
print("Number of boys: ", x)
print("Number of girls: ", y)
print("")
# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
print("")
# taking two inputs at a time
a, b = input("Enter two values: ").split()
print("First number is {} and second number is {}".format(a, b))
print("")
# taking multiple inputs at a time 
# and type casting using list() function
x = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ", x)
print("________________________________________________________________________________________")


print("")

# 6. String

# Creating a String
# with single Quotes
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ")
print(String1)
print("")
# Creating a String
# with double Quotes
String2 = "I'm a Geek"
print("\nString with the use of Double Quotes: ")
print(String2)

#accessing string elements
print("")
print("accessing the string elements using indexing:")
print("first element of string 1 is:",String1[0])
print("last element of string 1 is:",String1[-1])

print("")
#slicing
print("slicing the string elements using indexing:")
print("displaying elements from 2 to 6th character:", String2[2:5])

print("")

print("reversal of string using slicing")
gfg = "geeksforgeeks"
print(gfg[::-1])

print("")

# Python Program to Update
# character of a String

String5 = "Hello, I'm a Geek"
print("Initial String: ")
print(String5)

# Updating a character of the String
## As python strings are immutable, they don't support item updation directly
### there are following two ways
#1
list1 = list(String1)
list1[2] = 'p'
String4 = ''.join(list1)
print("\nUpdating character at 2nd Index: ")
print(String4)

String3 = String5[0:2] + 'p' + String5[3:]
print(String3)

print("")
print("to use variables in print then use f string:")
f=24
print(f"the birthdate of mine is {f}")

print("")
print("String methods")

a = "!!!Harry!! !!!!!!!!! Harry"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry", "John"))
print(a.split(" "))
blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Harry"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))
# print(str1.index("ishh"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())
print("________________________________________________________________________________________")




# 7.Lists

l1=[1,2,3,4]
print(l1)
l2=[]
for i in l1:
    l2.append(i)
print(l2)

print("2nd element of l1 is",l1[1])

print("last element of l1 is",l1[-1])

print("slicing l1 from 1 to 3 is",l1[0:2])

print("reversal of l1 is",l1[::-1])

l3=l1+l2
print(l3)

l4=[['rachit',10,'rj',24],['nj',22,'vj',45]]
print(l4)
print("accessing elements from multi dim list")

print(l4[0][0]) # this means the first index is for selecting the dim or list from where you can choose the element to be displayed using second index which is the position of the character

print(l4[1][2])

print("length of the list 1:",len(l1))

print("length of the list 2:",len(l2))


print("")
print("list methods")

#append
list1=[1,2,3,4]
list1.append(5)
print(list1)

#extend
list2=[1,2,3,4]
list2.extend([5,6,7])
print(list2)

#insert
list3=[1,2,3,4]
list3.insert(2,5)
print(list3)

#remove
list4=[1,2,3,4]
list4.remove(2)
print(list4)

#pop
list5=[1,2,3,4]
list5.pop(2)
print(list5)

#clear
list6=[1,2,3,4]
list6.clear()
print(list6)

#count
list7=[1,2,4,4,1,2,3,4]
print(list7.count(4))

#reverse
list8=[1,2,3,4]
list8.reverse()
print(list8)

#sort
list9=[8,7,1,4]
list9.sort()
print(list9)


print("" '\n' "list Compression")

# Python program to demonstrate list 
# comprehension in Python 
  
# below list contains square of all 
# odd numbers from range 1 to 10 
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1] 
print(odd_square)



# 3. if else
# 4. for loop
# 5. while loop
# 6. break
# 7. continue
# 8. pass
# 9. def
# 10. lambda
# 11. list
# 12. tuple
# 13. set
# 14. dictionary
# 16. list comprehension
# 17. tuple comprehension
# 18. set comprehension
# 19. dictionary comprehension
# 20. string
# 21. string methods
# 22. list methods
# 23. tuple methods
# 24. set methods
# 25. dictionary methods
# 26. control flow statements
# 27. file handling
# 28. exception handling
# 29. modules
# 30. packages
# 31. class
# 32. object
# 33. inheritance
# 34. polymorphism
# 35. encapsulation
# 36. data abstraction
# 37. data hiding
# 38. data encapsulation
# 39. abstract class
# 40. interface
# 41. method overriding
# 42. method overloading
# 43. operator overloading
# 44. decorators
# 45. garbage collection
# 46. memory management
# 47. threading
# 48. multiprocessing
# 49. asyncio
# 50. asyncio with threads
# 51. asyncio with processes
# 52. asyncio with coroutines
# 53. asyncio with tasks
# 54. asyncio with queues
# 55. asyncio with events
# 56. asyncio with condition variables
# 57. asyncio with semaphores
# 58. asyncio with barriers
# 59. asyncio with mutexes
# 60. asyncio with locks
