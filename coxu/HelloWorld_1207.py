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