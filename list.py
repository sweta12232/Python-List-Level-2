

#list comprehensive is shorter syntax and generate the new list based on the condition
#newList = [Expression for item in itreable if condition = true]
list = [1,2,6,8,10,15] #normal 
newList = [x for x in list if x%2 == 0]
print(newList)