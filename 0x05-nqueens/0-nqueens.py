#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens
on an NxN chessboard. Write a program that solves the N queens problem.
"""

import sys


def is_available(queens, i, j):
    """checks if a spot is available"""
    for x, y in queens:
        if i == x or j == y or abs(i - x) == abs(j - y):
            return False
    return True


def queen_down(N, queens, final_combo):
    """recursive function to put down non attacking queens"""
    if len(queens) == N:
        sorted_queens = sorted(queens, key=lambda x: x[0])
        if sorted_queens not in final_combo:
            final_combo.append(sorted_queens)
        return final_combo
    for i in range(N):
        if any(i == x[0] for x in queens):
            continue
        for j in range(N):
            if is_available(queens, i, j):
                queen_down(N, queens + [[i, j]], final_combo)
                break
    return final_combo


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)
queens = []
queen_down(N, [], queens)
for queen in queens:
    print(queen)
