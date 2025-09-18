first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
city =  input("Enter your city: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))

full_name = first_name + " " + last_name

greeting = "Hello, " + full_name + " from " + city + "!"
print("Concatenated greeting:", greeting)

print("-" * 30)  

print("Name in uppercase:", full_name.upper())
print("Name in lowercase:", full_name.lower())

print("Name length:", len(full_name), "characters")

info = f"{full_name} is {age} years old, {height}m tall, and lives in {city}."
print("Formatted user info:", info)
