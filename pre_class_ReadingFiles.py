"""
To start working with files, we need to open it first by using a built-in function open(). 
According to the official related Python documents, it has the following parameters :
=> open (file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
----------------------------------------
Let's start by examining the most important parameters of the open() function, mode. 
This parameter has several options that regulate how or for what purpose we open the file. 
These options are as follows :

Character	What it's used for?
'r'     	Open for reading (default). If the file doesn't exist, FileNotFoundError will raise.
'a'	        Open for writing. It will append to the end of the file if it already exists. If there is no file, it will create it.
'w'	        Open for writing. It will be overwritten if the file already exists. If there is no file, it will create it.
'x'	        Open for exclusive creation, it will fail if the file already exists.
'b'	        Open in binary mode.
't'	        Open as a text file (default).
'+'	        Open for updating (reading and writing).

By default, open() function executes opening the file for reading ('r') as a text ('t'). 
In other words, it defaults to 'r' or 'rt' which means open for reading in text mode.

Tips:
Note that, as you can see above, depending on what you are going to do with the file, you can combine the modes according to your needs.
If you want to open and be able to read, modify, and update the existing file you should set the mode as 'r+'.

Another important point we should cover about mode is that ,
you can choose the format in which you want to open the file as text ('t') or binary ('b'). 
According to the official related Python documentation, 
files opened in 'binary' mode return contents as bytes objects without any decoding. 
In 'text' mode, the contents of the file are returned as str, 
the bytes having been first decoded using a platform-dependent encoding or using the specified encoding if given.

In this case, if you want to open a binary file for writing you should set the mode as 'wb'. 
On the other hand, if you want to work with a text file you don't need to specify 't',
 since the default value of mode is already set as 't'.
  So, when opening and writing a text file it's enough to set the mode as 'w'.

Finally, let us examine the differences between the use of 'w' and 'a'. 
Both options are used to modify the file or to write new data to the file. 
However, when you use 'a', the data you want to write will be added at the bottom of the file 
and combined with existing content, 
whereas using 'w' will delete the existing content and add new content each time
--------------------------------------------
You can use the following methods for reading this file :

.read(size)
.readline(size)
.readlines()
using loops

1. .read(size) :

This method is generally the most preferred method for reading files, 
although it depends on the need. This method reads the size bytes (characters) of the file. 
If this parameter is not specified, the entire file is read at once. Let's take an example of how this method works :

sea = open("fishes.txt", 'r')   

print(sea.read())  # displays the entire text content

sea.close()  # be sure to close the file
****Be sure to close the file you opened using the .close() method.
------------------------------------
2. .readline(size) :

Now let's take a look at the second method that we use to read files in the Python. 
This method reads only size bytes from a single line of the text. 
Now let's start to examine this method through an example :

sea = open("fishes.txt", 'r')   

print(sea.readline())  # displays the first line of the text
print(sea.readline())  # displays the second line
print(sea.readline())  # each time it goes to the new line

sea.close()

Tips:
Note that; .readline() reads the entire line.
Pay attention to the output that there are empty lines between each line

Now, let's take a look at an example using the size parameter. 
The first line of the text contains 26 bytes (characters) except the newline char (\n). 
But, note that the newline character (\n) is considered as a part of each line. 
Then the first line of text consists of 27 characters. Let's choose 13 as the size parameter and see what happens :

sea = open("fishes.txt", 'r')   

print(sea.readline(13))
print(sea.readline(13))
print(sea.readline(13))
print(sea.readline(13))

sea.close()

As you can see, 
the .readline(13) reads 13 chars through the line and it continues to read 13 chars each until the line ends, 
and only then passes to the next line. In this example, considering the first line consists of 27 characters,
 the print(sea.readline(13)) syntax can read the entire line in a total of three repetitions. 
 The output has two empty lines. 
 One of them is caused by the last character (\n) of the first line 
 and the other is because of the default empty line that the .readline() method puts between each line.
----------------------------------------------------------------
3. .readlines() :
And the third method in reading the files in Python is .readlines().
It reads the entire file line by line in the list form.
Using our same text file, let's look at the following example on how the output looks like :

sea = open("fishes.txt", 'r')   

print(sea.readlines())

output:
['Orca is a kind of Dolphin.\n', 'Blue Whale is the largest animal known on 
earth.\n', 'Sharks are the sister group to the Rays (batoids).\n', 'The Tuna 
Fish can weigh up to 260 kg.\n', 'Squid and Octopus are in the same class.']

sea.close()

As you can see in the output, all lines are displayed as separate elements of a list. 
You can easily see the fact that the newline character (\n) is a part of the line we've mentioned before.
The position of the stream (cursor) makes sense when using these methods. 
If we make the file read using one of these methods, 
each time we use the print(method) syntax it continues reading from where the cursor is.
 Let's take a look at the following example where .readline() and .readlines() are used together.

sea = open("fishes.txt", 'r')   

print(sea.readline())  # first line
print(sea.readlines())  # the rest of the lines

sea.close()

output:
Orca is a kind of Dolphin.

['Blue Whale is the largest animal known on earth.\n', 'Sharks are the sister 
group to the Rays (batoids).\n', 'The Tuna Fish can weigh up to 260 kg.\n', 
'Squid and Octopus are in the same class.']

You may have noticed that the type of the sea.readlines() object is the list. Let's see it :
sea = open("fishes.txt", 'r')   

print(type(sea.readlines())) # <class 'list'>

sea.close()
-------------------------------------
4. Using Loops :
As we stated before that we can apply different kinds of methods to the file-like object. 
Accordingly, the last method for reading a file is using the lines of the file-like object as an iterator. 
So the most efficient way to read the contents of a file is using the for loop. 
Let's take a look at an example of how we do this.

sea = open("fishes.txt", 'r')   
for line in sea:
    print(line)

sea.close()

output:
Orca is a kind of Dolphin.

Blue Whale is the largest animal known on earth.

Sharks are the sister group to the Rays (batoids).

The Tuna Fish can weigh up to 260 kg.

Squid and Octopus are in the same class.



In this way, especially large text files can be read easily and practically. 
This method gives us the opportunity to read the line we want, as well as freeing us from syntax repetition.
Since the type of sea.readlines() object is a list, 
we can use it as an iterator and read the whole file in the same way.


sea = open("fishes.txt", 'r')   

for line in sea.readlines():
    print(line)

sea.close()

output:
Orca is a kind of Dolphin.

Blue Whale is the largest animal known on earth.

Sharks are the sister group to the Rays (batoids).

The Tuna Fish can weigh up to 260 kg.

Squid and Octopus are in the same class.
-----------------------------------------------------
The Matter of Closing the Files
You should have noticed that in the examples we have given so far regarding file operations, 
whenever we open a file to work with that file using one of the reading methods, after finishing our working we close the file we opened with the close() method.

⚠️Attention ! :
Do not leave the file open.
Keep in mind that closing the file is paramount.
Normally, when the program finishes running, that file is closed. 
But this does not happen at times and people forget to close these files that have been opened while working with them. 
If we do not want to lose the data we are working with, 
we should keep in mind that the file should be closed as soon as our work is finished.

As we mentioned above, we can do the closing process with the close() method,
 but there is a slightly easier way to do this. Using the "with .... as ..." block. 
 In fact, the actual use of the "with ... as ..." block is to make sure that all the necessary functions are called.
  Take a look at the way we use it :

with open("fishes.txt", "r") as sea:
    print(sea.read())  # needs indented code block

output :
Orca is a kind of Dolphin.
Blue Whale is the largest animal known on earth.
Sharks are the sister group to the Rays (batoids).
The Tuna Fish can weigh up to 260 kg.
Squid and Octopus are in the same class.

As you can see, in this case, we don't need to use the close() method to close the file. It does this on its own.
"""
my_file = open("first_file.txt")  # this syntax opens a 'txt' file 

print(type(my_file))
my_file = open("first_file.txt", encoding="utf-8")
# we've used 'utf8' encoding format just the same as the previous one
"""-----------------------------------------------------------------------"""
sea1 = open("first_file.txt",'r')
print(sea1.read())  # displays the entire text content
sea1.close()  # be sure to close the file

"""Now let's do some readings using the size parameter. 
It specifies the sequence number of the characters starting at number 1. """
sea = open("first_file.txt",'r')
print(sea.read(33))  # displays the first 33 chars of the text
print()
print(sea.read(25))  # displays the next 25 chars of the text
print()
sea.seek(0)  # changes the stream (cursor) position to zero
print(sea.read(33))  # displays the first 33 chars again
print()
print(sea.tell())  # returns the current stream (cursor) position

sea.close()
"""Note that; while .read(33) counting the first 33 bytes, 
it covers newline \n and space character of the file text.
The offset= 0 indicating the first character of the text, 
'.seek(offset) method' changes the stream (cursor) position to a given offset. """

sea2 = open("first_file.txt", 'r')   

print(sea2.readline())  # displays the first line of the text
print(sea2.readline())  # displays the second line
print(sea2.readline())  # each time it goes to the new line

sea2.close()

sea3 = open("first_file.txt", 'r')   

print(sea3.readline(13))
print(sea3.readline(13))
print(sea3.readline(13))
print(sea3.readline(13))

sea3.close()

sea4 = open("first_file.txt", 'r')   

print(sea4.readlines())

sea4.close()





