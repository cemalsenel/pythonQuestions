""" 
We have completed the first part of working with files. There is another basic file operation.
 Now it's time to learn how to write to the files. 
 As you can remember that we have two most commonly used modes ('w' and 'a') that allow us to modify the files. 
 Let's examine them one by one :

write() Method :
As we mentioned earlier, we can overwrite a text to a file using 'w' mode, 
which means that every time we use 'w', the content of the file is deleted and new content is written. 
If there isn't any file then it will be created automatically.

Let's create and write string data to a file. We're going to use .write() method for writing :

with open("dummy_file.txt", 'w', encoding="utf-8") as file:  
# we create and open the file

    file.write('This is the first line of my text file')  
    # writes str data into file

with open("dummy_file.txt", 'r', encoding="utf-8") as file:
    print(file.read())  # reads the content of the 'dummy_file'

Now let's repeat the process and see what happens. This time the file (dummy_file) exists :

with open("dummy_file.txt", 'w', encoding="utf-8") as file:
    file.write('This is the new line for my dummy_file')  
    # we write new str data into it 

with open("dummy_file.txt", 'r', encoding="utf-8") as file:
    print(file.read())  # reads the content of the 'dummy_file'

As you can see in the output, the previous content has been deleted and replaced with new content.
When you write strings to a file using the .write() method, the string data is written exactly as it is. 
Whenever you use .write() method, each string joined together into one. 
Therefore you have to put newline characters (\n), separators or spaces, etc. manually if you want. 
Consider the following example :

with open("dummy_file.txt", 'w', encoding="utf-8") as file:
    file.write('My first sentence')
    file.write('My second sentence,')
    file.write('My third sentence\n')
    file.write('My fourth sentence ')
    file.write('My last sentence')

with open("dummy_file.txt", 'r', encoding="utf-8") as file:
    print(file.read())

output:
My first sentenceMy second sentence,My third sentence
My fourth sentence My last sentence

Now, think of that we have a list of fruit names. 
Let's write them to a file each on separate lines one after another.

fruits = ['Banana', 'Orange', 'Apple', 'Strawberry', 'Cherry']

with open("fruits.txt", 'w', encoding="utf-8") as file:
    for basket in fruits:
        file.write(basket + '\n')  # adds a newline character to each string
   
with open("fruits.txt", 'r', encoding="utf-8") as file:
    print(file.read())

with open("fruits.txt", 'r', encoding="utf-8") as file:
    print(file.readlines())  # reads and displays entire lines in a list

output:
Banana
Orange
Apple
Strawberry
Cherry

['Banana\n', 'Orange\n', 'Apple\n', 'Strawberry\n', 'Cherry\n']

Likewise, you can write your text to the file by using any character you want instead of the newline character. 
For example, if you want to separate the strings by a tab character, you should use '\t'.


---------------------------------------------------------------------------
Writing to File with '.writelines' Method
.writelines() Method :
There is another method for writing data to the files. It is .writelines() method. 
Unlike .write() method, .writelines() takes the iterable sequence of strings and writes them to the file. 
The difference between these two methods is just similar to the logic of difference between .read() and .readlines().
Let's use the same list of the fruits again but this time in a little bit different way. 
We should choose the line separators ourselves without using for loop. Let's see how we do it :

fruits = ['Banana\n', 'Orange\n', 'Apple\n', 'Strawberry\n', 'Cherry\n']

with open("fruits.txt", 'w', encoding="utf-8") as file:
    file.writelines(fruits)  # takes an iterator for writing
   
with open("fruits.txt", 'r', encoding="utf-8") as file:
    print(file.read())

with open("fruits.txt", 'r', encoding="utf-8") as file:
    print(file.readlines())

output:

Banana
Orange
Apple
Strawberry
Cherry

['Banana\n', 'Orange\n', 'Apple\n', 'Strawberry\n', 'Cherry\n']
------------------------------------------------------
Write a code that inserts a newline char \n to between lines of the text of the 'fishes.txt' file 
and reads the new content of that file. 


with open('fishes.txt', 'r', encoding = "utf-8") as sea:
    fish_lines = sea.readlines()

with open('fishes.txt', 'w', encoding = "utf-8") as sea:
    for reef in fish_lines:
        sea.write(reef + '\n')
        
with open('fishes.txt', 'r', encoding = "utf-8") as sea:
    print(sea.read())
----------------------------------------------------------------------
Appending to File using 'a' Mode:
Unlike the previous writing mode ('w'), 
in most cases when we want to add new content to a file, deleting the existing content is undesirable. 
Therefore, there is a need for another mode 
that both keeps the existing content of the file and saves the new content to the continuation of the file. 
In Python, we meet this need with 'a' mode which stands for append.

Well then, how we do that appending process. 
Let's add melon to our fruits.txt file as the last line. 
Let's remember our fruits : ['Banana\n', 'Orange\n', 'Apple\n', 'Strawberry\n', 'Cherry\n']


fruits = ['Banana\n', 'Orange\n', 'Apple\n', 'Strawberry\n', 'Cherry\n']

with open("fruits.txt", 'w', encoding="utf-8") as file:
    file.writelines(fruits)  # creates a file containing the elements of the list

with open("fruits.txt", 'r', encoding="utf-8") as file:
    print(file.read())  # reads the content of the file

with open("fruits.txt", 'a', encoding="utf-8") as file:
    file.write('Melon\n')  # adds "Melon" to the end of the existing file
   
with open("fruits.txt", 'r', encoding="utf-8") as file:
    print(file.read())  # reads the last content of the file

with open("fruits.txt", 'r', encoding="utf-8") as file:
    print(file.readlines())

output:

Banana
Orange
Apple
Strawberry
Cherry

Banana
Orange
Apple
Strawberry
Cherry
Melon

['Banana\n', 'Orange\n', 'Apple\n', 'Strawberry\n', 'Cherry\n', 'Melon\n']
"""
