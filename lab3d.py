#!/usr/bin/env python3
'''Lab 3 Part 2 script - subprocess'''
# Author ID: smeggeson1

import subprocess

def free_space():
    command = "df -h | grep '/$' | awk '{print $4}'"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    stdout_string = output.decode('utf-8').strip()
    
    return stdout_string

if __name__ == '__main__':
    print(free_space())