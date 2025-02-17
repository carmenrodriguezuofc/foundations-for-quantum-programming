costs = [5, 10, 3, 4]  # Create a list of costs
items = [0, 1, 0, 1]  # Create a list of items packed or not
costperitem = []  # Initialize an empty list to store the cost per item

# Loop through both lists simultaneously
for i in range(len(costs)):
    costperitem.append(-1*costs[i] * items[i])  # Multiply corresponding items

# Calculate the total cost by summing the costperitem list
total_cost = 0
for j in costperitem:
    total_cost += j  # Accumulate the total cost

# Print only the total cost
print(total_cost)  # This will print only the total cost
