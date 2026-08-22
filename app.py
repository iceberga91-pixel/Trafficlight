time = int(input("How many seconds have passed?"))

while time > 60:
    time = time - 60

if time < 40:
    print("RED")

elif time < 50:
    print("YELLOW")

elif time <= 60:
    print("GREEN")

lat
