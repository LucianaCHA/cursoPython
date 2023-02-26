name = 'John'
age = 30
#concat
print('My name is ' + name + ' and I am ' + str(age) + ' years old')
# is posiblñe to use format method
print(f'My name is {name} and I am {age} years old')
# is possible to use format method
print('My name is {name} and I am {age} years old'.format(name=name, age=age))

#iteration of strings
s = 'hello world'
for letter in s:
    print(letter)

#reverse
print(s[::-1])

#methods
print(dir("strings methods"))