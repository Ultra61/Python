
# Tylor Underwoood
# Introduction to Programming
# November 7th, 2021
import os

error = False # used to check to see if directory path exists
print("Welcome to the file program!")
while error == False:
    directory = input("Input the directory where you would like to save the file: ")
    error = os.path.isdir(directory)
    if error == False: # if path not found asked to retry
        print("error, enter another path...")
    else:
        error == True
file_name = input("What would you like the file to be called (end it in .csv): ") # ask user for name of the file ending in .csv
path = str(directory) + "/" + str(file_name) # concatenate to create path
new_file = open(path, "a") #create a file if specified does not already exist
name = input("What is your name?: ")
address = input("What is your address?: ")
phone_number = input("What is your phone number?: ")
content =  str(name) + " " + str(address) + " " + str(phone_number) # combine user input into a readable form
new_file.write(content) # write content to file
new_file.close() # close file so it can be read
new_file = open(path, "r") # reopen file for reading
print(new_file.read()) # read and print file 
