#we are going to need the user to  provide two inputs
#the temperature itself
#the unit they are currently on

temperature = float(input(" \n Enter your temperature: "))
unit = input("Enter your unit ( 'c' for(Celsius) or 'f' for(Fahrenheit): ").lower()

if unit == "" or temperature == "":
   print("You did not enter your unit or the  temperature or maybe even both, please try again")
elif unit == "c":
    temperature = temperature + 273.15
    print(f"Your temperature is {round(temperature, 2)} F")
elif unit == "f":
    temperature = temperature - 273.15
    print(f"Your temperature is {round(temperature, 2)} C")
else:
    print(f"One your temperature '{temperature}' or '{unit}' is invalid")
