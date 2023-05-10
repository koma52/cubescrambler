from . import trim, MATHLIB_SRC, SCRAMBLE_SRC, SCRAMBLE_333_SRC, MEGA_SCRAMBLE_SRC
import dukpy

#------------------------------------------------------------------------------

file_list = [MATHLIB_SRC, SCRAMBLE_SRC, SCRAMBLE_333_SRC, MEGA_SCRAMBLE_SRC]

@trim
def get_WCA_scramble(n=80):
    """ Gets a WCA scramble of length `n` for a 6x6x6 cube. Defaults to csTimer's default length of 80. """
    return dukpy.evaljs(file_list, scrambleType='wca666', n=n)

@trim
def get_SiGN_scramble(n=80):
    """ Gets a SiGN-notation scramble of length `n` for a 6x6x6 cube. Defaults to csTimer's default length of 80. """
    return dukpy.evaljs(file_list, scrambleType='sign666', n=n)

@trim
def get_edges_scramble(n=8):
    """ Gets an edges scramble of length `n` for a 6x6x6 cube. Defaults to csTimer's default length of 8. """
    return dukpy.evaljs(file_list, scrambleType='edges666', n=n)
