costs=[5,10,3,4]
items = [0,1,0,1]
values= [-costs[i]*items[i] for i in [0,1,2,3] if items[i]>0]
print(values)

