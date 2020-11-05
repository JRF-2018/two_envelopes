#!/usr/bin/python3
__version__ = '0.0.1' # Time-stamp: <2020-11-02T10:41:46Z>
## Language: Japanese/UTF-8

"""The Two Envelopes Problem: Closed Version."""

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
import argparse
ARGS = argparse.Namespace()

ARGS.trials = 10000
ARGS.x_max = 200

def parse_args ():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--trials", type=int)
    parser.add_argument("--x-max", "--max", type=int)
    parser.parse_args(namespace=ARGS)

def main ():
    s = 0
    for trial in range(ARGS.trials):
        r = random.randrange(2)
        x = random.randrange(1, ARGS.x_max + 1)
        if r == 0:
            a = x * 2
            b = x
        else:
            a = x
            b = x * 2
        s += np.array([a, b, x, b/a, a/b])
    av = s / ARGS.trials

    print("E(A) =", av[0])
    print("E(B) =", av[1])
    print("E(X) =", av[2])
    print("E(B/A) =", av[3], "(== 1.25)")
    print("E(A/B) =", av[4], "(== 1.25)")
    print("E(B)/E(A) =", av[1] / av[0], "(== 1.00)")

if __name__ == '__main__':
    parse_args()
    main()
