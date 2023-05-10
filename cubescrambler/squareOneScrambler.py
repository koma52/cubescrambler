from . import trim, MATHLIB_SRC, SCRAMBLE_SRC, SCRAMBLE_333_SRC, UTIL_SCRAMBLE_SRC, SCRAMBLE_SQ1_SRC
import dukpy

#------------------------------------------------------------------------------

file_list = [MATHLIB_SRC, SCRAMBLE_SRC, UTIL_SCRAMBLE_SRC, SCRAMBLE_333_SRC, SCRAMBLE_SQ1_SRC]

@trim
def get_WCA_scramble():
    """ Gets a WCA scramble for a Square-1. """
    return dukpy.evaljs(file_list, scrambleType='wcasq1')

@trim
def get_face_turn_metric_scramble(n=40):
    """ Gets a face turn metric scramble of length `n` for a Square-1. Defaults to csTimer's default length of 40. """
    return dukpy.evaljs(file_list, scrambleType='face_turn_metric', n=n)

@trim
def get_twist_metric_scramble(n=20):
    """ Gets a twist metric scramble for a Square-1.  Defaults to csTimer's default length of 20."""
    return dukpy.evaljs(file_list, scrambleType='twist_metric', n=n)
