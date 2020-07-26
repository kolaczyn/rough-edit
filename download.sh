#!/bin/bash

mkdir ../subs
mkdir ../original

#download subs
#cd ../subs
#youtube-dl --write-auto-sub --yes-playlist --skip-download -o '%(playlist_index)s' $1

# download videos
cd ../original
youtube-dl -f 22 --yes-playlist -o '%(playlist_index)s' $1