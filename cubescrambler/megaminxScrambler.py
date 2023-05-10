from . import trim, MATHLIB_SRC, SCRAMBLE_SRC, SCRAMBLE_333_SRC, UTIL_SCRAMBLE_SRC
import dukpy

#------------------------------------------------------------------------------

file_list = [MATHLIB_SRC, SCRAMBLE_SRC, UTIL_SCRAMBLE_SRC, SCRAMBLE_333_SRC]

@trim
def get_WCA_scramble(n=70):
    """ Gets a WCA scramble of length `n` for a Megaminx. Defaults to csTimer's default length of 70. """
    return dukpy.evaljs(file_list, scrambleType='wca', n=n).replace('\n','').replace('  ',' ').replace('  ',' ')

@trim
def get_Carrot_scramble(n=70):
    """ Gets a Carrot-notation scramble of length `n` for a Megaminx. Defaults to csTimer's default length of 70. """
    return dukpy.evaljs(file_list, scrambleType='carrot', n=n).replace('\n','').replace('  ',' ').replace('  ',' ')
    # return _UTIL_SCRAMBLER.call("util_scramble.getMegaminxCarrotScramble", n).replace('\n','').replace('  ',' ').replace('  ',' ')

@trim
def get_old_style_scramble(n=70):
    """ Gets an old-style scramble of length `n` for a Megaminx. Defaults to csTimer's default length of 70. """
    return dukpy.evaljs(file_list, scrambleType='old', n=n)
    # return _UTIL_SCRAMBLER.call("util_scramble.getMegaminxOldStyleScramble", n)