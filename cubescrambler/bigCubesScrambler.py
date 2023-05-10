from . import trim, MATHLIB_SRC, SCRAMBLE_SRC, SCRAMBLE_333_SRC, MEGA_SCRAMBLE_SRC
import dukpy

#------------------------------------------------------------------------------

file_list = [MATHLIB_SRC, SCRAMBLE_SRC, SCRAMBLE_333_SRC, MEGA_SCRAMBLE_SRC]

@trim
def get_8x8x8_scramble(n=120):
    """ Gets a random scramble (SiGN notation) of length `n` for an 8x8x8 cube. """
    return dukpy.evaljs(file_list, scrambleType='sign888', n=n)

@trim
def get_9x9x9_scramble(n=120):
    """ Gets a random scramble (SiGN notation) of length `n` for a 9x9x9 cube. """
    return dukpy.evaljs(file_list, scrambleType='sign999', n=n)

@trim
def get_10x10x10_scramble(n=120):
    """ Gets a random scramble (SiGN notation) of length `n` for a 10x10x10 cube. """
    return dukpy.evaljs(file_list, scrambleType='sign101010', n=n)

@trim
def get_11x11x11_scramble(n=120):
    """ Gets a random scramble (SiGN notation) of length `n` for an 11x11x11 cube. """
    return dukpy.evaljs(file_list, scrambleType='sign111111', n=n)
