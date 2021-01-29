s='g  hello'
x=s.split(' ')
print(x)
print(' '.join(i[0].upper()+i[1:] for i in x if i!='')) #kills the extra space and w/o the if condition its an error
print(' '.join(i.capitalize() for i in x)) #ignores the empty string


''' Output:
['g', '', 'hello']
G Hello
G  Hello'''
