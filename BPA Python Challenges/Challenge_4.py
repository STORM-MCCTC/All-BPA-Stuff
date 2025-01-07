f = open("BPA Python Challenges/data.txt", "r")
num_of_lines=0
for lines in "data.txt":
    currentline = f.readline()
    if currentline == "":
        pass
    else:
        num_of_lines += 1
f.close()

f = open("BPA Python Challenges/output.txt", "w")
f.write(f"Number of lines: {num_of_lines}")
f.close()