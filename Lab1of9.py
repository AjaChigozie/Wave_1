# Browse the complete list of string methods at:
# https://docs.python.org/3/library/stdtypes.html#string-methods 
# and try them out here. Endeavor to copy the link without the first # comment sign beginning it.

# STRING METHOD MANIPULATION
word = "My name is Ozymandias, king of kings."

# str.capitalize()
print(word.capitalize())

# str.count()
print(word.count('M', 0, 50))

# str.casefold()
print(word.casefold())

# str.encode()
print(word.encode('ascii'))

# str.find()
print(word.find('O'))

# str.rfind()
print(word.rfind('s'))

# str.endswith()
if word.endswith('kings.'):
    print(True)
else:
    print(False)

# str.expandtabs()
expand = 'O\tz\ty\tm\ta\tn\td\ti\ta\ts'
print(expand.expandtabs(2))
print(expand.expandtabs(8))

# str.format()
print('\nThis quote says: {}'.format(word), 'Look on my works,ye Mighty, and despair')

# str.title()
name = "gregory"
print(name.title())

# str.isalpha()
r = 'BUBASSSTIS'
print(r.isalpha())

# str.index
index = 'i love python'
print(index.index('h'))

#  str.isnumeric()
h = '12345'
print(h.isnumeric())

# str.isupper()
k = 'yanni'
print(k.isupper())

# str.join()
m = ''
print(m.join('you are'))

# str.replace(old, new[, count])
j = 'I love C# programming language'
print(j.replace('love', 'HATE'))

# str.decimal()
x = input('\nenter a few number: ')
print(x.isdecimal())

# str.isdigit()
print(x.isdigit())

# str.lower
small = '\nDATA SCIENCE'
print(small.lower())