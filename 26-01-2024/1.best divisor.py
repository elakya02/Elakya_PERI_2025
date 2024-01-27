"""Kristen loves playing with and comparing numbers. She thinks that if she takes two different positive numbers, the one whose digits sum to a larger number is better than the other. If the sum of digits is equal for both numbers, then she thinks the smaller number is better. For example, Kristen thinks that  is better than  and that  is better than .

Given an integer, , can you find the divisor of  that Kristin will consider to be the best?

Input Format

A single integer denoting .

Constraints

Output Format

Print an integer denoting the best divisor of .

Sample Input 0

12
Sample Output 0

6
Explanation 0

The set of divisors of  can be expressed as . The divisor whose digits sum to the largest number is  (which, having only one digit, sums to itself). Thus, we print  as our answer.
"""

import math
import os
import random
import re
import sys

def best_divisor(n):
    def digit_sum(digit):
        return sum(int(num) for num in str(digit))

    maximum_no = 1
    best_no = 1

    for i in range(1, n + 1):
        if n % i == 0:
            present_sum = digit_sum(i)
            if present_sum > maximum_no:
                maximum_no = present_sum
                best_no = i

    return best_no

if __name__ == '__main__':
    n = int(input().strip())
    result = best_divisor(n)
    print(result) 
