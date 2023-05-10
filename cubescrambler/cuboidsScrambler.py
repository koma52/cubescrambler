from . import trim, MATHLIB_SRC, SCRAMBLE_SRC, SCRAMBLE_333_SRC, MEGA_SCRAMBLE_SRC, SCRAMBLE_223_SRC, SCRAMBLE_133_SRC
import dukpy

#------------------------------------------------------------------------------

file_list = [MATHLIB_SRC, SCRAMBLE_SRC, SCRAMBLE_333_SRC, MEGA_SCRAMBLE_SRC, SCRAMBLE_223_SRC, SCRAMBLE_133_SRC]

@trim
def get_1x1x2_scramble():
    """ Gets a random scramble for a 1x1x2 cuboid (lul). """
    return dukpy.evaljs(file_list, scrambleType='112')

@trim
def get_1x3x3_scramble():
    """ Gets a random scramble for a 1x3x3 cuboid. """
    return dukpy.evaljs(file_list, scrambleType='133')

@trim
def get_floppy_cube_scramble():
    """ Gets a random scramble for a 1x3x3 cuboid. Alias of 1x3x3. """
    return get_1x3x3_scramble()

@trim
def get_super_floppy_cube_scramble():
    """ Gets a random scramble for a 1x3x3 super floppy cuboid. """
    return dukpy.evaljs(file_list, scrambleType='super_floppy')

@trim
def get_2x2x3_scramble():
    """ Gets a random scramble for a 2x2x3 cuboid. """
    return dukpy.evaljs(file_list, scrambleType='223')

@trim
def get_3x3x2_scramble():
    """ Gets a random scramble for a 3x3x2 cuboid. """
    return dukpy.evaljs(file_list, scrambleType='332')

@trim
def get_3x3x4_scramble():
    """ Gets a random scramble for a 3x3x4 cuboid. """
    return dukpy.evaljs(file_list, scrambleType='334')

@trim
def get_3x3x5_scramble(n=25):
    """ Gets a random scramble for a 3x3x5 cuboid, where `n` is the length of the non-3x3x3 portion of the scramble. """
    return dukpy.evaljs(file_list, scrambleType='335', n=n)

@trim
def get_3x3x6_scramble():
    """ Gets a random scramble for a 3x3x6 cuboid. """
    return dukpy.evaljs(file_list, scrambleType='336')

@trim
def get_3x3x7_scramble(n=40):
    """ Gets a random scramble for a 3x3x7 cuboid, where `n` is the length of the non-3x3x3 portion of the scramble. """
    return dukpy.evaljs(file_list, scrambleType='337', n=n)
