#1 Sum of n numbers using while loop:
sum1=0
num1=0
val=int(input("Enter a value: "))
print(f"You entered: {val}")
while num1<val:
    sum1=sum1+num1
    num1 = num1 + 1
print(f"Sum of first {val} numbers (starting from 0) is: {sum1}")


#2 Find if an entered integer is a Prime number:
n=int(input("Enter a number: "))
if n<=1:
    print(f"{n} is neither prime nor composite")
else:
    x=0
    for i in range(2,n):
        if n%i==0:
            x=1
        break
    if x==1:
        print(f"{n} is not a prime no.")
    else:
        print(f"{n} is a prime no.")