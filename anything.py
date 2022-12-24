lst = [1, 2, [], 3, [], 4]

# Use a list comprehension to filter out empty elements
filtered_lst = [x for x in lst if x]

print(filtered_lst)  # Output: [1, 2, 3, 4]