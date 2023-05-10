# Write a Python program that can do the following:

# - You have $50

# - You buy an item that is $15, that has a 3% tax

# - Using the print()  Print how much money you have left, after purchasing the item.

money: int = 50
item: int = 15

print(money - item*1.03)


# String Assignment
# String Assignment. (This can be tricky so feel free to watch solution so we can do it together)

# - Ask the user how many days until their birthday

# - Using the print()function. Print an approx. number of weeks until their birthday

# - 1 week is = to 7 days.35

days_by_week: int = 7
days_to_birthday: int = int(input('HOw many days untill your birthday? '))
print(f'{int(days_to_birthday/days_by_week)} week untill your birthday!')

# - Create a list of 5 animals called zoo

# - Delete the animal at the 3rd index.

# - Append a new animal at the end of the list

# - Delete the animal at the beginning of the list.

# - Print all the animals

# - Print only the first 3 animals

zoo = ['lion', 'giraffe', 'owl', 'aligator', 'elephant']
print(zoo)
zoo.pop(3)
print(zoo)
zoo.append('snake')
print(zoo)
zoo.pop(0)
print(zoo)
print(zoo[0:3])

# Given: my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# - Create a while loop that prints all elements of the my_list variable 3 times.

# - When printing the elements, use a for loop to print the elements

# - However, if the element of the for loop is equal to Monday, continue without printing

i = 0

while i < 3:
    i += 1
    for day in my_list:
        if day == 'Monday':
            pass
        print(day)

# Based on the dictionary:

my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}
# - Create a for loop to print all keys and values

# - Create a new variable vehicle2, which is a copy of my_vehicle

# - Add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4

# - Delete the mileage key and value from vehicle2

# - Print just the keys from vehicle2

for attribute in my_vehicle:
	print(attribute, my_vehicle[attribute])
        
vehicle2 = my_vehicle.copy()

vehicle2['number_of_tires'] = 4

vehicle2.pop('mileage')

for i in vehicle2:
    print(i)


    
# - Create a function that takes in 3 parameters(firstname, lastname, age) and

# returns a dictionary based on those values


def new_dict(firstname : str, lastname: str, age : int)-> dict:
     return {
          'Firstname': firstname,
          'Lastname' : lastname,
          'Age': age
     }

print(new_dict('Luciana', 'Cha', 20))


     