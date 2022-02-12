#!/usr/bin/env python3
""" This is the source code for the Slug Programming Language """
""" WARNING: Some of this code is stolen from Tsoding's old Porth source code. """
# Importing Libraries
import os
import sys
argv = sys.argv
# The OPs. It is important for the Programming Language.
OP_PUSH = 0
OP_PLUS = 1
OP_MINUS = 2
OP_DUMP = 3
OP_DROP = 4
COUNT_OPS = 5


token = [
    "put",
    "+",
    "-",
    "write",
    "drop"
    ]
comment = "#"
# The Stack. It stores all the data the programming language parse into a file.
stack = []

# Defining OPs.
def push(x):
    return (OP_PUSH, x)
def plus():
    return (OP_PLUS, )
def minus():
    return (OP_MINUS, )
def write():
    return (OP_DUMP, )


def nextKeyword(program):
    whitespace = ' '
    key = ''
    for p, op in enumerate(program):
        if op != whitespace:
            key += op
        if (p + 1 < len(program)):
            if program[p + 1] == whitespace:
                print(key)
                key = ''

# For running the program.
def com_prog(program): 
    stack = []
    whitespace = ' '
    key = ''
    for p, op in enumerate(program):
        assert COUNT_OPS == 5, "You have instructions not handled properly."
        # print(op)
        if op != whitespace:
            key += op
        if (p + 1 < len(program)):
            if program[p + 1] == whitespace:
                print(key)
                key = ''
        if program[p] == token[0]:
            stack.append(program[p+1])
            print(f"(Debug [`put`]) Stack: {stack}")
            if op != whitespace:
                key += op
        if program[p] == token[3]:
            # TODO: Find way to print/write strings.
            # assert False, "`write` operation is not done yet."
            stack = stack
            a = stack.pop()
            print(f"(Debug [`write`]) Stack: {stack}")
            print(a)
            stack.append(a)
            print(f"(Debug [`write`]) Stack: {stack}")
            if op != whitespace:
                key += op
        if program[p] == token[1]:
            stack = stack
            a = stack.pop()
            b = stack.pop(-1)
            summ = int(a) + int(b)
            stack.append(summ)
            print(f"(Debug [`plus`]) Stack: {stack}")
            if op != whitespace:
                key += op
        if program[p] == token[2]:
            stack = stack
            a = stack.pop()
            b = stack.pop(-1)
            diff = int(b) - int(a)
            stack.append(diff)
            print(f"(Debug [`minus`]) Stack: {stack}")
            if op != whitespace:
                key += op
        if program[p] == token[4]:
            stack = stack
            stack.pop(-1)
            print(f"(Debug [`drop`]) Stack: {stack}")
            if op != whitespace:
                key += op
        # Parsing Comment
        if program[p] == comment:
            # TODO: Find a way to pass comments properly.
            print(f"(Debug [`comment`] Stack: {stack})")
            continue
            if op != whitespace:
                key += op
        # print(key)
        # nextKeyword(program)
def sim_prog(program):
    # TODO: Find a reason not to delete this definition.
    stack = []
    for op in program:
        # For generating operations.
        if op[0] == OP_PUSH:
            stack.append(op[1])
        elif op[0] == OP_PLUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)    
        elif op[0] == OP_MINUS:
            a = stack.pop(-1)
            b = stack.pop(1)
            stack.append(b - a)
        elif op[0] == OP_DUMP:
            a = stack.pop()
            print(a)
        
# TODO: Make the programming language parse a file. (Done.)

''' program = [
    push(5),
    push(6),
    plus(),
    write(),
    push(5),
    push(3),
    minus(),
    write()
]'''
# File handling.
# filename = "test.slug"

# if len(argv) < 2:
# TODO: Find way to fix this crappy argument handling.
filename = argv[1]

if len(argv) > 2:
    assert False, "Invalid subcommand"
    exit(1)

# TODO: Come up for better error handling for wrong file extensions.

"""if len(filename) != ".slug":
    print(filename)
    print("ERROR: Wrong filename")
    exit(1)
"""
# filename = filename
with open(filename, "r") as f:
    program = f.read().split()


com_prog(program)
