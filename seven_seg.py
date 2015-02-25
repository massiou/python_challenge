#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Seven seg module """

__copyright__ = "Copyright 2015, Matthieu Velay"

SEVEN_SEG_DICT = {
                  "0": (" _ ", "| |", "|_|"),
                  "1": ("   ", "  |", "  |"),
                  "2": (" _ ", " _|", "|_ "),
                  "3": (" _ ", " _|", " _|"),
                  "4": ("   ", "|_|", "  |"),
                  "5": (" _ ", "|_ ", " _|"),
                  "6": (" _ ", "|_ ", "|_|"),
                  "7": (" _ ", "  |", "  |"),
                  "8": (" _ ", "|_|", "|_|"),
                  "9": (" _ ", "|_|", " _|")
                  }

def seven_seg(input_string):
    """
    @goal: given a string return the seven segment output
    @param input_string: integer we want to display as seven-seg way
    @return output_string: seven-seg converted string
    """
    try:
        int(input_string)
        output_string = ''
        seven_list = [ SEVEN_SEG_DICT[number] for number in input_string ]
        for index in range(3):
            for pos in range(len(input_string)):
                output_string += ''.join(seven_list[pos][index])
            output_string += '\n'
    except ValueError as exc:
        raise exc

    return output_string
