salary = [10000, 12000,20000, 15000,40000,5000]
#increase the all salary by 5% whoose salary is less than 15000

newSalary= [  x + 0.05*x  for x in salary if x < 15000]
print(newSalary)