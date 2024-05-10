print("Shubham")
print(12)
print("Hello shubham \ngupta")
# hi shubham comment
'''
multi
line
comment
'''

"""
This is
also work for 
multi line comment
"""

print("I am student of \"Btech computer science and engineering\" \'a")
print("Hey", 6, 7, sep="~") # Hey~6~7
print("Hey", 6, 7, end="$") # Hey 6 7$

############ Datatype  int,float, complex, string, boolean, list, tuple, dict

b=True
print(type(b))
a = complex(8,7)
print(a)

print(15//6) #it will print only digits that is before the decimal of the quotient
print(5**3) # it will works as power >> 5 ^3 = 125

# TYPECASTING

#x= input("Enter first number:")
#y = input("Enter second number:")  input take integer, string, boolean etc in string datatype so if enter
# x=12 , y=100 then x+y = 12100
#int(input())

name= "shubham"
print(name[0])
print(name[2])
print("**********************")

for character in name:
    print(character)

#Slicing
    x = "Shubham,Ghazipur"
    print(len(x))
    print(x[0:7]) # here 7 is excluding, it will print only from index 0 to index 6.
    print(x[:7]) # here if we doesn't mention the starting index like here '0', 
    #python will automatic insert it
    print(x[:])  # here python will insert 0 at starting index and string length at ending index.
    print(x[0:-3]) #python will interpret this like print(x[0:len(x)-3])  
    #>> output will be "Shubham,Ghazi"
    print(x[-1:-3]) # python interpret this like print(x[len(x)-1:-3])

##String methods
  # In Pythom, string is immutable like when perform any operation on string,
  # it will not change the original string, it create the another we can say reference
    nameOfx = " Shubham "
    print(nameOfx.upper()) #  output >> SHUBHAM 
    print(nameOfx.lower())
    print(nameOfx.strip())
    print(nameOfx) # output >> Shubham
    nameOfY = "chhotuu!!!! !!!!!!!" 
    print(nameOfY.rstrip("!")) # character should be last which is trailing ,
    #if we remove character"u" >> it can't
    print(nameOfY.replace("chhotuu","shubham"))
    print(nameOfY.split(" "))
    print(nameOfY.capitalize())
    print(nameOfY.center(50))
    print(nameOfY.count("c"))
    print(nameOfY.endswith("!!!!!!!"))
    # we can check string is ending with given parameter or not, also check for a value in-between the
    #string by providing start and end index positions.

    str1 ="welcome to the console"
    print(str1.endswith("to",4,10))

    # in python we can override the naming of the variable.
    print(str1.find("to"))
    print(str1.index("to"))

# isalnum()
# isalpha()
# islower()
# isupper()
# isprintable()
# isspace()
# istitle()
# startswith()
# swapcase()
# title()

#IF----------------ELSE
a=10
if(a>9):
    print("greater than 9")
else:
    print("less than 9")
print("loop ended")

# if(a>9):
#     print("lsdhfjhghs")
# elif:
#     print("dhfuguhfuhdfjvh")
# else:
#     print("kjdfhjhhhjfhjhj")

# match case >>  similiar to switch case
# There is no need of "break" keyword here.
# we case if -else in case 

ele = 7

match ele:
    case 0:
        print("case 0")
    case 1:
        print("case 1")
    case 2:
        print("case 2")
    case 7:
        print("case 7")
    case _:
        print("Default case")
#   case _ if(x>10)
        # print("x")


 # FOR-_-----------------------------------------------------------------LOOP
        # for character in ele:
        #     print(character)
        # for character in range(5):
        #     print(character)
        # for character in range(1,9):
        #     print(character)
        # for character in range(1,12,3):
        #     print(character)

 # While----------------------Loop-------While---else-------------------LOOP
 # DO -----------------------WHILE ------------LOOP
#  BREAK------------------CONTINUE

for char in range(11):
    if(char==10):
        break
    print (char)
print("break execute")


for char in range(11):
    if(char==10):
        continue
    print(char)
print("continue execute")


# FUNCTIONS
