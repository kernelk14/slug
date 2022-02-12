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
COUNT_OPS = 9


token = [
    "put",
    "+",
    "-",
    "write",
    "drop",
    "flip",
    "*",
    "/",
    "as"
    ]
comment = "#"
# The Stack. It stores all the data the programming language parse into a file.
stack = []
value_stack = []
# Defining OPs.
def push(x):
    return (OP_PUSH, x)
def plus():
    return (OP_PLUS, )
def minus():
    return (OP_MINUS, )
def write():
    return (OP_DUMP, )


# For running the program.
def com_prog(program): 
    stack = []
    value_stack = []
    whitespace = ' '
    key = ''
    i = 0
    def debugPrint(program):
        for p, op in enumerate(program):
            stack = stack
            # TODO: Make a debug print for all of the instructions.
            if program[p] == token[0]:
                print(f"(Debug [`put` value: {program[p+1]}] Stack: {stack})")
            elif program[p] == token[1]:
                print(f"(Debug [`plus`] Stack: {stack})")
            elif program[p] == token[2]:           
                print(f"(Debug [`minus`] Stack: {stack})")
            elif program[p] == token[3]:
                print(f"(Debug [`write`] Stack: {stack})")
            elif program[p] == token[4]:
                print(f"(Debug [`drop`] Stack: {stack})")
            elif program[p] == token[5]:
                print(f"(Debug [`flip`] Stack: {stack})")
            elif program[p] == token[6]:
                print(f"(Debug [`*`] Stack: {stack})")
            elif program[p] == token[7]:
                print(f"(Debug [`/`] Stack: {stack})")
            elif program[p] == token[8]:
                print(f"(Debug [`as` valName: {program[p+1]}, value: {program[p-1]}] Stack: {stack})")
            elif program[p] == comment:
                print(f"(Debug [`comment`] Stack: {stack})")
#
    for p, op in enumerate(program):
        #  value_stack = []
        assert COUNT_OPS == 9, "You have instructions not handled properly."
        # print(op)
        if op != whitespace:
            key += op
        if (p + 1 < len(program)):
            if program[p + 1] == whitespace:
                print(key)
                key = ''
        if program[p] == token[0]:
            stack.append(program[p+1])
            if program[p] == token[8]:
                value_stack = value_stack
                valName = program[p+1]
                value = program[p-1]
                value_stack.append(value)

            # debugPrint(program)
            print(f"(Debug [`put`]) Stack: {stack}")
            if op != whitespace:
                key += op
        elif program[p] == token[3]:
            # TODO: Find way to print/write strings.
            # assert False, "`write` operation is not done yet."
            stack = stack
            value_stack = value_stack
            if len(stack) == 0:
                a = value_stack.pop()
            else:
                a = stack.pop()
            if program[p] == token[8]:
                value_stack = value_stack
                valName = program[p+1]
                value = program[p-1]
                value_stack.append(value)
                    # value_stack = value_stack
                if program[p-1] == valName:
                    a = value_stack.pop()
                    b = value_stack.pop()
                    c = value_stack.swap()
                    value_stack.append(c)
                    print(a)
                    value_stack.append(value)
                if op != whitespace:
                    key += op
            # debugPrint(program)
            print(f"(Debug [`write`]) Stack: {stack}, Value Stack: {value_stack}")
            print(a)
            if len(stack) == 0:
                value_stack.append(a)
            else:
                stack.append(a)
            # debugPrint(program)
            print(f"(Debug [`write`]) Stack: {stack}, Value Stack: {value_stack}")
            if op != whitespace:
                key += op
        elif program[p] == token[1]:
            stack = stack
            a = stack.pop()
            b = stack.pop(-1)
            summ = int(a) + int(b)
            stack.append(summ)
            # debugPrint(program)
            print(f"(Debug [`plus`]) Stack: {stack}")
            if op != whitespace:
                key += op
        elif program[p] == token[2]:
            stack = stack
            a = stack.pop()
            b = stack.pop(-1)
            diff = int(b) - int(a)
            stack.append(diff)
            # debugPrint(program)
            print(f"(Debug [`minus`]) Stack: {stack}")
            if op != whitespace:
                key += op
        elif program[p] == token[4]:
            stack = stack
            stack.pop(-1)
            # debugPrint(program)
            print(f"(Debug [`drop`]) Stack: {stack}")
            if op != whitespace:
                key += op
        elif program[p] == token[5]:
            stack = stack
            a = stack.pop()
            b = stack.pop()
            stack.append(a)
            # debugPrint(program)
            print(f"(Debug [`flip`] Stack: {stack})")           
            stack.append(b)
            # debugPrint(program)
            print(f"(Debug [`flip`] Stack: {stack})")
            if op != whitespace:
                key += op
        elif program[p] == token[6]:
            stack = stack
            a = stack.pop()
            b = stack.pop(-1)
            prod = int(a) * int(b)
            stack.append(prod)
            # debugPrint(program)
            print(f"(Debug [`multiply`] Stack: {stack})")
            if op != whitespace:
                key += op
        elif program[p] == token[7]:
            stack = stack
            a = stack.pop()
            b = stack.pop(-1)
            quot = int(b) / int(a)
            stack.append(quot)
            # debugProgram(program)
            print(f"(Debug [`divide`] Stack: {stack})")
            if op != whitespace:
                key += op
        elif program[p] == token[8]:
            stack = stack
            value_stack = value_stack
            valName = program[p+1]
            value = program[p-1]
            value_stack.append(value)
            stack.pop()
            print(f"(Debug [`as` valName: {valName}, value: {value}, Stack: {stack}, Value Stack: {value_stack})")
            # value_stack.append(value)
            # debugPrint(program)
            #valName = program[p]         
            #value = program[p+1]
            if program[p] == valName:
                # stack = stack
                value_stack = value_stack
                # if valName == program[p-1]:
                print(f"(Debug [`callVar` valName: {valName}, value: {value} Stack: {stack})")
                value_stack.append(value)
                a = stack.pop()
                value_stack.append(a)
                # value_stack.swap()
                if op != whitespace:
                    key += op
            # if op != whitespace:
            #     key += op
        # TODO: Find way to call local variables.
        valName = program[p-1]
        value = program[p-1]
        if program[p] == valName:
            a = value_stack.pop()
            if len(value_stack) < 2:
                value_stack.append(a)
            else:
                b = value_stack.pop()
            value_stack.append(b)
            value_stack.append(a)
            if op != whitespace:
                key += op
        # Parsing Comment
        elif program[p] == comment:
            # TODO: Find a way to pass comments properly.
            # print(f"(Debug [`comment`] Stack: {stack})")
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
filename = argv[1]
# if len(argv) < 2:
# TODO: Find way to fix this crappy argument handling.
if len(argv) > 2:
    assert False, "Invalid subcommand"
    exit(1)

file_det = os.path.splitext(filename)
file_ext = file_det[1]

# TODO: Come up for better error handling for wrong file extensions.

if file_ext != ".slug":
    print(filename)
    print("ERROR: Wrong filename")
    exit(1)

# filename = filename
with open(filename, "r") as f:
    program = f.read().split()
com_prog(program)


