#Task1: Print hello world
print 'Hello World!'

#Task 2: read input from console and out it
#name = raw_input('What is your name\n')
#print 'HI, %s' % name

#Task3- For loop
friends = ['A', 'B', 'C']
for name,i in enumerate(friends):
    print "iteration {iteration} is {name}". format(iteration = i, name = name)
for name in enumerate(friends):
    print "Name is {name}".format(name = name)

#Task4 - Use a tuple
parents, babies = (1,1)
while babies < 10:
    print 'This generation has {0}'.format(babies)
    parents, babies = (babies, parents + babies)

print'{0}{1}{2}'.format('congyu','like','chouchou')

#Task 5
def greet(name):
    print 'Hello', name

greet('Jack')
greet('Joyce')

# Task 6
import re

for test_string in ['555-1212','ILL-EGAL','555-12LL']:
    if(re.match(r'\d{3}-\d{4}$', test_string)):
        print test_string, 'Is valid'
    else:
        print test_string,'not valid'

# Task 7, dictionaries, generator expression
price = {'apple': 0.40, 'banana': 0.50}
my_purchase = {'apple': 1, 'banana': 6}
grocery_bill = sum(price[fruit] * my_purchase[fruit] for fruit in my_purchase)
print 'I own the grocer $%.2f' % grocery_bill

sum = 0
for key in my_purchase:
    sum += my_purchase[key] * price[key]
print 'my Calculation:',sum