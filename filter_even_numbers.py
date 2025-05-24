#From the list nums = [10, 15, 20, 25, 30], create a new list that contains only the even numbers.

nums = [10, 15, 20, 25, 30]

new= []
for n in nums:
    if n%2 == 0:
        new.append(n)
print(new)