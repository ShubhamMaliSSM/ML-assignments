def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
        
    print(count)

text = str(input("Enter the string: "))
count_vowels(text)
