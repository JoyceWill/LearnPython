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




