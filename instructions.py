# functions/instructions module
# this contains implementations of not only COPY, but other instructions as well

import registers 

def COPY(val, reg):
    """Put the value val into the register reg, or raise an exception
    if the register is invalid.
    """
    registers.validate_register_name(reg)
    registers.write_register(reg, registers.get_operand_val(val))
    
    
def ADD(val1, val2, reg): 
    """Add val1 and val2 (which may be registers or numbers) and put the
    result into a register.
    """
    val1 = registers.get_operand_val(val1)
    val2 = registers.get_operand_val(val2)
    registers.write_register(reg, val1 + val2)
    

def SUB(val1, val2, reg): 
    """Add val1 and val2 (which may be registers or numbers) and put the
    result into a register.
    """
    val1 = registers.get_operand_val(val1)
    val2 = registers.get_operand_val(val2)
    registers.write_register(reg, val1 - val2)
    

def MUL(val1, val2, reg): 
    """Add val1 and val2 (which may be registers or numbers) and put the
    result into a register.
    """
    val1 = registers.get_operand_val(val1)
    val2 = registers.get_operand_val(val2)
    registers.write_register(reg, val1 * val2)