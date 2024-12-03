#!/bin/bash

# purpose: to write current date time in 
# /home/jaydeep/Desktop/Cron_prac/basic_tsk/dateTime.log file

curr_dt=$(date "+%Y-%m-%d_%H:%M")
#echo "Current date: $curr_dt"

echo "Current dateTime: $curr_dt" >> /home/jaydeep/Desktop/Cron_prac/basic_tsk/dateTime.log
