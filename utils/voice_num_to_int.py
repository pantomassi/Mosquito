"""
Helper method for converting {distance/speed} measurements passed through voice commands. Max speed is 100cm/s (original Tello's cap). Max distance per one commmand is set to 999cm (393.3 in) or 9.99m (32.78 ft).
Strings containing other words than numbers return None. Strings containing valid numbers, but not following the accepted convention- default to None.

"""

numbers = {
    'oh' : 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred': 100,
}

singles = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
tens = ('twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')


def word_to_num(word):
    if word in numbers:
        return numbers[word]
    return None


def conv_one_word_num(number_as_list):
    return word_to_num(number_as_list[0])


def conv_two_words_num(number_as_list):
    sum = 0
    if number_as_list[1] == "hundred":
        sum += word_to_num(number_as_list[0])*100
    elif number_as_list[0] in tens and number_as_list[1] not in tens:
        sum += word_to_num(number_as_list[0]) + word_to_num(number_as_list[1])
    elif number_as_list[0] in singles:
        sum += word_to_num(number_as_list[0])*100 + word_to_num(number_as_list[1])
    else:
        sum = None
    return sum


def conv_three_words_num(number_as_list):
    sum = 0
    if number_as_list[0] in singles and number_as_list[2] in singles:
        if number_as_list[1] == "oh":
            sum += word_to_num(number_as_list[0])*100 + word_to_num(number_as_list[2])
        elif number_as_list[1] in tens:
            sum += word_to_num(number_as_list[0])*100 + word_to_num(number_as_list[1]) + word_to_num(number_as_list[2])
    else:
        sum = None
    return sum



def voice_num_to_int(number_as_list):
    converted_num = None
    
    if len(number_as_list) == 1:
        converted_num = conv_one_word_num(number_as_list)
    elif len(number_as_list) == 2:
        converted_num = conv_two_words_num(number_as_list)
    elif len(number_as_list) == 3:
        converted_num = conv_three_words_num(number_as_list)

    return converted_num
