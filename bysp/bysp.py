__author__ = 'AivanF'
__copyright__ = 'Copyright 2018, AivanF'
__contact__ = 'projects@aivanf.com'
__license__ = """License:
 This software is provided 'as-is', without any express or implied warranty.
 You may not hold the author liable.

 Permission is granted to anyone to use this software for any purpose,
 including commercial applications, and to alter it and redistribute it freely,
 subject to the following restrictions:

 The origin of this software must not be misrepresented. You must not claim
 that you wrote the original software. When use the software, you must give
 appropriate credit, provide a link to the original file, and indicate if changes were made.
 This notice may not be removed or altered from any source distribution."""

from io import BytesIO
import sys

if sys.version_info[0] == 3:
	basestring = str

MAX_SPLITS = 16


def split_iob(whole, split_count):
	"""Return a list with parts of given file-like object, and it's bytes sum.

	For example, if split_count=3, then the whole file will be splitted into byte triples,
	and the 2nd returned file-like object will consist of
	all the 2nd bytes of each triple of a given object.
	"""
	parts = []
	for i in range(split_count):
		parts.append(BytesIO())
	bytes_count = 0
	current_split = 0
	byte = whole.read(1)
	while byte:
		parts[current_split].write(byte)
		current_split = (current_split + 1) % split_count
		bytes_count += 1
		byte = whole.read(1)
	for part in parts:
		part.seek(0)
	return parts, bytes_count


def split_io(*args, **kwargs):
	"""Return a list with parts of given file-like object.

	This function works the same as split_iob, but returns only list, without bytes sum.
	"""
	return split_iob(*args, **kwargs)[0]


def split_file(whole, split_count=None, parts=None, save=True):
	"""Split a file into parts, then save them to the disk or return a list with parts.

	Keyword arguments:
	whole -- filename or file-like object to split
	split_count -- count of parts to create
	parts -- parts filenames 
	save -- if should save on the save, or just return a list of parts
	"""
	if parts is None:
		if split_count is None:
			raise ValueError('At least split_count or parts must be given!')
		if split_count > MAX_SPLITS:
			split_count = MAX_SPLITS
			print('Too many splits! {} used.'.format(MAX_SPLITS))
	else:
		if split_count is None:
			split_count = len(parts)
	if isinstance(whole, basestring):
		filename_given = True
		whole_io = open(whole, 'rb')
	else:
		filename_given = False
		whole_io = whole
	results = split_iob(whole_io, split_count)
	parts_io = results[0]
	if filename_given:
		whole_io.close()
	if save:
		for i, part_io in enumerate(parts_io):
			if parts is None:
				if filename_given:
					name = whole + '.{}.part'.format(i)
				else:
					raise ValueError('If save=True, then parts must be given or whole must be a filename!')
			else:
				name = parts[i]
			with open(name, 'wb') as fl:
				fl.write(part_io.read())
		print('Split done! Bytes sum: {}'.format(results[1]))
	else:
		return parts_io


def combine_iob(parts):
	"""Return file-like object as a combination of given parts, and bytes sum.
	
	The argument is a list with file-like objects.
	This function works as reversion of split_iob function.
	"""
	if len(parts) < 1:
		raise ValueError('Parts list must not be empty!')
	whole = BytesIO()
	bytes_count = 0
	while True:
		done = 0
		for fl in parts:
			byte = fl.read(1)
			if byte:
				bytes_count += 1
				whole.write(byte)
			else:
				done += 1
		if done >= len(parts):
			break
	return whole, bytes_count


def combine_io(parts):
	"""Return file-like object as a combination of given parts.

	This function works the same as combine_iob, but returns only final file, without bytes sum.
	"""
	return combine_iob(filename, parts)[0]


def combine_file(filename=None, parts=None, save=True):
	"""Combine parts into whole object, then save it to the disk or return as file-like object.

	Keyword arguments:
	filename -- it is used to save whole file to the disk (if save=True),
		or to infer parts names (if parts=None)
	parts -- a list with filenames or file-like objects
	save -- if should save the whole to the disk or return it as a file-like object
	"""
	to_close = []
	if parts is None:
		if filename is None:
			raise ValueError('Either filename or parts must be given!')
		parts = []
		split_count = 0
		while True:
			try:
				fl = open(filename + '.{}.part'.format(split_count), 'rb')
				parts.append(fl)
				to_close.append(fl)
				split_count += 1
			except IOError:
				if split_count > 0:
					print('Found {} splits.'.format(split_count))
				break
	else:
		for i in range(len(parts)):
			if isinstance(parts[i], basestring):
				fl = open(parts[i], 'rb')
				parts[i] = fl
				to_close.append(fl)
	results = combine_iob(parts)
	for fl in to_close:
		fl.close()
	whole_io = results[0]
	whole_io.seek(0)
	if save:
		if filename is None:
			raise ValueError('If save=True, the filename must be given!')
		with open(filename, 'wb') as whole:
			whole.write(whole_io.read())
		print('Combine done! Bytes sum: {}'.format(results[1]))
	else:
		return whole_io


usage = """Possible usages:
split <filename> <split_count>
split <filename> <part_name> <part_name> ...
combine <filename>
combine <filename> <part_name> <part_name> ...
"""

use_error = 'Wrong usage!'


def main():
	argcnt = len(sys.argv)
	if argcnt < 3:
		print(usage)
		return

	if sys.argv[1] in ('s', 'split'):
		if argcnt == 4:
			split_file(sys.argv[2], split_count=int(sys.argv[3]))
		else:
			split_file(sys.argv[2], parts=sys.argv[3:])

	elif sys.argv[1] in ('c', 'combine'):
		parts = None
		if argcnt >= 4:
			parts = sys.argv[3:]
		combine_file(sys.argv[2], parts)

	else:
		print(use_error)

if __name__ == '__main__':
	main()
