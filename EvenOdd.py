numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

even_nos = []
odd_nos = []

for n in numbers:
    if n % 2 == 0:
        even_nos.append(n)
    else:
        odd_nos.append(n)

print("Even:", even_nos)
print("Odd:", odd_nos)
