import random

data1 = {} 
data2 = {}

print("Start")
for x in range(1000000000000000000000000000000):
    num1 = random.randint(0, 1000000000000000000000000000000)
    print(f"{num1}")
    data1[x] = num1
    for y in range(1000000000000000000000000000):
        num2 = random.randint(0, 1000000000000000000000000000000)
        data2[y] = num2
        print(f"{num2}")

print("The script has finished. Please run me again to continue monitoring!")