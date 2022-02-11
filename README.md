# ContentRemover


This is a simple python program that will remove certain specified chars from a program. A good tool for deleting annoying formatting in text files. 

## Flags

| Flag | Description |
| ----------- | ----------- |
| -T | Includes the '~' character at the start of a file path, useful for Linux systems in starting from the 'home' directory |
| -C | Allows for the use of a string to represent the ignored chars instead of a set of chars with spaces between them |
| -P | Preserves the original file and writes a new file in the same directory |
| -N | Keeps all the instances of newlines in the data for processing (leave this if you want to ignore the newlines, each line will still be written as intended) |
| -H | Shows this help screen    |
