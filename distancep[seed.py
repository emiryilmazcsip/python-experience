speed = int(input("Enter the speed"))
hours = int(input("Enter the hours"))
counter = 1
for counter in range(1, hours + 1):
    distance = speed * counter
    print(counter, distance)
    counter += 1
