#Function fileinput.input and class fileinput.FileInput read the standard input when the list of files is empty.

for line in fileinput.input():  # Sensitive
    print(line)

for line in fileinput.FileInput():  # Sensitive
    print(line)

for line in fileinput.input(['setup.py']):  # Ok
    print(line)

for line in fileinput.FileInput(['setup.py']):  # Ok
    print(line)