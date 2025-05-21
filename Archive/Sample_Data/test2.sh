#!/bin/bash
ls -a

# assign the exit status to a variable
exit_status=$?

# Write the exit status to a new file
echo $exit_status > exit_status2.txt
