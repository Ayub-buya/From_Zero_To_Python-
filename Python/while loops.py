# basic stuff
i = 1
while i <= 10:
  print(i* "*")
  i += 1
   
# A chrismass tree
i = 1
while i <= 10:
    print(i * "*" )
    i = 1+i

number =[1,2,3,4,5,6]
i=0
while i < len(number):
    print(number[i])
    i = i+1


number =[1,2,3,4,5,6]
count = 0
while count < len(number):
    print(number[count])
    count += 1


#Chrismas Tree
# Christmas Tree using while loop
#AI generated look into it, Seriously

rows = 1
height =int(input("Enter your desired height for the tree(I would advice 10): ")) 

while rows <= height:
    # Print spaces for centering
    spaces = height - rows
    while spaces > 0:
        print(" ", end="")
        spaces -= 1
    
    # Print stars
    stars = (2 * rows) - 1
    while stars > 0:
        print("*", end="")
        stars -= 1
    
    print()  # move to next line
    rows += 1

# Print the trunk
trunk = 2
while trunk > 0:
    space_count = height - 1
    while space_count > 0:
        print(" ", end="")
        space_count -= 1
    print("|")
    trunk -= 1


count = 1 
while count <= 10:
    print(count)
    count += 1


#pasword 
pasword = ""
while pasword != "cow":
    pasword = input("Enter your pasword: ").lower()
    print("Acees Granted")
    
#breck an infinite loop
#IDK WHAT THIS IS
while True:
    name =input("What is your name stranger?(if you dont want t andwer please entrer'Quit')").lower().split()
    if name == "quit":
        break
    print("Heleo {name}")

