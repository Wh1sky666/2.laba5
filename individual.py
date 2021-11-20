#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def summ(*args):
    if args:
        total = 0
        count = 0

        values = [int(arg) for arg in args]

        for idx in values:
            if idx == 0:
                count += 1
            if count == 1:
                total += idx
            if count == 2:
                return total
    else:
        return None


if __name__ == "__main__":
    print(summ(1, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9))
    print(summ(42, 16, 900, 0, 5, 5, 0, 856, 341, 15))
