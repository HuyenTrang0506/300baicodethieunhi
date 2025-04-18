'''Step 1: Count the frequency of each character in the string.

Step 2:
If more than one character has an odd frequency, print "NO SOLUTION".

If the conditions are met, proceed to construct the palindrome.

Step 3:
For each character with an even frequency, place half of the characters on the left and the other half on the right.

For the character with an odd frequency (if applicable), place it in the center of the palindrome.'''
from collections import Counter
import sys

def palindrome(s):
    count = Counter(s)

    # Step 1: Count the frequency of each character
    odd_chars = [char for char, freq in count.items() if freq % 2 == 1]

    # Step 2: If more than one character has an odd frequency, print "NO SOLUTION"
    if len(odd_chars) > 1:
        return "NO SOLUTION"

    # Step 3: Construct the palindrome
    left_half = []
    middle_char = ''

    # For characters with even frequency, split them equally to form the left and right sides
    for char, freq in count.items():
        if freq % 2 == 0:
            left_half.append(char * (freq // 2))
        else:
            middle_char = char * freq

    # Join left half, middle character (if any), and the reverse of left half
    palindrome = ''.join(left_half) + middle_char + ''.join(left_half)[::-1]
    return palindrome


s = sys.stdin.read().strip()
print(palindrome(s))