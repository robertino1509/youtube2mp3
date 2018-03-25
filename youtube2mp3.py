#!/usr/bin/env python

import sys
from subprocess import call

#path
path = "URL_DESTINATION"

# count the arguments
arguments = len(sys.argv) - 1

# main
#param_1= sys.argv[1]
position = 1  
while (arguments >= position): 
    command = "youtube-dl -ciw --extract-audio --audio-format mp3  --audio-quality 0 --output " + path + "%(title)s.%(ext)s " + sys.argv[position]
    call(command.split(), shell=False)
    position = position +1
