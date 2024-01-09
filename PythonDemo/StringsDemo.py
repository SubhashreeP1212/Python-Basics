#creating string variables in multiple ways
#
# s='welcome'
# s="wlcome"
# s=str('wlcome')
# s=str("wlcome")

#empty string
name=''
name=str()
name=""

#mutable :cannot chnage value of variable address
#immutable: can change the value of variable address
#String is immutable
# s="hello"
# print(id(s))
# s="welcome"
# print(id(s))
# print (s*2) #print string 2 times.* is used to print string mulitple times

#Slicing
# str="subhashree"
# print(str[1:5])#ubha #prints from 1 to 5-1 .String index starts from 0
# print(str[:6])#subhas
# print(str[1:])#ubhashree
# print(str[:])#subhashree
# print(str[:-1])#subhashre, -1 removes the last character
# print(str[-1:])#e it prints the last charcter
# print(str[:-2])#subhashr

#ord and chr function
# print(ord('A'))#returns ASCII code
# print(chr(65))#returns character represented by ASCII number

#max, min and len function
# print(max('subha'))
# print(min('subha'))
# print(len('subha'))

#in and not in operators
# s="subhashree"
# print('has'in s)
# print('sree'not in s)

# #count
# print(s.count('h'))

#comparision using relational operators
# print('subha'=='SUBHA')
# print('subha'!='SUBHA')
# print('subha'>"abc")
# print('subha'<'welcome')

#String functions
s='subhashree 123int'
# print(s.isalnum())#if string contains number
# print(s.isalpha())#if string contains only alphabets
# print(s.isdigit())
# print(s.isidentifier())#string contains any python keyword
# print(s.islower())
# print(s.isupper())
# print(s.isspace())

#searching for substrings
# print(s.endswith('int'))
# print(s.startswith('subha'))
# print(s.find(" "))#position of the character
# print(s.find("jkhk"))#-1 means not found
s1=s.capitalize()#capitalise first letter
print(s1)
s2=s.title()
print(s2)
s3=s.lower()
print(s3)
print(s.upper())
s5=s.swapcase()
print(s5)
s6=s.replace("shree","sree")
print(s6)

#reverse a string method 1
s="welcome"
reverse=""
for i in s: #here i is assigned the string chars from last.
    reverse=i+reverse
print(reverse)

#method2
reverse=s[::-1]
print(reverse)
