def function_name(parameters : str) -> str:
    "do something"
    return parameters

#properties

def argumentos(*args):
    print(args)
argumentos(1,2,3,4,5,6,7,8,9,10) # returns a tuple

print('\n####################################')

def argumentos(**kwargs):
    print(kwargs)
argumentos(a=1,b=2,c=3,d=4,e=5,f=6,g=7,h=8,i=9,j=10) # returns a dictionary

print('\n####################################')

def argumentos(*args, **kwargs):
    print(args)
    print(kwargs)
argumentos(1,2,3,4,5,6,7,8,9,10, a=1,b=2,c=3,d=4,e=5,f=6,g=7,h=8,i=9,j=10) # returns a tuple and a dictionary
