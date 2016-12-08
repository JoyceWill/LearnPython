# Adds up integers in the command line
# Run it in terminal like this
#  python weifengc/Task8-CommandLine.py 1 2 3
import sys

try:
    total = sum(int(arg) for arg in sys.argv[1:])
    print 'sum=', total
except ValueError:
    print 'Please supply integer arguments'
