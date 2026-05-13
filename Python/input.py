# string input

#ask the user for his or her name
name = input ("Whats your name?  ")
#say heyy to the user

"""ask ther user for his or her age"""
age = input("How old are you?   ")

print ("heyy you smelly bustard  " + name + "")
print (" You are now  " + age + " years old and ageing fast, make the most of your teenlife, and most impotant of all make yourself proud, mama raised no fools")

#to make the same stuff in the same line do as follows
color = input ("what is your favorite colour?  ")
print (" your favorite colour is ", end="")
print (color)

# Another way of askig for the user input can be done as follows by combinig both of the above methods
# I highly recomend this method as it is more efficient and less time consuming
food =input ("what is your favorite food?  ")
print ("I heard somewhere that your favorite food is ", food)
 # man also used sep to separate the different values in the print statement
print ("No way your favorite food is ", food , sep = "") 

#modern programers move diferent. Here is an example of how thy query for user input in thr modern GAME
sport = input ("what is your favorite sport? ")
print (f" your favorite sport is {sport} ")
# so we are going to role with the above like the big boys, okay!

# remove the space between the input do as follows
name = name.strip()
# the above will remove the space between the input and the output, so if the user input is " John " it will remove the space and output "John"
 
# You can also capitalize the first letter of the input by using the capitalize() method
name = name.capitalize()

# you may also need to capitalize the first letrer of the firs words in the input, you can do that by using the title() method
name = name .title() 

# YOU CAN BE A SMART ONE AND COMBINE ALL THE ABOVE METHODS IN ONE LINE OF CODE AS FOLLOWS
name = input ("What is your name? ").strip().title()
print (f" encantado ,{name}")
# I guess you feel like you just wasted your time .....haha...cry more

 # you can split users name into first name and last name by using the split() method
first_name, last_name = name.split(" ")
print (f"your first name is {first_name} and your second name is {last_name}")
 # you can exxclude each individualy and print out the firs name alone but you AREE  TOO GOOD ENOUGH YOU DONT NEED AN EXAMPLE, righht?

#IN summary
F1_favorite_driver = input("Who is your favorite driver?"  ).strip().title()
print (f"No wayy me too. I love {F1_favorite_driver} soo much, no one comes close")

# Integers input
 # ask the user to input their age
age = int(input ("How old are you? "))
print (f"you {age} and soo young you still have alot to give to this world, dont give up you matter")
# we dont use ".strip "or ".titile " because an integer has 

#floats input
#this are simplty integers with decimal points
# ask the user to input their height
hight = float(input ("What is your current height? "))
print (f"you are {hight}metres tall, wow you still have a long way to gorow.")
#float
#floats are also used to represent money, so you can ask the user to input their salary and then you can calculate their tax and then you can calculate their net salary
salary = float(input("What is your salary ?"))
print (f"Your salary is {salary}")
 # we can decide the no of decimals they have by using the round() function
salary = round (salary, 2) 
# this will round the salary to 2 decimal places
print (f"your salary is {salary}")
