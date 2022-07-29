#
# (C) ehsanha, 2022.
# Ehsan Haghpanah; haghpanah@scenus.com
#

from os import listdir
from os import path

#
# returns a list of sub-folders in provided path
#
# @param    pa : a string representing the path
# @return   a list of sub-folders
#
def get_subfolders(pa: str) -> list:
	return [path.join(pa, dr) for dr in listdir(pa) if (path.isdir(path.join(pa, dr)))]

#
# returns a list of files with the specified extension in provided path
#
# @param    pa : a string representing the path
# @return   a list of files
#
def get_files(pa: str, ex: str) -> list:
	return [path.join(pa, fi) for fi in listdir(pa) if (path.isfile(path.join(pa, fi)) and fi.endswith(ex))]

#
# a recursive routine that traverses the whole provided path 
# to find all files of the specified extension
#
# @param    pa : a string representing the path
# @param    ex : a string representing the file extension
# @param    ls : a list that holds full files' path
# @return   a list of full files' path
#
def find_files(pa: str, ex: str, ls: list) -> list:
	ls.extend(get_files(pa, ex))
	ds = get_subfolders(pa)
	for dr in ds:
		find_files(dr, ex, ls)
	return ls

def main_run() -> None:
	ls = []
	find_files("c:\pycodes", ".py", ls)
	print(ls)

main_run()