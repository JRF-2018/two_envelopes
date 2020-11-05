#!/usr/bin/python3
__version__ = '0.0.1' # Time-stamp: <2020-11-02T08:32:46Z>
## Language: Japanese/UTF-8

"""The Two Envelopes Problem: Real Version."""

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
from sympy import *
#init_session(pretty_print=False)
import argparse
ARGS = argparse.Namespace()

ARGS.trials = 10000
ARGS.x_max = 200
ARGS.q = 0

def parse_args ():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--trials", type=int)
    parser.add_argument("--x-max", "--max", type=float)
    parser.add_argument("-q", type=float)
    parser.parse_args(namespace=ARGS)

def main ():
    s = 0
    valid = 0
    for trial in range(ARGS.trials):
        r = random.randrange(2)
        x = random.uniform(0, ARGS.x_max)
        if r == 0:
            a = 2 * x / 3
            b = x / 3
        else:
            a = x / 3
            b = 2 * x / 3
        if a > ARGS.x_max / 3 + ARGS.q:
            continue;
        valid += 1
        s += np.array([a, b, x, b / a])
    av_c = s / valid

    x = Symbol('x', real=True)
    X = Symbol('X', real=True)
    E_a1_b = integrate(Rational(1, 3) * x / (X / 2), (x, 0, X / 2))
    E_b_b = integrate(Rational(2, 3) * x / X, (x, 0, X))
    E_c_b = Rational(1, 3) * E_a1_b + Rational(2, 3) * E_b_b
    assert Eq(E_a1_b, X * Rational(1, 12)).simplify()
    assert Eq(E_b_b, X * Rational(1, 3)).simplify()
    assert Eq(E_c_b, X * Rational(1, 4)).simplify()

    E_a1_a = integrate(Rational(2, 3) * x / (X / 2), (x, 0, X / 2))
    E_b_a = integrate(Rational(1, 3) * x / X, (x, 0, X))
    E_c_a = Rational(1, 3) * E_a1_a + Rational(2, 3) * E_b_a
    assert Eq(E_a1_a, X * Rational(1, 6)).simplify()
    assert Eq(E_b_a, X * Rational(1, 6)).simplify()
    assert Eq(E_c_a, X * Rational(1, 6)).simplify()

    E_a1_ba = integrate(Rational(1, 2) / (X / 2), (x, 0, X / 2))
    E_b_ba = integrate(2 / X, (x, 0, X))
    E_c_ba = Rational(1, 3) * E_a1_ba + Rational(2, 3) * E_b_ba
    assert Eq(E_a1_ba, Rational(1, 2)).simplify()
    assert Eq(E_b_ba, 2).simplify()
    assert Eq(E_c_ba, Rational(3, 2)).simplify()

    E_c_a = E_c_a.subs([(X, ARGS.x_max)]).evalf()
    E_c_b = E_c_b.subs([(X, ARGS.x_max)]).evalf()
    E_c_ba = E_c_ba.subs([(X, ARGS.x_max)]).evalf()

    print("valid:", valid, "/", ARGS.trials)
    if ARGS.q == 0:
        print("E(A) =", av_c[0], "(==", E_c_a, ")")
        print("E(B) =", av_c[1], "(==", E_c_b, ")")
        print("E(X) =", av_c[2])
        print("E(B/A) =", av_c[3], "(==", E_c_ba, ")")
        print("E(B)/E(A) =", av_c[1] / av_c[0], "(==", E_c_b / E_c_a, ")")
    else:
        print("E(A) =", av_c[0])
        print("E(B) =", av_c[1])
        print("E(X) =", av_c[2])
        print("E(B/A) =", av_c[3])
        print("E(B)/E(A) =", av_c[1] / av_c[0])

if __name__ == '__main__':
    parse_args()
    main()
