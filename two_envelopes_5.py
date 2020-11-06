#!/usr/bin/python3
__version__ = '0.0.2' # Time-stamp: <2020-11-06T17:58:52Z>
## Language: Japanese/UTF-8

"""The Two Envelopes Problem: Another Integer Version."""

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

ARGS.trials = 100000
ARGS.x_max = 200
ARGS.q = 50

def parse_args ():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--trials", type=int)
    parser.add_argument("--x-max", "--max", type=int)
    parser.add_argument("-q", type=int)
    parser.parse_args(namespace=ARGS)
    if ARGS.trials % 2 != 0:
        parser.error(message='The --trials must be an even number.')
    if ARGS.q % 2 != 0:
        parser.error(message='The -q must be an even number.')

def main ():
    valid1 = 0
    valid2 = 0
    s1 = 0
    s2 = 0
    for trial in range(ARGS.trials):
        r = random.randrange(2)
        x = random.randrange(1, ARGS.x_max + 1)
        if r == 0:
            a = x * 2
            b = x
        else:
            a = x
            b = x * 2
        if a <= ARGS.q:
            valid1 += 1
            s1 += np.array([a, b, r, x, b / a])
        if a == ARGS.q:
            valid2 += 1
            s2 += np.array([a, b, r, x, b / a])
    av1 = s1 / valid1
    av2 = s2 / valid2

    x = Symbol('x', integer=True)
    q = Symbol('q', integer=True)
    X = Symbol('X', real=True)
    y = Symbol('y', integer=True)

    if ARGS.q <= ARGS.x_max:
        n_a1 = summation(1, (x, 1, q/2))
        n_a2 = 0
        n_be = summation(1, (y, 1, q/2))
        n_bo = summation(1, (y, 1, q/2))
        E_a1_b = summation(x, (x, 1, q/2)) / n_a1
        E_be_b = summation((2 * x).subs([(x, 2 * y)]), (y, 1, q/2)) / n_be
        E_bo_b = summation((2 * x).subs([(x, 2 * y - 1)]), (y, 1, q/2)) / n_bo
        E_d_b = (n_a1 / (n_a1 + n_be + n_bo)) * E_a1_b \
            + (n_be / (n_a1 + n_be + n_bo)) * E_be_b \
            + (n_bo / (n_a1 + n_be + n_bo)) * E_bo_b
    else:
        n_a1 = summation(1, (x, 1, X/2))
        n_a2 = summation(1, (x, X/2 + 1, q/2))
        n_be = summation(1, (y, 1, X/2))
        n_bo = summation(1, (y, 1, X/2))
        E_a1_b = summation(x, (x, 1, X/2)) /n_a1
        E_a2_b = summation(x, (x, X/2 + 1, q/2)) / n_a2
        E_be_b = summation((2 * x).subs([(x, 2 * y)]), (y, 1, X/2)) / n_be
        E_bo_b = summation((2 * x).subs([(x, 2 * y - 1)]), (y, 1, X/2)) / n_bo
        E_d_b = (n_a1 / (n_a1 + n_a2 + n_be + n_bo)) * E_a1_b \
            + (n_a2 / (n_a1 + n_a2 + n_be + n_bo)) * E_a2_b \
            + (n_be / (n_a1 + n_a2 + n_be + n_bo)) * E_be_b \
            + (n_bo / (n_a1 + n_a2 + n_be + n_bo)) * E_bo_b

    if ARGS.q <= ARGS.x_max:
        n_a1 = summation(1, (x, 1, q/2))
        n_a2 = 0
        n_be = summation(1, (y, 1, q/2))
        n_bo = summation(1, (y, 1, q/2))
        E_a1_a = summation(2 * x, (x, 1, q/2)) / n_a1
        E_be_a = summation(x.subs([(x, 2 * y)]), (y, 1, q/2)) / n_be
        E_bo_a = summation(x.subs([(x, 2 * y - 1)]), (y, 1, q/2)) / n_bo
        E_d_a = (n_a1 / (n_a1 + n_be + n_bo)) * E_a1_a \
            + (n_be / (n_a1 + n_be + n_bo)) * E_be_a \
            + (n_bo / (n_a1 + n_be + n_bo)) * E_bo_a
    else:
        n_a1 = summation(1, (x, 1, X/2))
        n_a2 = summation(1, (x, X/2 + 1, q/2))
        n_be = summation(1, (y, 1, X/2))
        n_bo = summation(1, (y, 1, X/2))
        E_a1_a = summation(2 * x, (x, 1, X/2)) / n_a1
        E_a2_a = summation(2 * x, (x, X/2 + 1, q/2)) / n_a2
        E_be_a = summation(x.subs([(x, 2 * y)]), (y, 1, X/2)) / n_be
        E_bo_a = summation(x.subs([(x, 2 * y - 1)]), (y, 1, X/2)) / n_bo
        E_d_a = (n_a1 / (n_a1 + n_a2 + n_be + n_bo)) * E_a1_a \
            + (n_a2 / (n_a1 + n_a2 + n_be + n_bo)) * E_a2_a \
            + (n_be / (n_a1 + n_a2 + n_be + n_bo)) * E_be_a \
            + (n_bo / (n_a1 + n_a2 + n_be + n_bo)) * E_bo_a
        
    if ARGS.q <= ARGS.x_max:
        n_a1 = summation(1, (x, 1, q/2))
        n_a2 = 0
        n_be = summation(1, (y, 1, q/2))
        n_bo = summation(1, (y, 1, q/2))
        E_a1_ba = summation(Rational(1, 2), (x, 1, q/2)) / n_a1
        E_be_ba = summation(2, (y, 1, q/2)) / n_be
        E_bo_ba = summation(2, (y, 1, q/2)) / n_bo
        E_d_ba = (n_a1 / (n_a1 + n_be + n_bo)) * E_a1_ba \
            + (n_be / (n_a1 + n_be + n_bo)) * E_be_ba \
            + (n_bo / (n_a1 + n_be + n_bo)) * E_bo_ba
    else:
        n_a1 = summation(1, (x, 1, X/2))
        n_a2 = summation(1, (x, X/2 + 1, q/2))
        n_be = summation(1, (y, 1, X/2))
        n_bo = summation(1, (y, 1, X/2))
        E_a1_ba = summation(Rational(1, 2), (x, 1, X/2)) / n_a1
        E_a2_ba = summation(Rational(1, 2), (x, X/2 + 1, q/2)) / n_a2
        E_be_ba = summation(2, (y, 1, X/2)) / n_be
        E_bo_ba = summation(2, (y, 1, X/2)) / n_bo
        E_d_ba = (n_a1 / (n_a1 + n_a2 + n_be + n_bo)) * E_a1_ba \
            + (n_a2 / (n_a1 + n_a2 + n_be + n_bo)) * E_a2_ba \
            + (n_be / (n_a1 + n_a2 + n_be + n_bo)) * E_be_ba \
            + (n_bo / (n_a1 + n_a2 + n_be + n_bo)) * E_bo_ba

    if ARGS.q <= ARGS.x_max:
        if ARGS.q == 2:
            E_q_b_ = E_d_b.subs([(q, 2)])
        else:
            E_q_b_ = (E_d_b.subs([(q, q)]) - E_d_b.subs([(q, q - 2)])) * Rational(1, 2)
        E_q_b = ((q/2) * (1 * 1 / (X * 2)) + (2 * q) * (1 * 1 / (X * 2))) \
            / (1 * 1 / (X * 2) + 1 * 1 / (X * 2))
        E_q_a = (q * (1 * 1 / (X * 2)) + q * (1 * 1 / (X * 2))) \
            / ((1 * 1 / (X * 2)) + (1 * 1 / (X * 2)))
        E_q_ba = (Rational(1, 2) * (1 * 1 / (X * 2)) + 2 * (1 * 1 / (X * 2))) \
            / ((1 * 1 / (X * 2)) + (1 * 1 / (X * 2)))
    else:
        if ARGS.q == ARGS.x_max + 2:
            E_q_b_ = E_d_b.subs([(q, ARGS.x_max + 2)])
        else:
            E_q_b_ = (E_d_b.subs([(q, q)]) - E_d_b.subs([(q, q - 2)])) * Rational(1, 2)
        E_q_b = (q/2) * (1 * 1 / (X * 2)) / (1 * 1 / (X * 2))
        E_q_a = q * (1 * 1 / (X * 2)) / (1 * 1 / (X * 2))
        E_q_ba = Rational(1, 2) * (1 * 1 / (X * 2)) / (1 * 1 / (X * 2))

    f = lambda z: z.subs([(X, ARGS.x_max), (q, ARGS.q)]).simplify().evalf()
    
    print("Realm: d")
    print("valid:", valid1, "/", ARGS.trials)
    print("E(A) =", av1[0], "(==", f(E_d_a), ")")
    print("E(B) =", av1[1], "(==", f(E_d_b), ")")
    print("E(X) =", av1[3])
    print("E(B/A) =", av1[4], "(==", f(E_d_ba), ")")
    print("E(B)/E(A) =", av1[1] / av1[0], "(==", f(E_d_b / E_d_a), ")")
    
    print("Realm: q")
    print("valid:", valid2, "/", ARGS.trials)
    print("E(A) =", av2[0], "(==", f(E_q_a), ")")
    print("E(B) =", av2[1], "(==", f(E_q_b))
    print("E(B) =", av2[1], "(!=", f(E_q_b_), "==", simplify(E_q_b_), ")")
    print("E(X) =", av2[3])
    print("E(B/A) =", av2[4], "(==", f(E_q_ba), ")")
    print("E(B)/E(A) =", av2[1] / av2[0], "(==", f(E_q_b / E_q_a), ")")

if __name__ == '__main__':
    parse_args()
    main()
