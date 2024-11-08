#!/usr/bin/env python3

# Copyright {{{
# Copyright 2022, Khyle Isaias (kernelk14) <khyleisaias@gmail.com>
""" This project is in the MIT License. See `LICENSE` for details."""

""" This is the source code for the Slug Programming Language """

""" WARNING: Some of this code is stolen from Tsoding's old Porth source code. """
# }}}
# Importing Libraries {{{
import os
import getopt
import sys
# import re
# }}}
VERSION = '0.3.6-12beta'
# Command Line Arguments. {{{
argv = sys.argv
# }}}
# The OPs. It is important for the Programming Language. {{{
OP_PUSH = 0
OP_PLUS = 1
OP_MINUS = 2
OP_DUMP = 3
OP_DROP = 4
COUNT_OPS = 11
# }}}
# Token Lists {{{
token = [
    "put",    # token[0]
    "+",      # token[1]
    "-",      # token[2]
    "write",  # token[3]
    "drop",   # token[4]
    "flip",   # token[5]
    "*",      # token[6]
    "/",      # token[7]
    "as",     # token[8]
    ";",      # token[9]
    "for",    # token[10]
    "..",     # token[11]
    "do",     # token[12]
    "end",    # token[13]
    "while",  # token[14]
    "if",     # token[15]
    "elif",   # token[16]
    "else",   # token[17]
    "use",    # token[18]
    "job",    # token[19]
    "call",   # token[20]
    "inc",    # token[21]
    "dec",    # token[22]
    ]
wl_token = [
    "<",      # wl_token[0]
    ">",      # wl_token[1]
    "=",      # wl_token[2]
    "!",      # wl_token[3]
    "true",   # wl_token[4]
    "false"   # wl_token[5]
    ]
comment = "#"
ending = token[9]
# }}}
# The Stack. It stores all the data the programming language parse into a file. {{{
stack = []
value_stack = []
# }}}
# Defining OPs. {{{
def push(x):
    return (OP_PUSH, x)
def plus():
    return (OP_PLUS, )
def minus():
    return (OP_MINUS, )
def write():
    return (OP_DUMP, )
# }}}

# For running the program. {{{       
def com_prog(program):
    # assert False, "Compiling programs not done yet."
    # TODO: Find new language for compiling.
    # I've changed the transpiled language from C++ to Rust.
    # stack = []
    value_stack = []
    op_stack = []
    key = ''
    whitespace = ' '
    out_file = file_det[0] + ".rs"
    out = open(out_file, "w")
    out.write("#[allow(unused_variables, unused_assignments, unused_imports, unused_mut)]\n")
    out.write("use std::io;\n")
    # out.write("fn main() {\n")
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
            # print("out program reached here,")
            out.write(f"  let ")
            # print("This is before the `as` keyword loop")
        elif program[p] == token[8]:
            value_stack = value_stack
            valName = program[p+1]
            op_stack.append(valName)
            # print("printing `as` reaching here.")
            if program[p-1] == token[1]:
                # print("ERROR: Using operator as a value of a variable.")
                pass
                # com_prog(program)
                # out.write("}\n")
            # TODO: Find ways to parse string literals.
            else:
                out.write(f"mut {program[p+1]} = {program[p-1]};\n")
            # print("Operations reached here.")
            # print(f"OP Stack: {op_stack}")
            if op != whitespace:
                key += op        
            
        elif program[p] == token[1]:
            a = op_stack.pop()
            b = op_stack.pop()
            if program[p+2] == token[0]:
                print("ERROR: Defining operations as a variable.")
                out.write("}\n")
                exit(1)
            elif program[p+2] == token[1]:
                print("ERROR: Defining operations as a variable.")
                out.write("}\n")
                exit(1)
            elif program[p+2] == token[2]:
                print("ERROR: Defining operations as a variable.")
                out.write("}\n")
                exit(1)
            elif program[p+2] == token[3]:
                print("ERROR: Defining operations as a variable.")
                out.write("}\n")
                exit(1)
            elif program[p+2] == token[4]:
                print("ERROR: Defining operations as a variable.")
                out.write("}\n")
                exit(1)
            out.write(f"  let {program[p+2]} = {a} + {b};\n")
            op_stack.append(a)
            op_stack.append(b)
        elif program[p] == token[2]:
            if program[p] == token[8]:
                valName = program[p-1]
            else:
                pass
                # valName = valName
            a = op_stack.pop()
            b = op_stack.pop()
            out.write(f"  let {program[p+2]} = {a} - {b};\n")
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
                out.write("{}\n\",")
                out.write(f" {program[p-1]})")
            elif program[p-1] == '"':
                out.write("  println!(\"")
                out.write(f"{program[p-1]});")
            else:
                out.write("  println!(\"{}\"")
                out.write(f", {program[p-1]});\n")
            if op != whitespace:
                key += op
        elif program[p] == token[10]:
            out.write(f"  for i in {program[p+1]}")
        elif program[p] == token[11]:
            out.write(f"..{program[p+1]} ")
        elif program[p] == token[12]:
           out.write(" {\n  ")
        elif program[p] == token[13]:
            out.write("\n  }\n")
        elif program[p] == token[14]:
            out.write(f"  while ")
            if program[p+1] == wl_token[4]:
                out.write("true")
            elif program[p+1] == wl_token[5]:
                out.write("false")
            else:
                out.write(f"{program[p+1]} ")
                # print("While loop")
                if program[p+2] == wl_token[0]:
                    out.write(f"< {program[p+3]}")
                elif program[p+2] == wl_token[1]:
                    out.write(f"> {program[p+3]}")
                elif program[p+2] == wl_token[2]:
                    out.write(f"== {program[p+3]}")
                elif program[p+2] == wl_token[3]:
                    out.write(f"!= {program[p+3]}")
        elif program[p] == token[15]:
            out.write(f"  if ")
            if program[p+1] == wl_token[4]:
                out.write("true")
            elif program[p+1] == wl_token[5]:
                out.write("false")
            else:
                out.write(f"{program[p+1]} ")
                # print("While loop")
                if program[p+2] == wl_token[0]:
                    out.write(f"< {program[p+3]}")
                elif program[p+2] == wl_token[1]:
                    out.write(f"> {program[p+3]}")
                elif program[p+2] == wl_token[2]:
                    out.write(f"== {program[p+3]}")
                elif program[p+2] == wl_token[3]:
                    out.write(f"!= {program[p+3]}")
        elif program[p] == token[21]:
            out.write(f"  {program[p-2]} += {program[p-1]};\n")
        elif program[p] == token[22]:
            out.write(f"  {program[p-2]} -= {program[p-1]};\n")
        elif program[p] == token[16]:
            out.write("  } else if ")
            if program[p+1] == wl_token[4]:
                out.write("true")
            elif program[p+1] == wl_token[5]:
                out.write("false")
            else:
                out.write(f"{program[p+1]} ")
                # print("While loop")
                if program[p+2] == wl_token[0]:
                    out.write(f"< {program[p+3]}")
                elif program[p+2] == wl_token[1]:
                    out.write(f"> {program[p+3]}")
                elif program[p+2] == wl_token[2]:
                    out.write(f"== {program[p+3]}")
                elif program[p+2] == wl_token[3]:
                    out.write(f"!= {program[p+3]}")
        elif program[p] == token[17]:
            out.write("  } else ")
        elif program[p] == token[18]:
            out.write(f"use {program[p+1]};\n")
        elif program[p] == token[19]:
            out.write(f"fn {program[p+1]}() ")
        elif program[p] == token[20]:
            out.write(f"{program[p+1]}();\n")
        # I don't even know how I will implement the `drop` instruction again.    
        # last_op = op_stack[2:]
        op_stack = op_stack
        # print(f"OP Stack as of the valName call: {op_stack}")
        # print(f"Last OP Call: {op_stack[2:]}")
        if program[p] == op_stack:
            # print("Recognize valname: reaching here.")
            assert False, "You can screw up the transpiled code."
            if op != whitespace:
                key += op
    # out.write("}\n")
# }}}
# Command Line Arguments. {{{
def usage():
    # print("Slug")
    print("slug [args] <filename>")
    print("              -c --compile       Compile program")
    print("              -h --help          Display help")
    print("              -v --version       Display version number")
def com_proc(filename, file_det, file_ext, out_file):
    if file_ext != ".slug":
        print(filename)
        print("ERROR: Wrong filename")
        exit(1)
    with open(filename, "r") as f:
        program = f.read().split()
    program = program
    com_prog(program)
    compile(out_file, file_det)
    exit(0)
def compile(out_file, file_det):
    os.system(f"rustc {out_file}")
    # os.system(f"./{file_det[0]}")
argList = argv[1:]
opts = "ci:hdv"
long_opts = ["compile", "interpret", "help", "delete", "version"]
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
                com_proc(filename, file_det, file_ext, out_file)
            except IndexError as e:
                 print(e)
                 print("ERROR: No filename given")
                 exit(1)
        elif currentArgument in ("-i", "--interpret"):
            try:
                filename = argv[2]
                file_det = os.path.splitext(filename)
                file_ext = file_det[1]
                print("Oh no, I already removed the interpretation mode.\nPlease use the compilation mode instead with the `-c` or `--compile` flag.")
                if file_ext != ".slug":
                    print(filename)
                    print("ERROR: Wrong filename")
                    exit(1)
                with open(filename, "r") as f:
                    program = f.read().split()
                program = program
                # NEWS: I removed the interpretation mode permanently.
                print("Oh no, I already removed the interpretation mode.\nPlease use the compilation mode instead with the `-c` or `--compile` flag.")
                # sim_prog(program)
                exit(0)
            except IndexError:
                print("ERROR: No filename given")
                exit(1)
        # elif currentArgument in ("-d", "--delete")
        elif currentArgument in ("-h", "--help"):
            usage()
            exit(0)
        elif currentArgument in ("-v", "--version"):
            print(f"Slug Programming Language, version {VERSION}\n")
            exit(1)
except getopt.error as err:
    print(str(err))
usage()
# }}}
