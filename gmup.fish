#!/bin/fish 
function gpx 
    for i in (seq 1 $argv)
        $argv = $argv + 1 
        echo "Commit Number" $argv
        git add .
        git commit --allow-empty --allow-empty-message -m ""
        git push 
    end 
end