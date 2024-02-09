#sum of series program
num=int(input("Enter the number of terms:"))
sum=0
j=0
for i in range(0,num):
    sum=sum*10+1 #0+1=1  1*10+1=11
    print(sum,end=" ")
    j=j+sum #0+1=1 +11
print()
print("Sum of the series is",j)

#fibonacci series program
num=int(input("Enter the number:"))
a=0
b=1
print(a)
print(b)
for i in range(2,num):
    c=a+b
    a=b
    b=c
    print(c)

#last position of a string 
String="Emma is a data scientist who knows python.Emma works at google"
substring="Emma"
str_index = -1
for i in range(len(String)):
    if String[i:i+len(substring)] == substring:
        str_index = i
print(str_index)

#splitting a string
given_str="Emma-is-a-data-scientist"
a=given_str.split("-")
print("The substrings are:")
for i in a:
    print(i)

#remove empty strings from a list
x=["Emma","Jon","","Kelly",None,"Eric",""]
print("The original list is",x)
modified_list=list(filter(None,x))
print("The modified list is",modified_list)
