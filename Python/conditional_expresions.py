# This program checks if a number is even or odd
number = int(input("Enter the number you want to check if it is even or odd: "))
if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")


# This program checks if a number is positive, negative.

number = float(input("Enter the number you want to check if it is positive, negative : "))
print("positive"if number > 0 else "negative")

#This programs checks which number is greater than the other 
#This programs checks which number is greater than the other 

print ("This programs checks which number is greater than the other ")
a = int (input("Enter the first number: ") )
b= int (input("Enter the first number: ") )

print ("The greater number is {a}"if a > b else "The greater number is:",b)



#status 
age = int (input ("Enter your age: "))
print ( "adult" if age >= 18 else "under age ")

#temprature

temp =int( input(" please enter the curent room tempratue: "))
temp = "HOt" if temp > 40 else "Cool"
print (f"The room is {temp} ")

#but we can wright a simpler one 
#temprature
temp = int(input ("Enter you curent temperatue: "))
print ("It is must be hot" if temp > 20 else "It is must be cold" )

