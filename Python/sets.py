fruits = {"Mango", "banana","Apple" }
print (fruits)

Friends = (["sam","Anto", "Eugine", "Phidel"])
print (Friends)

#Adding
fruits = {"Mango", "banana","Apple" }
fruits.add("Orange")
print(fruits)

Friends = (["sam","Anto", "Eugine", "Phidel"])
Friends.append("Tina")
print (Friends)

#Removing
# removes - ERROR if not found
fruits = {"Mango", "banana","Apple" }
fruits.remove("Mango")
print (fruits)

#Removing all item
Friends = (["sam","Anto", "Eugine", "Phidel"])
Friends.clear ()
print (Friends)


#Removing a random item
Friends = (["sam","Anto", "Eugine", "Phidel"])
Friends.pop()
print (Friends)


# cheking menbership
fruits = {"Mango", "banana","Apple" }
print ("banana" in fruits)


#cream de la cream
a= {1,2,3,4}
b= {3,4,5,6}

print (a | b)     #TO print all the elements in both sets
print (a & b)     #To print out the coomon elements in both sets
print (a - b)     #To print out alll the elements in a that are not in b
print (a ^ b)     #To print out what is not in both a and b

