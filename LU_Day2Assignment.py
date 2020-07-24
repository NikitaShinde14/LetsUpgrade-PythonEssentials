#1 Use of back slash
print("hello\
      everyone")

#2 Triple quotes
print("""(”)….(”)
( ‘ o ‘ )
(”)–(”)
(””’)-(””’)""")

#3 Use of single and double quotes
print("India's capital is Delhi")

#4 Escape sequence of string
print("Good\tluck")
print("New\nline")

#5 Formatted o/p
name="John"
marks=90.65
age=18
print("Name: %s,Marks: %.2f,age: %d" %(name,marks,age))
print(f"Name: {name},Marks: {marks},age: {age}")

#6 Python Operators
# Arithmetic
print(5**3)

# Comparison
a=10
print(a%2!=0)

# Assignment
a=20
a+=5
print(a)

# Bitwise
p=4
q=5
print(p | q)

# Logical
x=10
y=20
if x>5 and y<25:
    print("True")

# Membership
word1="Country"
if "Z" not in word1:
    print("Z not in the word Country")

# Identity
val1=25
val2=26
print(val1 is val2)

#7 Operator precedence
print(10**2/50+2)
