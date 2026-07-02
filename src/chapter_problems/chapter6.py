import random
import sys
import time

# Multiple Assignments
cat = ["fat", "gray", "loud"]
size, color, disposition = cat


# Matrix
WIDTH = 70  # The number of columns

try:
    # For each column, when the counter is 0, no stream is shown.
    # Otherwise, it acts as a counter for how many times a 1 or 0
    # should be displayed in that column.
    columns = [0] * WIDTH
    while True:
        # Loop over each column:
        for i in range(WIDTH):
            if random.random() < 0.02:  # noqa: PLR2004
                # Restart a stream counter on this column.
                # The stream length is between 4 and 14 characters long.
                columns[i] = random.randint(4, 14)

            # Print a character in this column:
            if columns[i] == 0:
                # Change this " "" to "." to see the empty spaces:
                print(" ", end="")
            else:
                # Print a 0 or 1:
                print(random.choice([0, 1]), end="")
                columns[i] -= 1  # Decrement the counter for this column.
        print()  # Print a newline at the end of the row of columns.
        time.sleep(0.1)  # Each row pauses for one tenth of a second.
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.


""" Practice Questions
1.What is []?
Empty List

2.How would you assign the value "hello" as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
spam.insert("hello", 3)

## For the following three questions, assume spam contains the list ["a", "b", "c", "d"].
3.What does spam[int(int("3" * 2) // 11)] evaluate to?
"d"
4.What does spam[-1] evaluate to?
"d"
5.What does spam[:2] evaluate to?
["a", "b"]

## For the following three questions, assume bacon contains the list [3.14, "cat", 11, "cat", True].
6.What does bacon.index("cat") evaluate to?
1
7.What does bacon.append(99) make the list value in bacon look like?
[3.14, "cat", 11, "cat", True, 99]
8.What does bacon.remove("cat") make the list value in bacon look like?
[3.14, 11, "cat", True]

9.What are the operators for list concatenation and list replication?
concatenation = "+"
replication = "*"
10.What is the difference between the append() and insert() list methods?
append adds to the end, insert adds a value to a specific index
11.What are two ways to remove values from a list?
.remove, or .del
12.Name a few ways that list values are similar to string values.
You can index them, and they"re mutable
13.What is the difference between lists and tuples?
Tuples are non-mutable
14.How do you write the tuple value that has just the integer value 42 in it?
("42")
15.How can you get the tuple form of a list value? How can you get the list form of a tuple value?
tuple(spam) to a tuple, list(spam) to a list
16.Variables that “contain” list values don"t actually contain lists directly. What do they contain instead?
References to values
17.What is the difference between copy.copy() and copy.deepcopy()?
copy.deepcopy can be used on lists of lists
"""

