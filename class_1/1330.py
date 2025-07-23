a = 1
b = 2

a,b = map(int,input().split())

if (a>b):
    print(">")

elif (a == b):
    print("==")
    
else:
    print("<")
