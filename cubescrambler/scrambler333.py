from . import trim, MATHLIB_SRC, SCRAMBLE_SRC, SCRAMBLE_333_SRC, CROSS_SRC, MEGA_SCRAMBLE_SRC
import dukpy

# #------------------------------------------------------------------------------

file_list = [MATHLIB_SRC, SCRAMBLE_SRC, CROSS_SRC, SCRAMBLE_333_SRC, MEGA_SCRAMBLE_SRC]

@trim
def get_WCA_scramble():
    """ Gets a WCA scramble of a 3x3x3 cube. """
    return dukpy.evaljs(file_list, scrambleType="wca")

@trim
def get_3BLD_scramble():
    """ Gets a BLD scramble of a 3x3x3 cube. """
    return dukpy.evaljs(file_list, scrambleType="3bld")

@trim
def get_random_scramble():
    """ Gets a random scramble of a 3x3x3 cube. """
    return dukpy.evaljs(file_list, scrambleType="random")

@trim
def get_edges_scramble():
    """ Gets an edges-only scramble of a 3x3x3 cube. """
    return dukpy.evaljs(file_list, scrambleType="edges")

@trim
def get_corners_scramble():
    """ Gets a corners-only scramble of a 3x3x3 cube. """
    return dukpy.evaljs(file_list, scrambleType="corners")

@trim
def get_LL_scramble():
    """ Gets a last layer scramble of a 3x3x3 cube. """
    return dukpy.evaljs(file_list, scrambleType="ll")

@trim
def get_LSLL_scramble():
    """ Gets a last slot last layer scramble of a 3x3x3 cube. """
    return dukpy.evaljs(file_list, scrambleType="lsll")

@trim
def get_ZBLL_scramble():
    """ Gets a Zborowski-Bruchem last layer scramble of a 3x3x3 cube. """
    return dukpy.evaljs(file_list, scrambleType="zbll")

@trim
def get_ZZLL_scramble():
    """ Gets a Zbigniew Zborowski last layer scramble of a 3x3x3 cube. """
    return dukpy.evaljs(file_list, scrambleType="zzll")

@trim
def get_ZBLS_scramble():
    """ Gets a ZBLS scramble of a 3x3x3 cube. """
    return dukpy.evaljs(file_list, scrambleType="zbls")

@trim
def get_F2L_scramble():
    """ Gets an F2L (first two layers) scramble of a 3x3x3 cube. """
    return dukpy.evaljs(file_list, scrambleType="f2l")

@trim
def get_LSE_scramble():
    """ Gets an LSE (last six edges) scramble of a 3x3x3 cube. """
    return dukpy.evaljs(file_list, scrambleType="lse")

@trim 
def get_EOLine_scramble():
    """ Gets an EO line scramble of a 3x3x3 cube. """
    return dukpy.evaljs(file_list, scrambleType="eoline")

@trim
def get_CMLL_scramble():
    """ Gets a CMLL scramble of a 3x3x3 cube. """
    return dukpy.evaljs(file_list, scrambleType="cmll")

@trim
def get_CLL_scramble():
    """ Gets a CLL scramble of a 3x3x3 cube. """
    return dukpy.evaljs(file_list, scrambleType="cll")

@trim
def get_ELL_scramble():
    """ Gets an ELL scramble of a 3x3x3 cube. """
    return dukpy.evaljs(file_list, scrambleType="ell")

@trim
def get_easy_cross_scramble(n):
    """ Gets an 'easy cross' scramble, where the cross can be solved in `n` moves."""
    return dukpy.evaljs(file_list, scrambleType="easy_cross", n=n)

@trim
def get_2genRU_scramble():
    """ Gets a 2-gen scramble with only RU moves for a 3x3x3 cube. """
    return dukpy.evaljs(file_list, scrambleType="2genru")

@trim
def get_2genLU_scramble():
    """ Gets a 2-gen scramble with only LU moves for a 3x3x3 cube. """
    return dukpy.evaljs(file_list, scrambleType="2genlu")

@trim
def get_2genMU_scramble():
    """ Gets a 2-gen scramble with only MU moves for a 3x3x3 cube. """
    return dukpy.evaljs(file_list, scrambleType="2genmu")

@trim
def get_3genFRU_scramble():
    """ Gets a 3-gen scramble with only FRU moves for a 3x3x3 cube. """
    return dukpy.evaljs(file_list, scrambleType="3genfru")

@trim
def get_3genRUL_scramble():
    """ Gets a 3-gen scramble with only RUL moves for a 3x3x3 cube. """
    return dukpy.evaljs(file_list, scrambleType="3genrul")

@trim
def get_3genRrU_scramble():
    """ Gets a 3-gen scramble with only RrU moves for a 3x3x3 cube. """
    return dukpy.evaljs(file_list, scrambleType="3genrru")

@trim
def get_half_turns_scramble():
    """ Gets a half turns-only scramble for a 3x3x3 cube. """
    return dukpy.evaljs(file_list, scrambleType="half_turns")