""" Once possible misheards are turned into valid operations, check further if the command follows the convention of forming commands.
"""
from utils.voice_num_to_int import voice_num_to_int
import re


ONE_WORD_COMMANDS = ('exit', 'battery', 'status', 'altitude', 'cool', 'temp', 'picture', 'video', 'take off', 'land', 'emergency')


def is_valid_one_word_command(command_breakdown):
    if command_breakdown[0] in ONE_WORD_COMMANDS:
        return command_breakdown
    return ['invalid']


def is_valid_two_words_command(command_breakdown):
    operation = ' '.join(command_breakdown)
    valid_pattern = re.compile(r"(take off|stop video|turn back|flip (left|right|forward|back))$")

    is_valid = bool(re.match(valid_pattern, operation))
    if is_valid:
        return command_breakdown
    return ['invalid']




def is_valid_three_plus_words_command(command_breakdown): 
    maneuver_part = ' '.join(command_breakdown[:2])
    num_part = str(voice_num_to_int(command_breakdown[2:]))

    valid_maneuver_pattern = re.compile(r"set speed|go (left|right|forward|back|up|down)|turn (left|right)$")
    valid_number_pattern = re.compile(r"[1-9]\d{1,2}$")

    is_valid = bool(re.match(valid_maneuver_pattern, maneuver_part)) and bool(re.match(valid_number_pattern, num_part))
    if is_valid:
        return command_breakdown
    return ['invalid']



def validate_command(command_breakdown):
    result = ['invalid']

    if len(command_breakdown) == 0:
        result = ['empty']
    if len(command_breakdown) == 1:
        result = is_valid_one_word_command(command_breakdown)
    elif len(command_breakdown) == 2:
        result = is_valid_two_words_command(command_breakdown)
    elif 2 < len(command_breakdown) < 6:
        result = is_valid_three_plus_words_command(command_breakdown)

    return result
