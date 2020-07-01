#!/bin/bash

url=$1

#download subs
cd ../subs
youtube-dl --write-auto-sub --skip-download $url

# download videos
cd ../original
youtube-dl -f 22 $url

