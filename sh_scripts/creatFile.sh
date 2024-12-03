#!/bin/bash

# id for give uniq name of file
id=$(date +%H:%M)

# path where all files will created
dir_path=/home/jaydeep/Desktop/TempDir

# command to create files
touch $dir_path/file_$id.txt

# log for  track progress
echo "file_$id.txt is creted at $id time" >> $dir_path/del_logs.log

