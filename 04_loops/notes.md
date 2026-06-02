LOOPS (ITERATION)

A loop is used to repeat a block of code multiple times.

WHY LOOPS ARE USED:
- to avoid repeating code
- to automate tasks
- to process data
- to work with collections

FOR LOOP:
Used when we know how many times we want to repeat something.

Example:
for i in range(5):
    print(i)

range(5) -> 0, 1, 2, 3, 4

range(start, stop):
for i in range(1, 6):
    print(i)

range(1, 6) -> 1, 2, 3, 4, 5

range(start, stop, step):
for i in range(2, 11, 2):
    print(i)

Output: 2, 4, 6, 8, 10

WHILE LOOP:
A while loop repeats code while a condition is True.

Example:
i = 0
while i < 5:
    print(i)
    i += 1

IMPORTANT:
- avoid infinite loops
- always update the condition variable

BREAK:
Stops the loop immediately.

CONTINUE:
Skips the current iteration.