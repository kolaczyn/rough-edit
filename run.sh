#!/bin/bash

sh clean.sh
python gen-script.py "$1" "$2"
sh rip.sh