from . import trim, MATHLIB_SRC, SCRAMBLE_SRC, UTIL_SCRAMBLE_SRC
import dukpy

#------------------------------------------------------------------------------

file_list = [MATHLIB_SRC, SCRAMBLE_SRC, UTIL_SCRAMBLE_SRC]

@trim
def get_WCA_scramble():
    """ Gets a WCA scramble for a Rubik's Clock. """
    return dukpy.evaljs(file_list, scrambleType='wcaclock')

@trim
def get_Jaap_scramble():
    """ Gets a Jaap-notation scramble for a Rubik's Clock. """
    return dukpy.evaljs(file_list, scrambleType='jaap')

@trim
def get_concise_scramble():
    """ Gets a concise-notation scramble for a Rubik's Clock. """
    return dukpy.evaljs(file_list, scrambleType='concise')

@trim
def get_efficient_pin_order_scramble():
    """ Gets an efficient pin order scramble for a Rubik's Clock. """
    return dukpy.evaljs(file_list, scrambleType='efficient_pin_order')
