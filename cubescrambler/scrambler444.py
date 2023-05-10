from . import trim, MATHLIB_SRC, SCRAMBLE_SRC, SCRAMBLE_333_SRC, SCRAMBLE_444_SRC, MEGA_SCRAMBLE_SRC
import dukpy

#------------------------------------------------------------------------------

file_list = [MATHLIB_SRC, SCRAMBLE_SRC, SCRAMBLE_333_SRC, MEGA_SCRAMBLE_SRC, SCRAMBLE_444_SRC]

@trim
def get_random_state_scramble(n=40):
    """ Gets a random state scramble of length N for a 4x4x4 cube. Defaults to csTimer's default length of 40. """
    return dukpy.evaljs(file_list, scrambleType='random_state', n=n)

@trim
def get_4BLD_scramble(n=40):
    """ Gets a BLD scramble of length N for a 4x4x4 cube. Alias of get_random_state_scramble_scramble. """
    return get_random_state_scramble(n)

@trim
def get_SiGN_scramble(n=40):
    """ Gets a SiGN-notation scramble of length N for a 4x4x4 cube. Defaults to csTimer's default length of 40. """
    return dukpy.evaljs(file_list, scrambleType='sign444', n=n)

@trim
def get_WCA_scramble():
    """ Gets a WCA scramble of a 4x4x4 cube. Takes long!"""
    return dukpy.evaljs(file_list, scrambleType='wca444')

@trim
def get_edges_scramble(n=8):
    """ Gets an edges scramble of length `n` for a 4x4x4 cube. Defaults to csTimer's default length of 8. """
    return dukpy.evaljs(file_list, scrambleType='edges444', n=n)
