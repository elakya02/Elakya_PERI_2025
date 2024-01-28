"""
Two words are anagrams of one another if their letters can be rearranged to form the other word.

Given a string, split it into two contiguous substrings of equal length. Determine the minimum number of characters to change to make the two substrings into anagrams of one another.

Example

Break  into two parts: 'abc' and 'cde'. Note that all letters have been used, the substrings are contiguous and their lengths are equal. Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec' and 'cde' which are anagrams. Two changes were necessary.

Function Description

Complete the anagram function in the editor below.

anagram has the following parameter(s):

string s: a string
Returns

int: the minimum number of characters to change or -1.
Input Format

The first line will contain an integer, , the number of test cases.
Each test case will contain a string .

Constraints


 consists only of characters in the range ascii[a-z].
Sample Input

6
aaabbb
ab
abc
mnop
xyyx
xaxbbbxx
Sample Output

3
1
-1
2
0
1

"""

def maxMin(k, arr):
    arr.sort()
    minimum_diff = max(arr)
    for i in range(n-k+1):
        minimum_diff = min(minimum_diff , arr[i+k-1]-arr[i])
    return minimum_diff
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
