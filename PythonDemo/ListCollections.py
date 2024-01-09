mylist1 = [1,2,3,4,5,6,7,8,9]
mylist2 = [1,"hello","world",50.78]
mylist3= list() # empty list
# print(mylist1)
# print(mylist3)
# print(mylist2[3])
# print(mylist2[-1])
# print(mylist2[-3])
# print(mylist2[1:3])
# print(mylist2[-3:-1])

#modify item in list
mylist2[0]="subha"
print(mylist2)

#iterrating
for i in mylist2:
    print(i)

#checking if item exists in list
if "subha" in mylist2:
    print("yes subha is present")
else:
    print("no subha is not present")
#getting length of list
print(len(mylist2))

#insert new items to list using append or insert

mylist2.append(10)
mylist2.insert(0,"Rajat")
# print(mylist2)

#remove item from list
# #pop()
# mylist2.pop(2)#provide index number
# print(mylist2)
#del
# del mylist2[1]
# print(mylist2)

#clear
# mylist2.clear() #clear all items from the list but variable exists
# print(mylist2)

#remove
# mylist2.remove("subha")# ention the value
# print(mylist2)

#Copylist
mylist3=list(mylist2)
print(mylist3)
mylist3=mylist2.copy()
print(mylist3)

#appending two lists
# mylist3=mylist1+mylist2
# print(mylist3)

#appending using loop statements
# for i in mylist1: #appending list1 to list2
#     mylist2.append(i)
# print(mylist2)

#using extend()
mylist1.extend(mylist2) #appending list2 to mylist1
print(mylist1)