# integer value
int = 3
print(int)  

# float value
float = 4.5
print(float) 
 


# string (str)
str = 'apna college'
print(str[0:5])
 

str.replace('apna', 'apka')
str.slice(0, 4)
str2 = str.capitalize()


print(str2)
print(str2.endswith('ge')) # it will gives true or false
print(str2.find("Apna"))
print(str2.count('e'))
str3 = str2.replace('Apna', "Apka")
print(str3)  # Output: Apka college


# List
list = ['hello', 2, 'kesy', 'ho' ]
print(list)
list[0] = 'Hi'
print(list)

# tuple immutable cant be change if onmce declared
tup = ('hello', 2, 'kesy', 'ho' )
print(tup)
# tup[0] = 'Hi'



# Dictionary (key, value)
dict = {
    'name': 'Rahul',
    'age': 20,
    'city': 'Delhi',
    'country': 'India',
    'isAdult': True
}

print(dict)
print(dict.keys())
print(dict.values())


# set (Unique Values)
set = {'hi', 2, 'hello', 'hello', 5, 2}
print(len(set))
