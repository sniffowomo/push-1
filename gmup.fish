#!/bin/fish 
function gpx 
    for i in (seq 1 $argv) 
        echo "Commit Number" $argv
        git add .
        git commit --allow-empty --allow-empty-message -m ""
        git push 
        echo "----------------------------"
    end 
end