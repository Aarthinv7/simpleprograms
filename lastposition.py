String="Emma is a data scientist who knows python.Emma works at google"
substring="Emma"
str_index = -1
for i in range(len(String)):
    if String[i:i+len(substring)] == substring:
        str_index = i
print(str_index)
