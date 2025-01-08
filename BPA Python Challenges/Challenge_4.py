f = open("BPA Python Challenges/data.txt", "r") # opens data.txt(f)
num_of_lines = 0 # defines the num_of_lines variable
for lines in "data.txt": # for lines in the data.txt file it reads line and if the line is not emty 
    currentline = f.readline() # reads the line it is one and saves as currentline
    if currentline == "": # if the currentline has no text it pass's it
        pass 
    else: # if the line has text it will add one to the num_of_lines value
        num_of_lines += 1 
f.close() # closes file 

f = open("BPA Python Challenges/output.txt", "w") # opens or creates outputs.txt(f)
f.write(f"Number of lines: {num_of_lines}") # writes to file 
f.close() # closes file