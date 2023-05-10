from . import trim, MATHLIB_SRC, SCRAMBLE_SRC, SCRAMBLE_333_SRC, MEGA_SCRAMBLE_SRC, SKEWB_SRC
import dukpy

#------------------------------------------------------------------------------

file_list = [MATHLIB_SRC, SCRAMBLE_SRC, SCRAMBLE_333_SRC, MEGA_SCRAMBLE_SRC, SKEWB_SRC]

@trim
def get_WCA_scramble():
    """ Gets a WCA scramble of a Skewb. """
    return dukpy.evaljs(file_list, scrambleType='wcaskewb')

@trim
def get_ULRB_scramble():
    """ Gets a ULRB scramble of a Skewb. """
    return dukpy.evaljs(file_list, scrambleType='ulrbskewb')
