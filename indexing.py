fruit="mango juice"
print(fruit[0:5])
print(fruit[6:])
print(fruit[1:4])
print(fruit[4:7])
#To find the count of vowels present in the variable fruit
vowels="aeiou"
count=0
for i in vowels:
    for j in fruit:
        if i in j:
            count=count+1
print(count)
