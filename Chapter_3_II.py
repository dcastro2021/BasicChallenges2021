#Practicing Conditionals - 04.28.21

a = 10
b = 20

if a > b:
    print("a is greater than b")
    
if a < b:
    print("a is less than b")
    
if a == b:
    print("a is equal to b")

# Practicing lists - 04.28.21
# When using lists, one must use "[ , ]""

l1 = ["5", "2", "3", "3.4", "apple", "CAR"]

if "apple" in l1:
    print("Fruit in list.")

if "apple" not in l1:
    print("No fruit found.")

# Example #2

st1 = "Coffee Drinks"

if "Coffee" in st1:
    print("Caffeine.")

if "Coffee" not in st1:
    print("No Caffeine.")

# Example #3

print(len(l1))

if len(l1) > 4:
    print("That list is long.")
if len(l1) < 5:
    print("The list is short.")
