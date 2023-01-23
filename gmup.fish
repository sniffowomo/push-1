#!/bin/fish 
funtion gpx 
    for i in (seq 1 $argv)
        alias gpp="git add . && git commit --allow-empty --allow-empty-message && git push --progressgit p"