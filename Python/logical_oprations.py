#Event Scheduling depending onn the wether

temp = float(input("What is the current temperature? "))
is_raining = input("Is it raining? (yes/no): ").lower()
if temp > 30 or temp < 15 or is_raining:
    print("\nThe event has been cancelled")
else:
    print("\nThe event will go on as planned\n")
    