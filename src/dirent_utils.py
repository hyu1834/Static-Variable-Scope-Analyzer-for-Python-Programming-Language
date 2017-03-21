# Author: Hiu Hong Yu && Ming-Hung Lu
# University of California, Davis
# Winter 2017 - ECS 240 - Zhendong Su


import sys
import os
import shutil
import io_utils



## @brief remove all file in the list
#@details
# @param f - list of file paths to be remove
# @return 
def remove_files(f):
	for _file in f:
		try:
			os.remove(_file)

		except KeyboardInterrupt:
			sys.exit(0)
		except SystemExit:
			sys.exit(0)
		except Exception as e:
			io_utils.function_stderr("unable to remove %s due to: %s" % (_file,e.message),"e00000101")

## @brief remove single file provided
#@details
# @param f - single file path
# @return None
def remove_file(f):
	try:
		os.remove(f)

	except KeyboardInterrupt:
		sys.exit(0)
	except SystemExit:
		sys.exit(0)
	except:
		error("unable to remove %s" % (f),"e00000102")

## @brief remove everything in the directory provided
#@details
# @param directory_name - path of directory
# @return None
def clear_directory(directory_name):
	try:
		listOfFiles=os.listdir(directory_name)
		for f in listOfFiles:
			if os.path.isdir(directory_name+"/"+f) or os.path.islink(directory_name+"/"+f):
				clear_directory(directory_name+"/"+f)
				os.rmdir(directory_name+"/"+f)
			else:
				os.remove(directory_name+"/"+f)

	except KeyboardInterrupt:
		sys.exit(0)
	except SystemExit:
		sys.exit(0)
	except:
		error("unable to remove %s" % file,"p00000201")

## @brief create new directory with the name and path provided
#@details
# @param directory_name - path of directory and name
# @return True - successfully created
# @return False - Failed
def create_directory(directory_name):
	try:
		if os.path.exists(directory_name):
		#directory already exist# 
			clear_directory(directory_name)
			return(True)
		elif not os.path.exists(directory_name):
			#if not exist, create one#
			os.makedirs(directory_name)
			return(True)
		else:   #if anything else#
			return(False)

	except KeyboardInterrupt:
		sys.exit(0)
	except SystemExit:
		sys.exit(0)
	except:
		warning("unable to locate/create Directory %s"%directory_name)
		return(False)

## @brief create the directory only if the directory does not exist
#@details
# @param directory_name - path of directory and name
# @return directory path
def create_new_directory(self, directory_name):
	if not os.path.exists(directory_name):
		os.makedirs(directory_name)
	return (directory_name+'/')

## @brief list all files in directory, files only, not including sub-directory
#@details
# @param directory_path - path of directory and name
# @return iteratible
def list_files_in_directory(directory_path):
	if not os.path.isdir:
		return []

	return [os.path.join(directory_path,_file) for _file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path,_file))]

## @brief list all files in directory, sub-directory only, not including files
#@details
# @param directory_path - path of directory and name
# @return iteratible
def list_subdir_in_directory(directory_path):
	if not os.path.isdir:
		return []

	return [os.path.join(directory_path,_file) for _file in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path,_file))]

	# for _file in os.path.listdir(directory_name):
	#	 full_path = os.path.join(directory_path,_file)
	#	 if os.path.isdir(os.path.join(directory_path,_file)):
	#		 yield full_path

## @brief list all files in directory
#@details
# @param directory_path - path of directory and name
# @return iteratible
def list_all_in_directory(directory_path):
	if not os.path.isdir:
		return []

	return os.listdir(directory_path)
	# for _file in os.path.listdir(directory_name):
	#	 full_path = os.path.join(directory_path,_file)
	#	 yield full_path

## @brief get the size of specified file
#@details
# @param path - path to specified file
# @return size of file
def get_file_size(path):
	return os.path.getsize(path)

## @brief make a copy of the source file to destination
#@details
# @param source - source file path
# @param destination - destination path
# @return None
def copy_files(source, destination):
	if type(source) == list:
		for src in source:
			shutil.copy2(src, destination)
	else:
		shutil.copy2(source, destination)

## @brief move a file from source to destination
#@details
# @param source - source file path
# @param destination - destination path
# @return None
def move_file(source, destination):
	if type(source) == list:
		for src in source:
			shutil.move(src, destination)
	else:
		shutil.move(source, destination)

## @brief check if given file exist
#@details
# @param path - path to specified file
# @return True - if file exist
# @return False - if file does not exist
def is_file_exist(path):
	if os.path.isfile(path):
		return True
	return False

## @brief check if given directory exist
#@details
# @param path - path to specified file
# @return True - if exist
# @return False - if not exist
def is_directory_exist(path):
	if os.path.isdir(path):
		return True
	return False

## @brief get the base directory name of a given directory
#@details
# @param path - path to specified directory
# @return base directory name
def get_directory_basename(path):
	return os.path.dirname(path)

## @brief get the base file name of a given file
#@details
# @param path - path to specified file
# @return base file name
def get_file_basename(path):
	return os.path.basename(path)

## @brief rename a given file
#@details
# @param source - source file path
# @param destination - destination path with new name
# @return None
def rename_file(source, destination):
	os.rename(source, destination)

## @brief get base file name and it extension
#@details
# @param path - path to specified file
# @return basename - file basename
# @return extension - file extension
def get_file_basename_extension(path):
	return os.path.splitext(os.path.basename(path))

## @brief get the file path without extension
#@details
# @param path - path to specified file
# @return path - path without extension
def get_file_path_without_extension(path):
	return os.path.join(os.path.dirname(path), os.path.basename(path))

## @brief check if a given file is the same as given type by checking extension
#@details
# @param path - path to specified file
# @param _type - extension
# @return True - same extension
# @return False - different extension
def is_file_type(path, _type):
	filename, ext = get_file_basename_extension(path)
	if ext != _type:
		return False

	return True

## @cond
if __name__ == '__main__':
	import sys
	if len(sys.argv) < 2 or len(sys.argv) > 3:
		print('usage: python dirent_util.py <option>[option_arguement]')
		sys.exit(0)

	option = '-l'
	option_arguement = None

	for i in range(1,len(sys.argv)):
		if '-' in sys.argv[i][0]:
			option = sys.argv[i]
		else:
			option_arguement = sys.argv[i]

	if option == '-lf' and option_arguement:
		for _file in list_files_in_directory(option_arguement):
			print(_file)

## @endcond