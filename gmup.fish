#!/bin/fish 
function gpx 
    for i in (seq 1 $argv) 
        echo "----------------------------"
        echo "Commit Number" $i
        git add .
        git commit --allow-empty --allow-empty-message -m "$i"
        git push 
        echo "----------------------------"
    end 
end