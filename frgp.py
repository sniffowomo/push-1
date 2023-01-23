#!/usr/bin/env python3
'''
The following fish shell code 

#!/bin/fish 
function gpx 
    for i in (seq 1 $argv) 
        echo "----------------------------"
        echo "Commit Number" $i
        git add .
        git commit --allow-empty --allow-empty-message -m "$i"
        git push --progress
        echo "----------------------------"
    end 
end

Convert bastard to python

'''

import subprocess

# git add . command - this should be normal one
subprocess.run(["git", "add", "."])

# git commit --allow-empty --allow-empty-message -m ""
subprocess.run(["git", "commit", "--allow-empty",
               "--allow-empty-message", "-m", ""])
