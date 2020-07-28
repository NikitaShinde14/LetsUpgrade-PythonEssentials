#1 Find all occurrence of substring in the given string "what we think we become;we are Python programmers".Print the index values
import re
str1="what we think we become;we are Python programmers"
val=input("enter val: ")
print([i.start() for i in re.finditer(val,str1)])

#2 Explain using islower(),isupper() with different kinds of strings
str2="Welcome everyone with a SMILE"
print(str2.islower())

str2="ALL IS WELL"
print(str2.isupper())