# initialize dictionary 
test_dict = {'AVENGERS': 2, 'Assemble': 2, 'AHHHHHHHHH': 1}

# printing the original dictionary
print("original dictionary: ", test_dict)

# initialize value
value = 2

# using loop
#selective key values in dictionary

res = 0
for key in test_dict:
    if test_dict[key] == value:
        res = res+1

# printing the result
print("Frequency of value is:", res)
