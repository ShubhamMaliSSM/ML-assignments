def remove_duplicates(input_list):
    return list(set(input_list))

numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6]
clean_list = remove_duplicates(numbers)

print(f"Original: {numbers}")
print(f"Without duplicates: {clean_list}")
