from . import trim, MATHLIB_SRC, SCRAMBLE_SRC, SCRAMBLE_333_SRC, MEGA_SCRAMBLE_SRC
import dukpy

#------------------------------------------------------------------------------

file_list = [MATHLIB_SRC, SCRAMBLE_SRC, SCRAMBLE_333_SRC, MEGA_SCRAMBLE_SRC]

@trim
def get_WCA_scramble(n=60):
    """ Gets a WCA scramble of length `n` for a 5x5x5 cube. Defaults to csTimer's default length of 60. """
    return dukpy.evaljs(file_list, scrambleType='wca555', n=n)

@trim
def get_5BLD_scramble(n=60):
    """ Gets a BLD scramble of length N for a 5x5x5 cube. Alias of get_WCA_scramble. """
    return get_WCA_scramble(n)

@trim
def get_SiGN_scramble(n=60):
    """ Gets a SiGN-notation scramble of length `n` for a 5x5x5 cube. Defaults to csTimer's default length of 60. """
    return dukpy.evaljs(file_list, scrambleType='sign555', n=n)

@trim
def get_edges_scramble(n=8):
    """ Gets an edges scramble of length `n` for a 5x5x5 cube. Defaults to csTimer's default length of 8. """
    return dukpy.evaljs(file_list, scrambleType='edges555', n=n)
