#numbers = range(5)
'''
start is 0 by default,
step is 1 by default,
range generated from 0 to 4
'''
'''
print (list(numbers))
# step is 1 by default, range generated from 10 to 19
numbers = range(10,20)
print (list(numbers))
# range generated from 1 to 10 increment by step of 2
numbers = range(1, 10, 2)
print (list(numbers))
'''
#factorial

N = int(input('Enter the number to fine the factorial of: '))
fact = 1
for x in range(1,N+1):
    fact= fact*x
print('The factorial of {} is {}'.format(N,fact))