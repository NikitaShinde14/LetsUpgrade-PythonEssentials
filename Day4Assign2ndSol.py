#1 Find all occurrence of substring in the given string "what we think we become;we are Python programmers".Print the index values

str1 = "what we think we become ; we are Python programmers"
val = input("enter val: ")
s=0
temp=0
cnt=str1.count(val)
while s < cnt:
    temp=str1.find(val,temp+1)
    print(f"{val} is found at {temp}")
    s=s+1