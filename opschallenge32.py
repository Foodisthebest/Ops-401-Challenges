#!/usr/bin/python3

# Script Name: Signature-based Malware Detection Part 2 of 3
# Author: Renona Gay, worked off of example in class
# Date of latest revision: 02/14/2024
# Purpose: To identify a file by generating a hash value; used in the security process of hash validation

# PLACEHODER FOR FINAL ASSIGNMENT

#Script generates hashes of files using hashlib library

#Import libraries
import hashlib

#Function that takes filename and makes a hash for the contents of the file
def hash_file(filename):

    #Creat a hash object
    h = hashlib.sha1()

    #Open file for reading in binary mode 
    with open(filename, 'rb') as file:

        #Loop until the end of the file
        chunk = 0
        while chunk != b'':
            #Read 1024 bytes at a time
            chunk = file.read(1024)
            print(chunk)
            h.update(chunk)

    # Return hex representation if the hash object
    return h.hexdigest()

# Substitute file name for the function
message = hash_file("file.log")
print(message)
            
local_variable