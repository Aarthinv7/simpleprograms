def rec(n):
    if(n<0):
        return 0
    else:
        return n+rec(n-1)
n=int(input("Enter the number:"))
print(rec(n))
