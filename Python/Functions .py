#greatings
def greet(name):
    return f"Helo {name}!"
print (greet("Ayub"))


#happy birth day *3
def happy_birth_day(name,age) :
    return f'''happy birth day to you\n 
    happy bith day dear {name}\n
    happy birth day to you\n 
    how old are you now \n 
    {age}\n
    How old are you now\n 
    {age}\n
    happy birth day happy birth day, happy birth  day to you'''

print(happy_birth_day("Ayub", "21"))

#happy birth day again
def happy_birthday(name,age):
    return f" Happy birthday to you\n Happy birthday to you\n Happy bithday dear {name}\n Happy birthday to you\n how old are you now \n {age}\n How old are you now\n {age}\n happy birthday happy birthday, happy birthday to you"
print(happy_birthday("Ayub", 20))



#parameters vs arguments
def add(a,b):
    z= a+b
    return z


def subtract(a,b):
    z= a-b
    return z


def multiply (a,b):
    z= a*b
    return z
 

def divide (a,b):
    return a/b #This will work but the answer will not be returned
               #aparently this is considerd bad practice, dont do this
 
print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))

#create full name


def create_name(first_name, last_name):
    first_name =first_name.capitalize()
    last_name =last_name.capitalize() 
    return first_name+" "+last_name
print (create_name ("ayub","kipruto"))


#square of a number
def square(n):
    result =n*n
    return (result)
print(square(4))



#Describe
def discription(name,age,city,school):
    print(f'''{name} is {age} years old
curently in {city} for his attacment 
but a student in {school}''')
discription("Ayub","20","ngong","kirinyaga university")

#