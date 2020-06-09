#file_object.read() - read the contents of the file method
#file_object.write() - write to the file method
#file_object.close() - close the object 

# open('<file_name>', '<mode>')

#modes:
# r - read
#r+ - read and write
# w - erase and write
# w+ - erase plus write and read
# r+b = read + binary data ( images)

my_file = open('terminator.txt', 'w+') # This will create a file if not there, when used with the write() method.

my_file.write('Beast\n')
my_file.write('Phoenix\n')
my_file.writelines([
    'Cyclops\n',
    'Bishop\n',
    'Nightcrawler\n'
])

# MUST close the file when done reading or writing! 

my_file.seek(0) # Alternative to read() when a file is opened in w+ mode
# Any write after this statement above will be placed in the next cursor
print(my_file.read())

my_file.close()  # 

my_file = open('terminator.txt', 'r')
print(my_file.read())

my_file.close()


# with statement: At the end of with statement it will call the close() method to close the value

# Format:

with open('honda.txt', 'w+') as car_model:
    car_model.write('Hello Honda\n')
    car_model.write('Fav sucker\n')

# The above creates a file called honda.txt

#To read 

with open('honda.txt', 'r+') as car_model:
    print(car_model.read())

# O/P: Hello Honda
# Fav sucker


with open('honda.txt', 'r+') as new_myfiles:
    for line in new_myfiles.readlines():
        print(line)


# O/P: 


#Hello Honda

#Fav sucker

# Adds additional new lines 





