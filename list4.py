#In python index starts with 0
list = ["Sweta", 11, "Bishnu", 22, "Suraj", 33, "Swopnil"]
print(list[0]) #prints sweta

list = ["Sweta", 11, "Bishnu", 22, "Suraj", 33, "Swopnil"]
print(list[-1]) #print swopnil

list = ["Sweta", 11, "Bishnu", 22, "Suraj", 33, "Swopnil"]
print(list[0:]) #print all the elements in the list

list = ["Sweta", 11, "Bishnu", 22, "Suraj", 33, "Swopnil"]
print(list[::-1]) #print all the elements from the last

list = ["Sweta", 11, "Bishnu", 22, "Suraj", 33, "Swopnil"]
print(list[::-1]) #print all the elements from the last


list = ["Sweta", 11, "Bishnu", 22, "Suraj", 33, "Swopnil"]
print(list[:5]) #print all the elements from the first to fouth


list = ["Sweta", 11, "Bishnu", 22, "Suraj", 33, "Swopnil"]
print(list[3:]) #print all the elements from [22, 'Suraj', 33, 'Swopnil']

list = ["Sweta", 11, "Bishnu", 22, "Suraj", 33, "Swopnil"]
print(list[-3:-1]) #print all the elements from three last[suraj] not including last element[swopnil].

list = ["Sweta", 11, "Bishnu", 22, "Suraj", 33, "Swopnil"]
if "Sweta" in list:
     print("Hello Sweta!\n I believe in you!.")