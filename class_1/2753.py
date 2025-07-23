n = int(input())

if (n % 4 == 0 and n % 100 != 0):
    print(1)
elif(n % 400 == 0):
    print(1)
else:
    print(0)

# a = int(input())

# if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
#     print('1')
# else:
#     print('0')