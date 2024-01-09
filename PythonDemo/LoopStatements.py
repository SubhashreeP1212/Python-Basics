#range function usage
#range(10) --0 to 10
#range(1,10) start point 1 and end point 10
#range(1.10,2) start point 1,end point 10 and increment by 2

print(list(range(10)))
print(list(range(5,10)))
print(list(range(2,10,3)))
#print only odd numbers
print(list(range(1,10,2)))
#print only even numbers
print(list(range(0,10,2)))
#decreement
print(list(range(10,1,-1)))

#loop statements
#while loop, for loop
# i=1
# while(i<=10):
#     print(i)
#     i=i+1
# print("done")
# #print 10 to 1
# i=10
# while(i>=1):
#     print(i)
#     i=i-1
# print("done")

#for loop
#print 1 to 9
# for i in range(10):
#     print(i)

#print 1 to 10
# for i in range(1,11):
#     print(i)

#print only even numbers
for i in range(0,29,2):
    print(i)
#print odd number
for i in range(1,29,2):
    print(i)

#print in descending order
for i in range(10,0,-1):
    print(i)




