name = ["JEcica", "Manu", "Josh", "Tim"]
print(name[0:3] )

name = ["JOhn", "Bob", "Josh", "Tim"]
name[0]="Johnson"
print(name[0] )


#how to add in a new number using .append
number = [1,2,3,4,5]  
number.append(6)
print (number)

#how to add in a new number using .insert
number = [1,2,3,4,5]
number.insert(6,6)
print (number)


#how to remove a number using .remove
number = [1,2,3,4,5]
number.remove(3)
print (number)


#how to remove all 
number = [1,2,3,4,5]
number.clear()
print (number)


#how to check if a certain value is precent in the list 
number = [1,2,3,4,5]
print (1 in number)

#how to check the number of items in a list
number = [1,2,3,4,5]  
print (len(number))