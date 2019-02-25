# Idea
This is a tiny Python library and command line utility for splitting any binary files into meaningless parts and combining them back. 

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

    12 88 64 97 70 52 76 63 57 02 91 24

It is divided into 4 groups of 3 bytes each:

    (12 88 64) (97 70 52) (76 63 57) (02 91 24)

Which are written as 3 parts:

1. `12 97 76 02`
2. `88 70 63 91`
3. `64 52 57 24`

If a file size is not divisible by parts count, then the last group just won't be full,
and the parts will have a bit (a byte, to be precise) different size.

Of course, the algorithm works much better for the files with compression,
and worse for the row data (having every 3d or 5th letter of a text is not so bad).
Luckily, we can archive any file!
Moreover, many popular formats of pictures, music and video use compression by default.

# Installation

You can download Python file from [GitHub repository](https://github.com/AivanF/ByteSplitter), or simply use PyPI:

    pip install ByteSplitter

# Command line usage patterns

After installation using `pip`, you can use the utility:

1\. Splitting of a file with default names of parts:

- `split <file_name> <split_count>`

2\. Splitting of a file with specified names of parts:

- `split <file_name> <part_name> <part_name>` 

3\. Combining of a file with default names of parts:

- `combine <file_name>`

4\. Combining of a file with specified names of parts:

- `combine <file_name> <part_name> <part_name> ...`

# Command line usage examples

Check the [example folder](https://github.com/AivanF/ByteSplitter/tree/master/example):

1\. Combine user-named part files into whole `result.png`:

- `bysp combine result.png p3 p14 p15`

2\. Split the file into 2 parts with custom names:

- `bysp split result.png abc def`

3\. Split the file into 10 parts with automatically given names `result.png.0.part`, ..., `result.png.9.part`:

- `bysp s result.png 10`

4\. Combine automatically named parts into whole file (Count of parts mustn't be specified if the files have default names):

- `bysp c new-result.png`

Also, you can call BySp in a Python module way: `python -m bysp` or as usual Python file: `bysp.py` (with provided path).

# Python usage

ByteSplitter can be used as a regular Python library: `import bysp`. The code consists of single file and several simple functions with docstrings, so you can easily understand it. The code works well on both Python 2 & 3. Briefly, the functions are:

## split_io

Returns a list of parts as file-like objects.

- `whole` – a file-like, the data to split.
- `split_count` – count of parts.

## split_file
 
Splits a file into parts, then save them to the disk or return a list with parts.

- `whole` – filename or file-like object to split.
- `split_count = None` – count of parts to create; can be passed, if `parts` is given).
- `parts = None` – custom filenames of parts; if not given, default generated names will be used.
- `save = True` – if should save parts to the disk, or return a list of file-like objects.

## combine_io
 
Returns file-like object as a combination of given parts

- `parts` – a list of file-like objects.

## combine_file
 
Combines given parts, then saves final file to the disk or returns it as a file-like object.

- `filename = None` – filename.
- `parts = None` – a list of file-like objects or filenames; if not given, then `filename` aegument will be used to find the parts.
- `save = True` – if should save final file to the disk, or return it as a file-like object.

---

As you can see, the `*_file` functions work the same as `*_io` functions, but have many optional arguments, so are more flexible.

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
