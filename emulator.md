# CPU Emulator

## Introduction

We will be building a simulator/emulator that can read and execute a program written in a simple programming language.

([EXAPUNKS]: http://www.zachtronics.com/exapunks/)

_Disclaimer: EXAPUNKS and its contents, including the EXA language and the
excerpts from the TRASH WORLD NEWS manual used in this document, are a
property of Zachtronics LLC._

## Fundamentals

> Our simple CPU contains **code** and **registers**.  
> **CODE:** This is a list of instructions that tell the CPU what to do. It's
> written in a special computer language specifically designed for them. 
> **REGISTERS:** Think of these are slots that can store numbers. Registers
> can be read and written to by instructions in your code. 

The CPU has two registers:

* The `X` register is a general-purpose storage register. It can store a
  number and initially contains 0.
* The `T` register is a general-purpose storage register like `X`. 

The following abbreviations will be used to represent required operands:

* `R`: A register
* `R/N`: A register, or a number between -9999 and 9999

## Basic operations

### Instructions

For the first part of the problem, we will be focusing on the most basic features and instructions of the language.

* __`COPY R/N R`__
<br>Copy the value of the first operand into the second operand.
* __`ADDI R/N R/N R`__ 
<br>Add the value of the first operand to the value of the second operand and store the result in the third operand.
* __`SUBI R/N R/N R`__
<br>Same as `ADDI`, for substraction.
* __`MULI R/N R/N R`__  
Same as `ADDI`, for multiplication.
* __`DIVI R/N R/N R`__  
Same as `ADDI`, for integral division.
* __`MODI R/N R/N R`__  
Same as `ADDI`, for modulo.
  
As you can see, all of the above operations put their result into a _register_, but the
operands can be either registers or numbers.

Here are a few parsing constraints:
* Any unknown instruction, register or invalid number should result in a crash (e.g., throw an exception)
* Leading spaces (at the start of a line of code) should be ignored
* Empty lines should be ignored

Write a program that can understand a piece of code with any of the above instructions and run it.

### Guidelines

1. It is generally a good idea to start by identifying the inputs and outputs
   of the program. Here, the input is the code for the CPU, which will be just
   plain text. No need to worry about outputs for now; printing the register
   values after each step should be enough. Don't hesitate to add more __`print`__
   lines as needed.

2. The first piece of code you'll need is one that can read a line of code
   and make sense of it. For example, `"ADDI 30 X T"` could be converted into
   `("ADDI", [30, "X", "T"])` or any other structure of your choice. This will
   make it much easier to write the actual running logic. It is at this step
   that you could check if instructions and their operands are valid.

3. Before implementing the instructions, think about how you want to handle
   the registers.
   
4. If you manage to design the code parsing and register handling carefully,
   actually implementing the instructions should be fairly easy! The only
   detail is that you will need to be careful about whether an argument is a
   number or a register name when both are allowed, and choose the correct
   behavior.
   
5. While it's fine to have global variables, for example, for the registers, I
recommend that you have functions that access those variables so that in other 
modules (files) you can call those functions to set the registers and get their
values.

6. I would recommend breaking this up into multiple files (modules).

### Example

Here is an example:

    COPY 70 X
    ADDI X 1 X
    COPY 3 T
    MULI T X T
    SUBI T 1 T

Decomposed, this program will:

1. Set `X` to 70
2. Add 1 to the value of `X` and store that value back in `X`
3. Set `T` to 3
4. Multiply `X` by `T` and store that value in `T`
5. Substract 1 from `T` and store the result in `T`

At the end, `X` should hold 71 and `T` should hold 212.

### Challenge

Here is another example for you to try your code on:

    COPY 647 X
    MODI X 7 T
    DIVI X T X
    MULI T T T
    MULI X T X
    MULI T T T
    ADDI X T X
    DIVI T 9 T
    ADDI X 3 X
    ADDI T X T
    ADDI T X X
    SUBI X T T
    SUBI X T X
    SUBI X T X

What are the values of the registers at the end? As a bonus, can you identify
what operation the last five instructions are effectively doing?

## Thoughts on algorithm
* read the file a line at a time
* skip if empty line
* validate the instruction (first word on the line...COPY, ADDI, etc.)
  * if word is not in my list of valid instructions then bail out (throw an exception)
  * otherwise, it's valid and COPY is the odd one out (takes 2 arguments vs. 3 arguments)
  * count the number of arguments on the line and be sure it's 3 or 4 as needed
    * if not correct, then bail out

```
  valid_commands = 'COPY ADDI ...'.split() # this could be a tuple or some other container

  def COPY(arguments): # words[1:], i.e., the slice of the original line which excludes the instruction

  def validate_args(num_args, ... ) #: pass in "blueprint" for these arguments
      # this function's job might be to validate number of args
      # and "type" of arguments (i.e., they are numbers when they should be and
      # registers when they should be)
      if len(arguments) != num_args: # not valid for COPY
          CRASH!
      # COPY R/N R
      # How do I know that argument[1] is a Register?
      # COPY(['X', 'FOO'])
      
      # classify each argument as register or number

      if we expect a register only and arg not in valid_registers: # [ 'X', 'T' ]
          CRASH!

      # if we can accept a number here, how do we know it's a number?
      try:
          arg = int(arg) # attempt to int-ify the argument
          # we found a number!
      except ValueError:
          # this is not a number, so CRASH!

      # suppose the command was COPY T X and T has 25 in it right now
      return tuple of the validated args converted to operands... (25, 'X')
```

# Our process should be as follows:
0. the entire process should be infused with the idea that we are working together
1. understand the problem
2. identify major components (modules) / pseudocode to explain how they communicate 
3. identify functions (and how they will work) to perform the tasks noted in step 2 (possibly stub them out)
4. do TDD per module, group like functions in TDD together (generate test_*.py files)
5. make tests pass, you can decide who does what
6. put it all together and run the tests here
