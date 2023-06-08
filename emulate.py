import registers, instructions

# allow user to enter commands which will be parsed and executed

instruction_mapper = {
    # it's very Pythonic to use a dict instead of a bunch of nest if/elsif statements
    # ...and prior to 3.10, Python did not have a case statement (which is called 'match')
    'COPY': instructions.COPY,
    'ADD' : instructions.ADD,
    'SUB' : instructions.SUB,
    'MUL' : instructions.MUL,
}

while (statement := input()):
    # user types in something like COPY 10 X
    # so let's split the input into words so we can parse it
    instruction, *operands = statement.split()
    
    if instruction in instruction_mapper:
        instruction_mapper[instruction](*operands)
        registers.print_registers()
    else:
        print('unknown instruction:', instruction)
