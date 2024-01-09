name,age,salary='Subha',31,10000.5
print(name,age,salary)

#also can be printed approach 2
print("Name is :", name)
print("Age is :", age)
print("Salary is :", salary)

#approach3
print("Name is: %s, Age is: %d, Salary is: %g" %(name,age,salary))

#Approach4
print("Name is:{}, Age is:{}, Salary is:{}" .format(name,age,salary))
print("Age is:{}, Name is:{}, Salary is:{}" .format(name,age,salary))# maintain the order of variables else age will print name and name will print age
print("Age is:{}, Name is:{}, Salary is:{}" .format(age,name,salary))

