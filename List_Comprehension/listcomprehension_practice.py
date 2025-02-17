costs=[5,10,3,4]
items = [0,1,0,1]

#practice 1: creating a list comprehension with the function zip and create a variable for the sum values
#values= [-x*y for x, y in zip(costs,items) if y !=0]
#totalcost = sum(values)
#print(totalcost)
#Practice 2: create a list comprehension Using the zip function to combine the elements of both lists
#values= sum([-x*y for x, y in zip(costs,items) if y !=0])
#print(values)
#practice 3: Create a list comprehension with the iteration i
values= sum([-costs[i]*items[i] for i in [0,1,2,3] if i>0])
print(values)
