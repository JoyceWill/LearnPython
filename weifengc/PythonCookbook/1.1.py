#Unpacking a sequence into separate values
p = (4, 5)

x,y = p

print x
print y

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data

print name
print shares
print price
print date


#If there is a mismatch in the number of element, you will get an error

p = (4, 5)
x, y, z = p

