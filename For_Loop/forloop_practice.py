costs = (5, 10, 3, 4)  # Create a tuple of costs
items = (0, 1, 0, 1)  # Create a tuple of items packed or not
costperitem = []  # Initialize an empty list to store the cost per item

# Loop through both lists simultaneously
for i in range(len(costs)):
    costperitem.append(-1*costs[i] * items[i])  # Multiply corresponding items

print(costperitem)
#Store the sum of the item in a value
setvalue = 0
for j in costperitem:
    setvalue +=j
print(setvalue)

