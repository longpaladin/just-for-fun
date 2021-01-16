"""
Author: Pang Jin Jia
Last updated: 9 Jan 2021
"""

import random

new4Dnumber = random.randint(0,9999)

# Modulo string formatting
print('The 4D number you should buy is: %04d' % (new4Dnumber))

# Format method string formatting
print('The 4D number you should buy is: {:04d}'.format(new4Dnumber))

# F-string formatting
print(f'The 4D number you should buy is: {new4Dnumber:04d}')
