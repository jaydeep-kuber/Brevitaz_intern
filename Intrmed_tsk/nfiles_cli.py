import os
import sys
import datetime
import random
import string
import argparse

# initilize parser
parser = argparse.ArgumentParser(description="Generate n files with uniq names")

# adding args with default vals
# default num of files
parser.add_argument('--num', type=int, default=2, help="Number of files to generate(default is 2).")

# default file prefix
parser.add_argument('--prefix', type=str, default="tmp", help="Prefix of filename(default is  tmp).")

# default extension
parser.add_argument('--ext', type=str, default="txt", help="Extension of your file(default is txt).")

# default destination path
parser.add_argument('--path', type=str, default=".", help="Destination directory path(default  is present directory).")

args = parser.parse_args()

# dispaly msg
print("-------n file generator------")

# Get val from args
num = args.num
prefix = args.prefix.lower()
ext = args.ext.lower()
dir_path = args.path


# get uid in dates
curr_dt = datetime.datetime.now()
uid_dt = curr_dt.strftime('%d_%H%M%S')

# cheaking if directory is exist or not.
if not os.path.exists(dir_path):
	print(f"Error: the directory {dir_path} is not exist.")
	sys.exit(1)

# check is '/' is present
if dir_path[-1] != '/':
	dir_path += '/'

# generating files
for i in range(1, num+1):
	uid_ltrs = ''.join(random.choices(string.ascii_lowercase, k=3))
	f_name = f"{prefix}{i}_{uid_dt}_{uid_ltrs}.{ext}"
	f_path = os.path.join(dir_path, f_name)

	#create file
	open(f_path, 'w').close()

# final mesaage
print(f"{num}, files are created at: {dir_path}")
