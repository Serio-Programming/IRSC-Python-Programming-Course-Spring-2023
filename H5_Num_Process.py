# Homework 5: Numeric Processing
# Program By: Tyler Serio
# File Name: H5_Num_Process.py
# Function: This program reads and writes to files

filename = "random.txt"
try:
    file = open(filename, "r")
except (FileNotFoundError):
    print("That file cannot be found!")
    print("We cannot run the program without the file!")
    print("Make sure the file is in the directory!!")
    input("Press any key to exit ")
    exit()

def read():
    """This function reads the file and outputs its information"""
    print(f"Reading {filename}.")
    for line in file:
        line = line.replace("\n", "")
        print(line)

def count():
    """This function counts the number of lines in the file"""
    file.seek(0)
    print(f"Counting {filename}.")
    count = 0
    for line in file:
        count += 1
    print(f"There are {count} numbers within the file.")
    return count
        
def sumfunc():
    """This function adds together all the numbers in the file"""
    file.seek(0)
    print(f"Adding {filename}.")
    total = 0
    for line in file:
        line = int(line)
        total += line
    print(f"The sum of all numbers in the file is {total}.")
    return total

def aver(y, x):
    """This function finds the average of all the numbers in the file"""
    print(f"Averaging {filename}.")
    z = y / x
    print(f"The average of the numbers in the file is {y} divided by {x}, which is {z}")
    return z

def write():
    """This function writes the results to another file"""
    print("Writing results to a new file!")
    newfilename = "random_output.txt"
    newfile = open(newfilename, "w")
    newfile.write(f"The number of lines in {filename} was {x}\n")
    newfile.write(f"The sum of the numbers in {filename} was {y}\n")
    newfile.write(f"The average of the numbers in {filename} was {z}\n")
    print(f"Done! The new file is called {newfilename}!")
    file.close()
    newfile.close()
    
read()
x = count()
y = sumfunc()
z = aver(y, x)
write()
input("Press any key to exit ")
exit()
