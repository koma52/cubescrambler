from . import trim, MATHLIB_SRC, PYRAMINX_SRC
import dukpy

#------------------------------------------------------------------------------

file_list = [MATHLIB_SRC, PYRAMINX_SRC]

@trim
def get_WCA_scramble():
    """ Gets a WCA scramble of a Pyraminx. """
    return dukpy.evaljs(file_list, scrambleType='wca')

@trim
def get_optimal_scramble():
    """ Gets an optimal scramble of a Pyraminx. """
    return dukpy.evaljs(file_list, scrambleType='optimal')
