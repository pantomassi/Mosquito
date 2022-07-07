""" Validation of commands will not allow for passing invalid commands to the Tello object, but why not try to get some commands right the first time.

If multiple commands/nums recognized by the program can be misheard as the same word- no conversion is made. E.g. both 'ten' and 'turn' are sometimes misheard as 'the', so there's no replacement for 'the' to avoid unexpected behavior.

Whenever possible, chose the shorter possible word for a command to avoid potential collisions. Example: 'go' is less prone to misheards than 'move'.

!!! Iterate through more complex keys first.
"""

import re


CONVERSION_DICT = {
    'four our the': 'forward',
    'four working': 'forward',
    'four or': 'forward',
    'for or': 'forward',
    'philip four': 'flip forward',
    'philip for': 'flip forward',
    ' o ': ' oh ',
    'while': 'one',
    ' to ': ' two ',
    'through': 'three',
    'far ': 'four ',
    'for ': 'four ',
    'seeks': 'six',
    'then': 'ten',
    'alladin': 'eleven',
    'authority': 'forty',
    'forwardy': 'forty',
    'party': 'forty',
    'lan ': 'land ',
    'landd': 'land',
    'plan': 'land',
    'when': 'land',
    'no': 'go',
    'yo': 'go',
    'darn': 'turn',
    'during': 'turn',
    'her': 'turn',
    'terry': 'turn',
    'their': 'turn',
    'turner': 'turn',
    'turning': 'turn',
    'philip': 'flip',
    'harvard': 'forward',
    'fourth': 'forward',
    'ford': 'forward',
    'fort ': 'forward ',
    ' op ': 'up',
    'now': 'down',
    'pack': 'back',
    'bag': 'back',
    'ride': 'right',
    'said': 'set',
    'buttery': 'battery',
    'lottery': 'battery',
    'marjorie': 'battery',
    'madrid': 'battery',
    'damp': 'temp',
    'temperature': 'temp'
    }



def replace_misheards(command, conversion_dict=CONVERSION_DICT):
    for key in conversion_dict:
        if key in command:
            command = re.sub(key, f'{conversion_dict[key]}', command)
    pre_filtered_command = command.split()
    return pre_filtered_command
