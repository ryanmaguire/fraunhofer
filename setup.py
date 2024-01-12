"""
################################################################################
#                                   LICENSE                                    #
################################################################################
#   This file is free software: you can redistribute it and/or modify          #
#   it under the terms of the GNU General Public License as published by       #
#   the Free Software Foundation, either version 3 of the License, or          #
#   (at your option) any later version.                                        #
#                                                                              #
#   This file is distributed in the hope that it will be useful,               #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of             #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              #
#   GNU General Public License for more details.                               #
#                                                                              #
#   You should have received a copy of the GNU General Public License          #
#   along with this file.  If not, see <https://www.gnu.org/licenses/>.        #
################################################################################
#   Purpose:                                                                   #
#       Compiles all of the C code and assembles the Python module.            #
################################################################################
#   Author:     Ryan Maguire                                                   #
#   Date:       January 12, 2024                                               #
################################################################################
"""

from numpy.distutils.misc_util import Configuration
from numpy.distutils.core import setup

# Use the numpy setup tools to compile the C file.
def configuration(parent_package = '', top_path = None):
    """
        Function:
            configuration
        Purpose:
            Creates the Python module from the C source file.
    """

    config = Configuration(
        package_name = None,
        parent_name = parent_package,
        top_path = top_path
    )

    config.add_extension(
        'fraunhofer',
        ['fraunhofer.c'],
        libraries = ["tmpl"]
    )

    return config

# Creates the Python module from the C source file.
if __name__ == "__main__":
    setup(configuration = configuration)
