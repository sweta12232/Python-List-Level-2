list = [8,8, 878, 88]
def newlist():
     list[-0], list[-1] = list[-1], list[0]
     return list
     
print(newlist())





