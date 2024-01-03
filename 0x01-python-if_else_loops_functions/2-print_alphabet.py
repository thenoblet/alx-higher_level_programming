#!/usr/bin/python3

## Iterate over ASCII values from 97 to 122
for i in range(97, 123):
    """
    Printing the character corresponding to the current ASCII value
    - Uses the `chr()` function to convert ASCII values to their 
      corresponding characters
    """
    print("{}".format(chr(i)), end='')
