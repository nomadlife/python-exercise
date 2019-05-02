def usage():
    print("""
    Usage:
    python count_alphabet.py [textfile]

    options:
    -h --help       Show this screen

    """)

import sys, getopt

def main(argv):
    try:
        opts, atgs = getopt.getopt(argv, 'h', ['help'])
    except:
        print('Usage: python count_alphabet.py [textfile] ')
        print('or -h or --help for help')
        sys.exit()
    for opt, arg in opts:
        if opt in ('-h','--help'):
            usage()
            sys.exit(2)
        else:
            assert False, "Unhandled option"



if __main__ == "__main__":
    if len(sys.argv) > 1:
        main(argv)
    else:
        print('Usage: python count_alphabet.py [textfile] ')
        print('or -h or --help for help')
        sys.exit()
