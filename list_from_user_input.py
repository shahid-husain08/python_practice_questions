#Ask the user to enter 5 numbers and store them in a list.

number = []

for i in range(5):
    num = int(input("Enter the number = "))
    number.append(num)
print(number)