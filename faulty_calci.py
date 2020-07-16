#design a faulty calculator for the below problems
#45*3=555, 56+9=77, 56/6 =4

x = int(input('Enter 1st number : '))
y = int(input('Enter 2nd number : '))
z = (input("enter what u wana calculate---> '/','*', '+', '-' :"))
if x==45 and y==3 and z == '*':
    print('your ans is :', 555)
elif x==56 and y==9 and z== '+':
    print('your ans is : 77')
elif x == 56 and y == 6 and z == '/':
    print('your ans is : 4')
elif z == '-':
    print('your ans is :', x - y)
elif z == '/':
    print('your ans is :', x / y)
elif z == '*':
    print('your ans is :', x * y)
elif z == '+':
    print('your ans is :', x + y)
else:
    print('oops! you have entered wrong no.')


