#!/usr/bin/python3
__version__ = '0.0.3' # Time-stamp: <2020-11-12T13:31:59Z>
## Language: Japanese/UTF-8

"""The Two Envelopes Problem: Integer Version."""

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

def parse_args ():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--trials", type=int)
    parser.add_argument("--x-max", "--max", type=int)
    parser.parse_args(namespace=ARGS)
    if ARGS.trials % 2 != 0:
        parser.error(message='The --trials must be an even number.')


def main ():
    trials = []
    for trial in range(ARGS.trials):
        r = random.randrange(2)
        x = random.randrange(1, ARGS.x_max + 1)
        if r == 0:
            a = x * 2
            b = x
        else:
            a = x
            b = x * 2
        trials.append([a, b, r, x, b / a])
    trials = np.array(trials)
    t_a = trials[:, 0]
    t_b = trials[:, 1]
    t_r = trials[:, 2]
    t_x = trials[:, 3]
    t_a1 = trials[(t_x <= ARGS.x_max / 2) & (t_r == 0)]
    t_a2 = trials[(t_x > ARGS.x_max / 2) & (t_r == 0)]
    t_be = trials[(t_r == 1) & (t_x % 2 == 0)]
    t_bo = trials[(t_r == 1) & (t_x % 2 == 1)]
    t_c = trials[(t_a <= ARGS.x_max) & (t_a % 2 == 0)]
    t_d = trials[t_a <= ARGS.x_max]
    t_a2_ = trials[t_a > ARGS.x_max]
    t_bo_ = trials[t_a % 2 == 1]
    assert t_a1.shape[0] + t_be.shape[0] == t_c.shape[0]
    assert t_c.shape[0] + t_bo.shape[0] == t_d.shape[0]
    assert np.all(t_a2 == t_a2_)
    assert np.all(t_bo == t_bo_)
    
    x = Symbol('x', integer=True)
    X = Symbol('X', integer=True)
    y = Symbol('y', integer=True)

    n_a1 = summation(1, (x, 1, X/2))
    n_a2 = summation(1, (x, X/2 + 1, X))
    n_be = summation(1, (y, 1, X/2))
    n_bo = summation(1, (y, 1, X/2))

    E_a1_b = summation(x, (x, 1, X/2)) / n_a1
    E_a2_b = summation(x, (x, X/2 + 1, X)) / n_a2
    E_be_b = summation((2 * x).subs([(x, 2 * y)]), (y, 1, X / 2)) / n_be
    E_bo_b = summation((2 * x).subs([(x, 2 * y - 1)]), (y, 1, X / 2)) / n_bo
    E_c_b = (n_a1 / (n_a1 + n_be)) * E_a1_b + (n_be / (n_a1 + n_be)) * E_be_b
    E_d_b = (n_a1 / (n_a1 + n_be + n_bo)) * E_a1_b \
        + (n_be / (n_a1 + n_be + n_bo)) * E_be_b \
        + (n_bo / (n_a1 + n_be + n_bo)) * E_bo_b
    E_omega_b = ((n_a1 + n_be) / (n_a1 + n_a2 + n_be + n_bo)) * E_c_b \
        + (n_a2 / (n_a1 + n_a2 + n_be + n_bo)) * E_a2_b \
        + (n_bo / (n_a1 + n_a2 + n_be + n_bo)) * E_bo_b
    assert Eq(E_a1_b, X/4 + 1/2).simplify()
    assert Eq(E_a2_b, 3*X/4 + 1/2).simplify()
    assert Eq(E_be_b, X + 2).simplify()
    assert Eq(E_bo_b, X).simplify()
    assert Eq(E_c_b, 5*X/8 + 5/4).simplify()
    assert Eq(E_d_b, 3*X/4 + 5/6).simplify()
    assert Eq(E_omega_b, 3*X/4 + 3/4).simplify()

    E_a1_a = summation(2 * x, (x, 1, X/2)) / n_a1
    E_a2_a = summation(2 * x, (x, X/2 + 1, X)) / n_a2
    E_be_a = summation(x.subs([(x, 2 * y)]), (y, 1, X / 2)) / n_be
    E_bo_a = summation(x.subs([(x, 2 * y - 1)]), (y, 1, X / 2)) / n_bo
    E_c_a = (n_a1 / (n_a1 + n_be)) * E_a1_a + (n_be / (n_a1 + n_be)) * E_be_a
    E_d_a = (n_a1 / (n_a1 + n_be + n_bo)) * E_a1_a \
        + (n_be / (n_a1 + n_be + n_bo)) * E_be_a \
        + (n_bo / (n_a1 + n_be + n_bo)) * E_bo_a
    E_omega_a = ((n_a1 + n_be) / (n_a1 + n_a2 + n_be + n_bo)) * E_c_a \
        + (n_a2 / (n_a1 + n_a2 + n_be + n_bo)) * E_a2_a \
        + (n_bo / (n_a1 + n_a2 + n_be + n_bo)) * E_bo_a
    assert Eq(E_a1_a, X/2 + 1).simplify()
    assert Eq(E_a2_a, 3*X/2 + 1).simplify()
    assert Eq(E_be_a, X/2 + 1).simplify()
    assert Eq(E_bo_a, X/2).simplify()
    assert Eq(E_c_a, X/2 + 1).simplify()
    assert Eq(E_d_a, X/2 + 2/3).simplify()
    assert Eq(E_omega_a, 3*X/4 + 3/4).simplify()

    E_a1_ba = summation(Rational(1, 2), (x, 1, X/2)) / n_a1
    E_a2_ba = summation(Rational(1, 2), (x, X/2 + 1, X)) / n_a2
    E_be_ba = summation(2, (y, 1, X / 2)) / n_be
    E_bo_ba = summation(2, (y, 1, X / 2)) / n_bo
    E_c_ba = (n_a1 / (n_a1 + n_be)) * E_a1_ba + (n_be / (n_a1 + n_be)) * E_be_ba
    E_d_ba = (n_a1 / (n_a1 + n_be + n_bo)) * E_a1_ba \
        + (n_be / (n_a1 + n_be + n_bo)) * E_be_ba \
        + (n_bo / (n_a1 + n_be + n_bo)) * E_bo_ba
    E_omega_ba = ((n_a1 + n_be) / (n_a1 + n_a2 + n_be + n_bo)) * E_c_ba \
        + (n_a2 / (n_a1 + n_a2 + n_be + n_bo)) * E_a2_ba \
        + (n_bo / (n_a1 + n_a2 + n_be + n_bo)) * E_bo_ba
    assert Eq(E_a1_ba, 1/2).simplify()
    assert Eq(E_a2_ba, 1/2).simplify()
    assert Eq(E_be_ba, 2).simplify()
    assert Eq(E_bo_ba, 2).simplify()
    assert Eq(E_c_ba, 5/4).simplify()
    assert Eq(E_d_ba, 3/2).simplify()
    assert Eq(E_omega_ba, 5/4).simplify()

    f = lambda q: q.subs([(X, ARGS.x_max)]).simplify().evalf()
    
    print("Realm: c")
    av_c = np.mean(t_c, axis=0)
    print("valid:", t_c.shape[0], "/", ARGS.trials)
    print("E(A) =", av_c[0], "(==", f(E_c_a), ")")
    print("E(B) =", av_c[1], "(==", f(E_c_b), ")")
    print("E(X) =", av_c[3])
    print("E(B/A) =", av_c[4], "(==", f(E_c_ba), ")")
    print("E(B)/E(A) =", av_c[1] / av_c[0], "(==", f(E_c_b / E_c_a), ")")

    print("\nRealm: a2")
    av_a2 = np.mean(t_a2, axis=0)
    print("valid:", t_a2.shape[0], "/", ARGS.trials)
    print("E(A) =", av_a2[0], "(==", f(E_a2_a), ")")
    print("E(B) =", av_a2[1], "(==", f(E_a2_b), ")")
    print("E(X) =", av_a2[3])
    print("E(B/A) =", av_a2[4], "(==", f(E_a2_ba), ")")
    print("E(B)/E(A) =", av_a2[1] / av_a2[0], "(==", f(E_a2_b / E_a2_a), ")")

    print("\nRealm: bo")
    av_bo = np.mean(t_bo, axis=0)
    print("valid:", t_bo.shape[0], "/", ARGS.trials)
    print("E(A) =", av_bo[0], "(==", f(E_bo_a), ")")
    print("E(B) =", av_bo[1], "(==", f(E_bo_b), ")")
    print("E(X) =", av_bo[3])
    print("E(B/A) =", av_bo[4], "(==", f(E_bo_ba), ")")
    print("E(B)/E(A) =", av_bo[1] / av_bo[0], "(==", f(E_bo_b / E_bo_a), ")")

    print("\nRealm: d")
    av_d = np.mean(t_d, axis=0)
    print("valid:", t_d.shape[0], "/", ARGS.trials)
    print("E(A) =", av_d[0], "(==", f(E_d_a), ")")
    print("E(B) =", av_d[1], "(==", f(E_d_b), ")")
    print("E(X) =", av_d[3])
    print("E(B/A) =", av_d[4], "(==", f(E_d_ba), ")")
    print("E(B)/E(A) =", av_d[1] / av_d[0], "(==", f(E_d_b / E_d_a), ")")
    assert Eq(E_d_b/E_d_a, (9 * X + 10) / (6 * X + 8)).simplify()
    #plot(E_d_b/E_d_a, (X, 0, 100))

    print("\nRealm: Omega")
    av_omega = np.mean(trials, axis=0)
    print("valid:", ARGS.trials)
    print("E(A) =", av_omega[0], "(==", f(E_omega_a), ")")
    print("E(B) =", av_omega[1], "(==", f(E_omega_b), ")")
    print("E(X) =", av_omega[3])
    print("E(B/A) =", av_omega[4], "(==", f(E_omega_ba), ")")
    print("E(B)/E(A) =", av_omega[1] / av_omega[0], "(==",
          f(E_omega_b / E_omega_a), ")")
    
if __name__ == '__main__':
    parse_args()
    main()
