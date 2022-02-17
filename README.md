# Slug

## About this Project
A Hobby Programming Language Made In Python.

This is inspired in [Tsoding's Porth](https://gitlab.com/tsoding/porth) Programming Language.

## Quick Start
To display help:
```console
$ ./main.py -h
```

To compile program(WARNING: compiling code is not done yet, so please do not use it until I make it work properly):
```console
$ ./main.py -c <filename>
```

To interpret program:
```console
$ ./main.py -i <filename>
```

## Language Basics
To put a number into a stack and print it you do:
```
put 20 write
```

To drop a number into the stack you do:
```
put 20 write drop
```
REMEMBER: if you dropped a number out of the stack, you cannot use the number again(unless you put it again.)

To add numbers and print it you do:
```
put 20
put 30
+ write
```

To subtract numbers and print it you do:
```
put 30
put 20
- write
```

To multiply numbers and print it you do:
```
put 20
put 30
* write
```

To divide numbers and print it you do:
```
put 2
put 20
/ write
```

To put 2 numbers into the stack and flip it you do:
```
put 10 write
put 20 write
flip write flip write
```
## WARNING!!!
### This in still in development, do this in your own risk.
