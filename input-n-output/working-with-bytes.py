# byte object 

print(b'This is how you specify a byte object')

# Each entry in a byte unlike string (which is a char) is an integer between 0-256 

# Bytes are immutable

# bytearray is mutable

print(bytes(10)) # O/P: b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
print(bytes(range(10))) # O/P: b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t'

my_bytes= b"This is a byte object which represents a hex char"

print(my_bytes[0])      #O/P: 84
print(my_bytes[0:1])    # O/P: b'T'

## BYTE-ARRAY

print(bytearray())      # O/P: bytearray(b'') - Empty byte array



#### NOTES 

What is a bytes Object?
A bytes object is an immutable sequence (just like a string) that consists of single bytes of data. Where a string is a sequence of characters, a bytes object is a sequence of bytes. There's also a type called bytearray that is a mutable counterpart of the bytes. A "byte" is an integer from 0 to 256, but we will see them represented using ASCII characters and hexadecimal numbers. Let's create our first bytes object in the REPL:

>>> my_bytes = b"This is a byte"
>>> my_bytes
b'This is a byte'
The b prefix allows us to create a bytes object literal, but we can also use the bytes() constructor method:

>>> bytes(b"This is a byte")
b'This is a byte'
>>> bytes(10)
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
>>> bytes(range(10))
b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t'
What is \x00? A 2 character hexadecimal number encompasses all possible values for an individual byte (0-256). The bytes object will show its representation using 2 digit hexadecimal values unless the value translates to an ASCII character like \x09 being \t.

A big difference between strings and bytes is what is returned when you index the item versus slicing. For a string, you always get a string returned, even for a single index. For bytes, indexing will return an integer; slicing will return a bytes object.

>>> my_bytes
b'This is a byte'
>>> my_bytes[0]
84
>>> my_bytes[0:2]
b'Th'
Bytearrays
There isn't a literal syntax for creating a bytearray object; we need to use the bytearray constructor, which works just like the bytes constructor except that it can also take a bytes object as the argument to create a mutable version.

>>> bytearray()
bytearray(b'')
>>> bytearray(10)
bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
>>> bytearray(range(10))
bytearray(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t')
>>> bytearray(b'Bytes')
bytearray(b'Bytes')
Because bytearrays are mutable, we can use the same assignment operations that we would normally with a list, except that we need to remember that when working with an index, we need to pass in an integer value and when replacing a slice we need to pass in a bytes object.

>>> b_array = bytearray(10)
>>> b_array[0] = b'T'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'bytes' object cannot be interpreted as an integer
>>> b_array[0:1] = b'T'
>>> b_array
bytearray(b'T\x00\x00\x00\x00\x00\x00\x00\x00\x00')
>>> b_array[1] = 0x10
>>> b_array
bytearray(b'T\x10\x00\x00\x00\x00\x00\x00\x00\x00')
Using bytes Mode for Files
To use the bytes mode when reading a file, we'll need to specify whether we're going to read, write, or append and then also add the b mode. Let's open our xmen.txt file in bytes mode:

>>> with open('xmen.txt', 'rb') as my_file:
...     my_file.read()
...
b'Beast\nPhoenix\nCyclops\nBishop\nNightcrawler\n'
>>> with open('xmen.txt', 'rb') as my_file:
...     my_file.readlines()
...
[b'Beast\n', b'Phoenix\n', b'Cyclops\n', b'Bishop\n', b'Nightcrawler\n']
The main difference between text mode and bytes mode is that we need to use bytes objects when writing, and we'll receive bytes objects when reading.

Reading into Bytearrays
Because bytearrays are mutable, we can create them specifying the size and then read that exact amount of information from a file to place into the bytearray.

>>> my_file = open('xmen.txt', 'rb')
>>> b_array = bytearray(10)
>>> my_file.readinto(b_array)
10
>>> b_array
bytearray(b'Beast\nPhoe')
An alternative way to create a bytearray with a specific length and content would be to call read with the length argument that we hadn't used yet and then passing that value into the bytearray constructor:

>>> new_b_array = bytearray(my_file.read(10))
>>> new_b_array
bytearray(b'nix\nCyclop')


