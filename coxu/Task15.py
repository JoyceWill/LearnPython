from itertools import groupby
lines = '''
This is the
first paragraph.

This is the second.
'''.splitlines() #splitlines break line into list of string
# accourding to the /n line breaker

#Use intertools.groupby and bool to treturn group of
#condecutive lines that either have content or don't.

for has_chars, frags in groupby(lines,bool):
    if has_chars:
        print ' '.join(frags)