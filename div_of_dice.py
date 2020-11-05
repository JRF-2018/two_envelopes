#!/usr/bin/python3
__version__ = '0.0.1' # Time-stamp: <2020-11-02T06:44:04Z>
## Language: Japanese/UTF-8

"""The Two Envelopes Problem: Division of Two Dices."""

##
## License:
##
##   Public Domain
##   (Since this small code is close to be mathematically trivial.)
##
## Author:
##
##   JRF
##   http://jrf.cocolog-nifty.com/software/
##   (The page is written in Japanese.)
##

import random
import numpy as np
import itertools
import argparse
ARGS = argparse.Namespace()

ARGS.trials = 10000

def parse_args ():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--trials", type=int)
    parser.parse_args(namespace=ARGS)

def main ():
    s = 0
    for trial in range(ARGS.trials):
        a = random.randrange(6) + 1
        b = random.randrange(6) + 1
        s += b/a
    s /= ARGS.trials

    e = np.mean([(i + 1)/ (j + 1)
                 for i, j in itertools.product(range(6), range(6))])

    print("E =", s, "(==", e, ")")

if __name__ == '__main__':
    parse_args()
    main()
