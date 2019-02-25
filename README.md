# Idea
This is a tiny Python library and command line utility for splitting any binary files into parts and combining them back. 

It can be useful for storing or transferring some kind of valuable data.
While most of modern technologies try to encrypt such data
(though any encription can be hacked, thanks to quantum computing),
keeping the data away is a timeless approach.
Especially if the data is divided into multiple parts, and each part separately is just useless.

# Algorithm

If you have a file with L bytes, and you want to split it into N parts,
then the algorithm will divide your file into groups of bytes with size N,
and each byte of the group will be written into corresponding part.

Let's consider an example, a small file with 12 bytes which we want to devide into 3 parts:

> 12 88 64 97 70 52 76 63 57 02 91 24

It is divided into 4 groups of 3 bytes each:

> (12 88 64) (97 70 52) (76 63 57) (02 91 24)

Which are written as 3 parts:

> 12 97 76 02  
> 88 70 63 91  
> 64 52 57 24  

If a file size is not divisible by parts count, then the last group just won't be full,
and the parts will have a bit (a byte, to be precise) different size.

Of course, the algorithm works much better for the files with compression and worse for the row data
(having every 3d or 5th letter of a text is not so bad). Luckily, we can archive any file!
Moreover, many popular formats of pictures, music and video have compression by default.

# Command line usage patterns

1. Splitting of a file with default names of parts:

>split <file_name> <split_count>  

2. Splitting of a file with specified names of parts:

>split <file_name> <part_name> <part_name> ...  

3. Combining of a file with default names of parts:

>combine <file_name>  

4. Combining of a file with specified names of parts:

>combine <file_name> <part_name> <part_name> ...  

# Command line usage examples

1. Combine user-named part files into whole `result.png`:

>python bysp.py combine result.png p3 p14 p15  

2. Split the file into 2 parts with custom names:

>python bysp.py split result.png abc def  

3. Split the file into 10 parts with automatically given names `result.png.0.part`, ..., `result.png.9.part`:

>python bysp.py s result.png 10  

4. Combine automatically named parts into whole file (Count of parts mustn't be specified if the files have default names):

>python bysp.py c new-result.png  

Note that you will maybe need to specify some relative path to the files.

# Python usage

ByteSplitter can be easily used as a regular Python library. The code consists of single file and several simple functions with docstrings, so you can easily understand it.

## License

 This software is provided 'as-is', without any express or implied warranty.
 You may not hold the author liable.

 Permission is granted to anyone to use this software for any purpose,
 including commercial applications, and to alter it and redistribute it freely,
 subject to the following restrictions:

 The origin of this software must not be misrepresented. You must not claim
 that you wrote the original software. When use the software, you must give
 appropriate credit, provide an active link to the original file, and indicate if changes were made.
 This notice may not be removed or altered from any source distribution.
