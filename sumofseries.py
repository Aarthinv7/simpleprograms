num=int(input("Enter the number of terms:"))
sum=0
j=0
for i in range(0,num):
    sum=sum*10+1 #0+1=1  1*10+1=11
    print(sum,end=" ")
    j=j+sum #0+1=1 +11
print()
print("Sum of the series is",j)
