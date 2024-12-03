# !/bin/bash

# Directory where the files are stored
directory="/home/jaydeep/Desktop/TempDir"

# Find the oldest file in the directory
oldest_file=$(ls -t "$directory" | tail -n 1)

# Check if the directory is not empty
if [ -z "$oldest_file" ]; then
    echo "directory is empty"
    exit 1
fi

# Full path to the oldest file
oldest_file_path="$directory/$oldest_file"

# Delete the oldest file
rm -f  "$oldest_file_path"

# Log
# time of deletion
curr_time=$(date +%H:%M)
echo "$oldest_file, is Deleted from $oldest_file_path at $curr_time" >> /home/jaydeep/Desktop/TempDir/del_logs.log
echo "-----------------------" >> /home/jaydeep/Desktop/TempDir/del_logs.log

