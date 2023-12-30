# Example usage of *args Array

name, *line = input().split()    # Takes a input like Pratik 20 30 40 and assign Pratik to name and rest to line list (all as strings)
scores = list(map(float, line))   # Cast all elements of line list to float and generate a list named scores

# Simple Example
# Code
a, *arr1 = [1,2,3,4]
print(arr1)

# Output
[2, 3, 4]

# Example Usage of Walrus Operator
data = [1, 2, 3, 4, 5]
if (length := len(data)) > 3:
    print(f"List length is {length}")

# Output
List length is 5

# Quick Peek in to Syntax from CLI
Eg. For 'list' 
On Console

> dir(list)
Prints
> ['__add__', '__class__', ..., 'insert', 'pop', 'remove', 'reverse', 'sort']

> help(list.pop)
Prints
Help on method_descriptor:

pop(self, index=-1, /)
    Remove and return item at index (default last).
    
    Raises IndexError if list is empty or index is out of range.