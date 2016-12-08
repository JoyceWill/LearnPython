# All examples can be found here : https://wiki.python.org/moin/SimplePrograms


#Task 1 - print hello world
print 'Hello world!'


#Task2 - read input and output it
name = raw_input('What is your name?\n')
print 'Hi, %s' % name


#Task3 - For loop
friends = ['Join', 'Will', 'Joyce']
for i, name in enumerate(friends):
    print "iteration {iteration} is {name}".format(iteration=i, name=name)


#Task4 - Use a tuple
parents, babies = (1,1)
while babies < 10:
    print 'This genration has {0}'.format(babies)
    parents, babies = (babies, parents + babies)


#Task5 - functions

#This is a function, take name as input parameter
def greet(name):
    print 'Hello', name

greet('Jack')
greet('Bob')


# Task 6 import and regular expression

import re

for test_string in ['555-1212', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print test_string, 'is a valid US local phone number'
    else:
        print test_string,'rejected'

# Task 7, dictionaries, generator expression

prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {'apple': 1, 'banana': 6}
grocery_bill = sum(prices[fruit] * my_purchase[fruit] for fruit in my_purchase)
print 'I owe the grocer $%.2f' % grocery_bill

