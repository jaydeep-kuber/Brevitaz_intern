# this programm create n number of files at desired destication.
import  os
import datetime
import sys
import random,string
print("-----n files generator-----")
# taking number of files 
num = int(input("Enter the number of files you want to generat: "))
# taking prefix in file name
prefix = input("Enter common prefix of filename (temp/tmp/file): ").lower()
# taking file extension
ext = input("Enter file extension without dot (txt, pdf, etc): ").lower()
# do this process to name file unique all time
# taking current date time as first uid
curr_dt = datetime.datetime.now()
timestamp= curr_dt.strftime('%m%d-%H%M%S')
# taking time in micro for more accuracy
uid_dt = curr_dt.microsecond
# take 2 random lower latters as second uid

# taking destiny directory path
dir_path = input("Enter destination directory path: ")
# checking if '/' is present or not of not then add it at the end od path
if(dir_path[-1] != '/' ):
	dir_path += "/"
# error handling
if not os.path.exists(dir_path):
        print(f"Error: The directory '{dest_path}' does not exist.")
        sys.exit(1)
# generate file and save it
for i in range(1, num+1):
	uid_letters = ''.join(random.choices(string.ascii_lowercase, k=2))
	f_name = f"{prefix}{i}_{uid_dt}_{uid_letters}.{ext}"
	f_path = os.path.join(dir_path,f_name)
	open(f_path, 'w').close()
print(f"{num}, files are created at : {dir_path}")
# print(dest_path)

# def get_unique_filename(base_filename):
  #  i = 1
   # while os.path.exists(f"{base_filename}{i}.txt"):
    #    i += 1
   # return f"{base_filename}{i}.txt"
