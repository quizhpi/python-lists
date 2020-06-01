#
# Lists with python
#

# List of companies
companies = ["Tesla", "SpaceX", "Amazon", "Apple", "Google"]
print(companies)

# Access the last element of the list
companies = ["Tesla", "SpaceX", "Amazon", "Apple", "Google"]
print(companies[-1])

# Access all the elements starting at index 1
companies = ["Tesla", "SpaceX", "Amazon", "Apple", "Google"]
print(companies[1:])

# Access elements between specific indices
companies = ["Tesla", "SpaceX", "Amazon", "Apple", "Google"]
print(companies[1:4])

# Append a list to another list
ranks = [1, 2, 3, 4, 5]
sports = ["basketball", "football", "baseball", "boxing", "soccer"]

sports.extend(ranks)
print(sports)

# Append an item to a list
sports = ["basketball", "football", "baseball", "boxing", "soccer"]
print(sports)
sports.append('skateboard')
print(sports)

# Adding an item to a specific index of a list
car_brands = ["Tesla", "BMW", "Ford"]
car_brands.insert(1, 'Mercedes-Benz')
print(car_brands)

# Remove a specific element form a list
car_brands = ["Tesla", "BMW", "Ford"]
car_brands.remove('BMW')
print(car_brands)

# Remove all elements from a list
car_brands = ["Tesla", "BMW", "Ford"]
car_brands.clear()
print(car_brands)

# Removing the last element from a list
car_brands = ["Tesla", "BMW", "Ford"]
car_brands.pop()
print(car_brands)

# Check if a specific element exist in a list
sports = ["basketball", "football", "baseball", "boxing", "soccer"]
print(sports.index('boxing'))

# How many times does the same element exist in a list
sports = ["basketball", "football", "baseball", "boxing", "soccer", "boxing"]
print(sports.count("boxing"))

# Sort a list in alphabetical or numerical order
sports = ["basketball", "football", "baseball", "boxing", "soccer"]
ranks = [9, 2, 4, 7, 1]
sports.sort()
ranks.sort()
print(sports)
print(ranks)

# Reverse the order of a list
ranks = [0, 1, 2, 3, 4, 5]
ranks.reverse()
print(ranks)

# Make a copy of a list
car_brands = ["Tesla", "BMW", "Ford"]
my_car_brands = car_brands.copy()
print(my_car_brands)

