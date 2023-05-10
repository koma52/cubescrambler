from . import trim, MATHLIB_SRC, SCRAMBLE_222_SRC
import dukpy

#------------------------------------------------------------------------------

file_list = [MATHLIB_SRC, SCRAMBLE_222_SRC]

@trim
def get_WCA_scramble():
    """ Gets a WCA random scramble (sub-optimal) of a 2x2x2 cube. """
    return dukpy.evaljs(file_list, scrambleType='wca')

@trim
def get_random_scramble():
    """ Gets a WCA random scramble (sub-optimal) of a 2x2x2 cube. """
    return dukpy.evaljs(file_list, scrambleType='random')

@trim
def get_optimal_scramble():
    """ Gets an optimal random state scramble of a 2x2x2 cube. """
    return dukpy.evaljs(file_list, scrambleType='optimal')
