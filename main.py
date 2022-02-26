#!/usr/bin/env python3

# Copyright 2022, Khyle Isaias (kernelk14) <khyleisaias@gmail.com>
""" This project is in the MIT License. See `LICENSE` for details."""

""" This is the source code for the Slug Programming Language """

""" WARNING: Some of this code is stolen from Tsoding's old Porth source code. """

# Importing Libraries
import os
import getopt
import sys
argv = sys.argv
# The OPs. It is important for the Programming Language.
OP_PUSH = 0
OP_PLUS = 1
OP_MINUS = 2
OP_DUMP = 3
OP_DROP = 4
COUNT_OPS = 10


token = [
    "put",
    "+",
    "-",
    "write",
    "drop",
    "flip",
    "*",
    "/",
    "as",
    ";"
    ]
comment = "#"
ending = token[9]
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
def sim_prog(program): 
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
    def ifValName(program, valName, valGet, value):
        # assert False, "`ifValName` is still broken."
        value = value
        # value_stack = value_stack
        # valGet = value_stack.index(value)
        print(f"(Debug [`callVar`]) valName: {valName}, Before value: {value}, After value: {valGet}, reaching here.")
        key = ''
        if program[p] == token[8]:
            print(f"(Debug [`as` in `write`], valName: {valName}, value: {value}] Stack: {stack})")
            value_stack = value_stack
            valName = program[p+1]
            value = program[p-1]
            valGet = value_stack.index(value) - 1
            value_stack.append(value)
                # value_stack = value_stack
            if program[p-1] == valName:
                valName = valGet
                value_stack.append(valName)
                print(f"(Debug [`callVar`, valName: {valName}, value: {value}] Stack: {stack})")
                # b = value_stack.pop()
                # c = value_stack.swap()
                # value_stack.append(a)
                a = value_stack.pop()
                print(a)
                value_stack.append(value)
                # if op != whitespace:
                #     key += op
        if op != whitespace:
            key += op
    for p, op in enumerate(program):
        #  value_stack = []
        assert COUNT_OPS == 10, "You have instructions not handled properly."
        # print(op)
        if op != whitespace:
            key += op
        if (p + 1 < len(program)):
            if program[p+1] == whitespace:
                print(key)
                key = ''
            elif program[p+1] == ending:
                print("Ending ';' here")
        if program[p] == token[0]:
            stack.append(program[p+1])
            # value_stack.append(program[p+1])
            if program[p] == token[8]:
                # print("Pushing variables, reaching here.")
                a = stack.pop()
                value_stack = value_stack
                valName = program[p+1]
                value = program[p-1]
                # stack.append(a)
                value_stack.append(a)
                # value_stack.append(value)

            # debugPrint(program)
            # print(f"(Debug [`put`]) Stack: {stack}, Value Stack: {value_stack}")
            if op != whitespace:
                key += op
        elif program[p] == token[3]:
            # TODO: Find way to print/write strings.
            # assert False, "`write` operation is not done yet."
            stack = stack
            value_stack = value_stack
            # value = value
            valName = program[p-1]
            # valGet = value_stack.index(value)
            # ifValName(program, valName, valGet, value)

            
           
           # debugPrint(program)
            
            # print(f"(Debug [`write`]) Stack: {stack}, Value Stack: {value_stack}")
            
            if program[p-1] == valName:
                value = stack.pop(-1)
                if (value == value):
                    stack.append(value)
                    valGet = stack.index(value)
                else:
                    valGet = value_stack.index(value)
                # value = value_stack.pop(valGet)
                # print("Calling valName, reaching here.")
                a = stack.pop(valGet)
                # print(f"From Value Stack, valName: {valName}, out: {a}")
                # print(value_stack[valGet])
            
            if len(stack) == 0:
                a = value_stack.pop(valGet)
                value_stack.append(a)
            else:
                a = stack.pop()
                stack.append(a)
 
            
            if program[p-1] == valName:
                valDet = value_stack[valGet]
                # a = value_stack.pop(valGet)
                print(value_stack[valGet - 1])
                value_stack.append(valDet)
                # valGet = valGet
            else:
                print(a)
            # print(f"Stack: {stack}")
            # print(f"Value Stack: {value_stack}")
            if len(stack) == 0:
                value_stack.append(a)
            else:
                stack.append(a)
            # debugPrint(program)
            # print(f"(Debug [`write`]) Stack: {stack}, Value Stack: {value_stack}")
            if op != whitespace:
                key += op
        elif program[p] == token[1]:
            stack = stack
            a = stack.pop()
            b = stack.pop(-1)
            summ = int(a) + int(b)
            stack.append(b)
            stack.append(summ)
            # debugPrint(program)
            # print(f"(Debug [`plus`]) Stack: {stack}")
            if op != whitespace:
                key += op
        elif program[p] == token[2]:
            stack = stack
            a = stack.pop()
            b = stack.pop(-1)
            diff = int(b) - int(a)
            stack.append(diff)
            # debugPrint(program)
            # print(f"(Debug [`minus`]) Stack: {stack}")
            if op != whitespace:
                key += op
        elif program[p] == token[4]:
            stack = stack
            stack.pop(-1)
            # debugPrint(program)
            # print(f"(Debug [`drop`]) Stack: {stack}")
            if op != whitespace:
                key += op
        elif program[p] == token[5]:
            stack = stack
            a = stack.pop()
            b = stack.pop()
            stack.append(a)
            # debugPrint(program)
            # print(f"(Debug [`flip`] Stack: {stack})")           
            stack.append(b)
            # debugPrint(program)
            # print(f"(Debug [`flip`] Stack: {stack})")
            if op != whitespace:
                key += op
        elif program[p] == token[6]:
            stack = stack
            a = stack.pop()
            b = stack.pop(-1)
            prod = int(a) * int(b)
            stack.append(prod)
            # debugPrint(program)
            # print(f"(Debug [`multiply`] Stack: {stack})")
            if op != whitespace:
                key += op
        elif program[p] == token[7]:
            stack = stack
            a = stack.pop()
            b = stack.pop(-1)
            quot = int(b) / int(a)
            stack.append(quot)
            # debugProgram(program)
            # print(f"(Debug [`divide`] Stack: {stack})")
            if op != whitespace:
                key += op
        # TODO (IMPORTANT): Find way to get the location of the value of a variable in the stack/value stack.
        elif program[p] == token[8]:
            stack = stack
            # print(f"`as`, Stack: {stack}")
            value_stack = value_stack
            # print(f"`as`, Value Stack: {value_stack}")
            valName = program[p+1] 
            value = program[p-1]
            valGet = stack.index(value)
            stLen = len(stack)
            print(f"{stLen} objects in the Stack")
            vstLen = len(value_stack)
            print(f"{vstLen} objects in the Value Stack")
            if valGet != value:
                valGet = stack.index(value)   
            
            for v in range(vstLen - 1):
                # print(f"valGet Loop, called {valGet}")
                # valGet = vstLen - valGet
                valGet = vstLen
            # print(f"valGet, value: {stack[valGet]}")
            stack.append(valGet)
                # valGet += 1
                
            # print("valGet iterating loop, reaching here.")
            valGet = stack.index(value)
            # valGet += 1
            # print(f"valGet: called {valGet}, value: {value}")
            # if program[p+1] == valName:
            #     valName = valGet
            # print(f"`as`, Value Stack: {value_stack}")
            # print(f"Value Stack called {value_stack[valGet]}")
            value_stack.append(value)
            # print(f"Value Stack called {value_stack[valGet - 1]}")
            stack.pop()
            # print(f"(Debug [`as` valName: {valName}, value: {value}, Stack: {stack}, Value Stack: {value_stack})")
            print("------------------------------------------------------------------------------------------------")
            # ifValName(valName, valGet, value, value)
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
        """valName = program[p-1]
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
        """
        # print(op)
        # print(key)
        # nextKeyword(program)
def com_prog(program):
    # assert False, "Compiling programs not done yet."
    # TODO: Find a reason not to delete this definition.
    # TODO: Find new language for compiling.
    stack = []
    value_stack = []
    op_stack = []
    key = ''
    whitespace = ' '
    out_file = file_det[0] + ".rs"
    out = open(out_file, "w")
    out.write("use std::io;\n")
    # out.write("using namespace std;\n")
    out.write("fn main() {\n")
    for p, op in enumerate(program):
        if op != whitespace:
            key += op
        if (p + 1 < len(program)):
            if program[p+1] == whitespace:
                print(key)
                key = ''
        if program[p] == token[0]:
            value_stack = value_stack
            op_stack = op_stack
            value_stack.append(program[p+1])
            print("out program reached here,")
            out.write(f"  let ")
            print("This is before the `as` keyword loop")
        elif program[p] == token[8]:
            value_stack = value_stack
            valName = program[p+1]
            op_stack.append(valName)
            print("printing `as` reaching here.")
            out.write(f"{program[p+1]} = {program[p-1]};\n")
            print("Operations reached here.")
            print(f"OP Stack: {op_stack}")
            if op != whitespace:
                key += op        
            # out.write("  printf(\"Hello World\");\n")
        elif program[p] == token[1]:
            # assert False, "the `+` operation is not implemented yet."
            valName = valName
            a = op_stack.pop()
            b = op_stack.pop()
            if program[p+2] == token[0]:
                print("ERROR: Defining operations as a variable.")
                out.write("}\n")
                exit(1)
                # pass
                # assert False, "Defining operations as a variable."
            out.write(f"  let {program[p+2]} = {a} + {b};\n")
            op_stack.append(a)
            op_stack.append(b)
            '''
            if program[p] == token[8]:
                print("`as` keyword to file out, reaching here.")
                out.write(f"  int {program[p+1]} = {program[p-1]};\n")
        
        '''
        elif program[p] == token[2]:
            valName = valName
            a = op_stack.pop()
            b = op_stack.pop()
            out.write(f"  int {program[p+2]} = {a} - {b};\n")
            op_stack.append(a)
            op_stack.append(b)

        elif program[p] == token[3]:
            valName = program[p-1]
            if program[p-1] == token[1]:
                a = value_stack.pop()
                b = value_stack.pop()
                res = int(a) + int(b)
                out.write(f"  println!(\"{res}\");\n")
            elif program[p-1] == token[2]:
                a = value_stack.pop()
                b = value_stack.pop()
                res = int(a) - int(b)
                out.write(f"  println!(\"{res}\");\n")
            elif program[p-1] != program in token:
                out.write(f"  println!(\"")
                out.write("{}\",")
                out.write(f" {program[p-1]})")
            else:
                out.write("  println!(\"{}\"")
                out.write(f", {program[p-1]});\n")
            if op != whitespace:
                key += op
    
        last_op = op_stack[2:]
        op_stack = op_stack
        # for o, os in enumerate(op_stack):
        #     print(op_stack.index(last_op))
        # o = op_stack.pop(-1)
        print(f"OP Stack as of the valName call: {op_stack}")
        print(f"Last OP Call: {op_stack[2:]}")
        # op_stack.append()
        if program[p] == op_stack:
            print("Recognize valname: reaching here.")
            assert False, "You can screw up the transpiled code."
            if op != whitespace:
                key += op
    out.write("}\n")
    
    """for op in program:
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
    """    
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

def usage():
    # print("Slug")
    print("./main.py [args] <filename>")
    print("              -c --compile       Compile program")
    print("              -i --interpret     Interpret program")
    print("              -h --help          Display help")
# File handling.
# filename = "test.slug"
# filename = argv[1]
argList = argv[1:]
opts = "ci:h"
# hlp = "h"
long_opts = ["compile", "interpret", "help"]
# print(argv)
try:
    if len(sys.argv) < 2:
        print("ERROR: No arguments given\n")
        usage()
        exit(1)
    args, vals = getopt.getopt(argList, opts, long_opts)
    for currentArgument , currentValue in args:
        if currentArgument in ("-c", "--compile"):
            try:
                filename = argv[2]
                file_det = os.path.splitext(filename)
                file_ext = file_det[1]
                out_file = file_det[0] + ".rs"
                if file_ext != ".slug":
                    print(filename)
                    print("ERROR: Wrong filename")
                    exit(1)
                with open(filename, "r") as f:
                    program = f.read().split()
                program = program
                com_prog(program)
                os.system(f"rustc {out_file}")
                exit(0)
            except IndexError as e:
                print(e)
                print("ERROR: No filename given")
                exit(1)
        elif currentArgument in ("-i", "--interpret"):
            try:
                filename = argv[2]
                file_det = os.path.splitext(filename)
                file_ext = file_det[1]
                if file_ext != ".slug":
                    print(filename)
                    print("ERROR: Wrong filename")
                    exit(1)
                with open(filename, "r") as f:
                    program = f.read().split()
                program = program
                sim_prog(program)
                exit(0)
            except IndexError:
                print("ERROR: No filename given")
                exit(1)

        elif currentArgument in ("-h", "--help"):
            usage()
            exit(0)
except getopt.error as err:
    print(str(err))
usage()
"""
if len(argv) < 2:
    options = argv[1]
    filename = argv[2]
    print("ERROR: No filename found, exiting")
    exit(1)
    file_det = os.path.splitext(filename)
    file_ext = file_det[1]
    if file_ext != ".slug":
        print(filename)
        print("ERROR: Wrong filename")
        exit(1)

    with open(filename, "r") as f:
        program = f.read().split()
    if options == "-c":
        program = program
        com_prog(program)
    elif options == "-i":
        program = program
        sim_prog(program)
    elif options == filename:
        program = program
        sim_prog(program)
    elif options == NULL:
        print("ERROR: No flags or filename given\n")
        exit(1)
    else:
        print("Invalid Subcommand.\n")
        exit(1)
"""
# if len(argv) < 2:
# TODO: Find way to fix this crappy argument handling.
# if len(argv) > 2:
    # assert False, "Invalid subcommand"
    # exit(1)

# TODO: Come up for better error handling for wrong file extensions.


# filename = filename


