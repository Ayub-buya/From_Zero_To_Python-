# this in one of the most easiest ways of storing data

capitals = {
    "kenya" : "Nairobi",
    "Canada"  : "Ottowa",
    "England" : "London",
    "Itali" : "rome",
    "Germany" :"Berlin",
    "USA" : "washington DC"
}
#print(dir (capitals)) #to display all the keys and values

print (capitals.get("Canada")) #to check is a value is within a dictionary
capitals.update({"japan":"Tokyo"})
capitals.update({"USA":"NYC"})
print(capitals.get("USA"))
capitals.pop("England")
print(capitals.get("England"))



