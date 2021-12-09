
str=input(" enter the word ")
n=int(input(" enter number of copies "))

def copier (str,n):
    result=""
    for i in range (n):
        result = result+str
    return result

print(copier(str,n))    