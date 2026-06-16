# Python File Handling — Complete Notes

## What is a file
A file is external storage used to save data permanently outside a Python program.

Common file types:
- .txt (text files)
- .csv (tabular data)
- .log (logs)
- .json (structured data)

Basic idea:
Open → Read/Write → Close (handled automatically with with open)

---

## open() function

open("file.txt", "r")

Syntax:
open(filename, mode)

---

## File modes

- "r" = read (file must exist)
- "w" = write (overwrites file)
- "a" = append (adds to end)
- "x" = create new file (error if exists)
- "r+" = read + write
- "w+" = write + read (overwrites)

---

## with open() (best practice)

Bad:
file = open("data.txt", "r")
content = file.read()
file.close()

Good:
with open("data.txt", "r") as file:
    content = file.read()

Advantages:
- automatically closes file
- safer
- standard in data analytics

---

## Reading files

Read full file:
with open("data.txt", "r") as file:
    content = file.read()

Read line by line:
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())

Read all lines:
with open("data.txt", "r") as file:
    lines = file.readlines()

---

## Writing files

Overwrite file:
with open("data.txt", "w") as file:
    file.write("Hello\n")

Append file:
with open("data.txt", "a") as file:
    file.write("New line\n")

---

## Important methods

write():
- writes text
- does NOT add newline automatically
file.write("text")

writelines():
file.writelines(["a\n", "b\n"])

---

## File paths

Relative path:
open("data.txt")

Absolute path:
open("/Users/name/Desktop/data.txt")

---

## Working directory

import os
print(os.getcwd())

Used to check where Python is running.

---

## Error handling

try:
    with open("missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")

---

## Practical patterns

Logging:
with open("log.txt", "a") as file:
    file.write("Event happened\n")

Data cleaning:
with open("data.txt", "r") as file:
    lines = file.readlines()

clean_lines = [line.strip() for line in lines]

Counting lines:
count = 0
with open("data.txt", "r") as file:
    for line in file:
        count += 1
print(count)

Filtering:
with open("data.txt", "r") as file:
    for line in file:
        if "ERROR" in line:
            print(line.strip())

---

## Memory vs Files

Memory:
- temporary
- fast
- lost after program ends

Files:
- permanent
- slower
- stored on disk

---

## Common mistakes
- forgetting .strip()
- wrong file path
- using "w" instead of "a"
- confusion between read() and readlines()
- not checking working directory

---