#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
%(scriptName)s Script Description:

This tee is designed to handle text font colors.

"""

#=============================================================

import os, sys, re

scriptName = os.path.basename(__file__).replace('.pyc', '.py')
scriptDir  = os.path.dirname(os.path.realpath(__file__))

sys.path.append(scriptDir + '/lib')
sys.path.append(scriptDir + '/bin')

import getopt

#=============================================================

if sys.version_info[0] == 3:
    xrange = range

#====================================================

def get_docstring():
    # all_option_preconfigured_string = '            ' + '\n            '.join([key+' '+value for x in all_option_preconfigured for key, value in dict.items(x)])
    all_option_preconfigured_string = '\n            '.join([key+' '+value for x in all_option_preconfigured for key, value in dict.items(x)])
    return __doc__ % {'scriptName': scriptName, 'all_option_preconfigured': all_option_preconfigured_string,}


def usage(exit_or_return='exit'):
    printout(get_docstring())
    if exit_or_return == 'exit':
        sys.exit(1)
    else:
        return

#====================================================


if __name__ == '__main__':


    try:
        opts, args = getopt.getopt(sys.argv[1:], "a:", ["a=", "h"])
    except getopt.GetoptError as err:
        reportError("Runstring " + str(err))
        usage()

    output_file = ''
    output_file_mode = 'w'
    for opt, arg in opts:
        if opt == "-a" or opt == "--a":
            output_file = arg
            output_file_mode = 'a'
        elif opt == "--h":
            usage()
        else:
            reportError("Unrecognized runstring option: " + opt)
            usage()

    if output_file == "":
        if len(sys.argv) == 2:
            output_file = sys.argv[1]
        else:
            print("ERROR: Missing output filename.")
            sys.exit(1)

    outfd = open(output_file, output_file_mode)
    for line in sys.stdin:
        outfd.write(line)
        sys.stdout.write(line)
        # print(line)
        sys.stdout.flush()

   






