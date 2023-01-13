def kaprekar(num):
    """Do Kaprekar!"""
    KAPREKAR_NUMBER = 6174
    # num must be a 4-digit int w/not all digits the same
    # or a string which can be int-ified into above
    
    # so let's int-ify and check that the result is as expected
    num = int(num) # this will throw a ValueError exception if not int-ifiable
    
    # if we get here, then it must be an int
    
    if len(str(num)) != 4: # not a 4-digit int
        raise ValueError
        
    if len(set(str(num))) == 1: # all digits are the same!
        raise ValueError
     
    # Our original version of the function didn't return anything. It just ran until
    # we converged on the Kaprekar number. If we want a test to be able to check the
    # actual calculations, then we need to at least return something.
    #
    # So it's somewhat contrived, but we'll return the first calculation as well as
    # the number of iterations required for convergence. We can probably assume that
    # if we did one calculation correctly, the subsequent calculations will be right.
    
    results = []
    
    while num != KAPREKAR_NUMBER:
        # make a number out of the digits from low to high
        digits_up = sorted(str(num))
        digits_down = sorted(str(num), reverse=True)
        num = int(''.join(digits_down)) - int(''.join(digits_up))
        results.append(num)
    
    if not results:
        return KAPREKAR_NUMBER, 1
    else:
        return results[0], len(results)